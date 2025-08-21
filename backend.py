import psycopg2
import os

# Function to establish a database connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASS'),
            host=os.getenv('DB_HOST')
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error connecting to database: {e}")
        return None

# --- User Management CRUD ---
def create_user(name, email, weight_kg):
    conn = get_db_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (name, email, weight_kg) VALUES (%s, %s, %s) RETURNING user_id;", (name, email, weight_kg))
            user_id = cur.fetchone()[0]
            conn.commit()
            return user_id

def read_user(user_id):
    conn = get_db_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users WHERE user_id = %s;", (user_id,))
            return cur.fetchone()

# --- Workout Tracking CRUD ---
def create_workout(user_id, workout_data):
    # This function would handle both the workout and its exercises in a transaction.
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO workouts (user_id, workout_date, duration_minutes, notes) VALUES (%s, %s, %s, %s) RETURNING workout_id;",
                            (user_id, workout_data['date'], workout_data['duration_minutes'], workout_data['notes']))
                workout_id = cur.fetchone()[0]
                for exercise in workout_data['exercises']:
                    cur.execute("INSERT INTO exercises (workout_id, name, sets, reps, weight_kg) VALUES (%s, %s, %s, %s, %s);",
                                (workout_id, exercise['name'], exercise['sets'], exercise['reps'], exercise['weight_kg']))
            conn.commit()
            return True
        except psycopg2.Error as e:
            conn.rollback()
            print(f"Error logging workout: {e}")
            return False

def read_user_workouts(user_id):
    conn = get_db_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM workouts WHERE user_id = %s ORDER BY workout_date DESC;", (user_id,))
            return cur.fetchall()

# --- Goal Setting CRUD ---
def create_goal(user_id, description, target, start_date, end_date):
    conn = get_db_connection()
    if conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO goals (user_id, description, target_value, start_date, end_date) VALUES (%s, %s, %s, %s, %s);",
                        (user_id, description, target, start_date, end_date))
            conn.commit()

# --- Business Insights Functions ---
def get_business_insights():
    conn = get_db_connection()
    insights = {}
    if conn:
        with conn.cursor() as cur:
            # COUNT: Total number of workouts logged
            cur.execute("SELECT COUNT(*) FROM workouts;")
            insights['total_workouts'] = cur.fetchone()[0]

            # AVG: Average workout duration
            cur.execute("SELECT AVG(duration_minutes) FROM workouts;")
            insights['avg_workout_duration'] = cur.fetchone()[0]

            # SUM: Total weight lifted across all exercises
            cur.execute("SELECT SUM(weight_kg) FROM exercises;")
            insights['total_weight_lifted'] = cur.fetchone()[0]

            # MAX: Maximum weight lifted in a single exercise
            cur.execute("SELECT MAX(weight_kg) FROM exercises;")
            insights['max_weight_lifted_single_exercise'] = cur.fetchone()[0]

            # MIN: Minimum reps performed in any exercise
            cur.execute("SELECT MIN(reps) FROM exercises;")
            insights['min_reps_per_exercise'] = cur.fetchone()[0]
    return insights