import streamlit as st
import backend as db # Import your backend module

st.set_page_config(layout="wide", page_title="Fitness Tracker")

# Navigation sidebar
st.sidebar.title("FitFriends App")
page = st.sidebar.radio("Navigate", ["Log Workout", "My Profile", "Workout History", "Leaderboard", "Goals", "Business Insights"])

# Page for logging a new workout
if page == "Log Workout":
    st.header("🏋️‍♂️ Log Your Workout")
    with st.form("new_workout_form"):
        # Form fields for date, duration, and notes
        st.subheader("Workout Details")
        date = st.date_input("Date")
        duration = st.number_input("Duration (minutes)", min_value=1)
        notes = st.text_area("Notes")

        # Dynamic fields for exercises
        st.subheader("Exercises")
        num_exercises = st.number_input("Number of exercises", min_value=1, value=1)
        exercises = []
        for i in range(num_exercises):
            st.markdown(f"**Exercise {i+1}**")
            name = st.text_input(f"Name", key=f"ex_name_{i}")
            sets = st.number_input("Sets", min_value=1, key=f"ex_sets_{i}")
            reps = st.number_input("Reps", min_value=1, key=f"ex_reps_{i}")
            weight = st.number_input("Weight (kg)", min_value=0.0, key=f"ex_weight_{i}")
            exercises.append({'name': name, 'sets': sets, 'reps': reps, 'weight_kg': weight})

        submit_button = st.form_submit_button("Log Workout")
        if submit_button:
            workout_data = {
                'date': date,
                'duration_minutes': duration,
                'notes': notes,
                'exercises': exercises
            }
            if db.create_workout(st.session_state['user_id'], workout_data):
                st.success("Workout logged successfully!")
            else:
                st.error("Failed to log workout.")

# Page for business insights
elif page == "Business Insights":
    st.header("📊 Application Insights")
    insights = db.get_business_insights()
    if insights:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Workouts", f"{insights['total_workouts']:,}")
            st.metric("Avg Duration", f"{insights['avg_workout_duration']:.2f} min")
        with col2:
            st.metric("Total Weight Lifted", f"{insights['total_weight_lifted']:,} kg")
        with col3:
            st.metric("Max Weight Lifted", f"{insights['max_weight_lifted_single_exercise']:,} kg")
            st.metric("Min Reps per Exercise", f"{insights['min_reps_per_exercise']}")
    else:
        st.warning("No data available for insights.")