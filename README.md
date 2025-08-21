# Fitness-Tracker
FitFriends Fitness Tracker
Welcome to the FitFriends Fitness Tracker, a personal application designed to help individuals track their fitness activities, set goals, and share progress with a small group of friends. This project is built using a modern Python-based stack with a clear separation of concerns, following CRUD principles for a maintainable codebase.

<br>

<br>

🎯 Features
User Profile Management: Create and update a personal profile, including name, email, and weight.

Workout & Progress Tracking: Log workouts with details like duration and exercises performed (including sets, reps, and weight lifted). Visualize progress over time.

Social Connections: Connect with friends to form a social network within the app.

Dynamic Leaderboard: View a real-time leaderboard that ranks friends based on a chosen metric, such as total workout minutes for the week.

Personal Goal Setting: Set and track personal fitness goals.

Business Insights Dashboard: Gain valuable insights from fitness data using SQL aggregate functions.

<br>

<br>

🛠️ Technical Stack
Frontend: Streamlit

Backend: Python

Database: PostgreSQL

Database Connector: psycopg2

<br>

<br>

📂 Repository Structure
The project is organized into two primary files to separate the business logic from the user interface.

backend.py: Handles all interactions with the PostgreSQL database. It contains functions for every Create, Read, Update, and Delete (CRUD) operation.

frontend.py: The Streamlit application that provides the user interface. It imports functions from backend.py to display data and capture user input.

<br>

<br>

📦 Database Schema
The database schema is designed to be relational and efficient, supporting all application features.

SQL

-- SQL code to create the necessary tables
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    weight_kg DECIMAL(5, 2)
);

CREATE TABLE friends (
    user_id_1 INTEGER REFERENCES users(user_id),
    user_id_2 INTEGER REFERENCES users(user_id),
    PRIMARY KEY (user_id_1, user_id_2),
    CHECK (user_id_1 <> user_id_2)
);

CREATE TABLE workouts (
    workout_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    workout_date DATE NOT NULL,
    duration_minutes INTEGER NOT NULL,
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE exercises (
    exercise_id SERIAL PRIMARY KEY,
    workout_id INTEGER REFERENCES workouts(workout_id),
    name VARCHAR(255) NOT NULL,
    sets INTEGER NOT NULL,
    reps INTEGER NOT NULL,
    weight_kg DECIMAL(6, 2),
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id)
);

CREATE TABLE goals (
    goal_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    description TEXT NOT NULL,
    target_value INTEGER,
    current_value INTEGER,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
<br>

<br>

🚀 How to Run the Application
Clone the repository:

Bash

git clone <repository_url>
cd <repository_name>
Set up the environment:

Ensure Python and PostgreSQL are installed on your system.

Create a dedicated database for the application.

Run the SQL code above to create the necessary tables.

Install dependencies:

Bash

pip install -r requirements.txt
(Note: You will need to create a requirements.txt file containing streamlit and psycopg2.)

Configure database connection:

Create a .env file in the root directory.

Add your database credentials to the file.

Code snippet

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASS=your_db_password
DB_HOST=localhost
Run the application:

Bash

streamlit run frontend.py
The application will launch in your web browser.
