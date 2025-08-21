# Fitness-Tracker
FitFriends Fitness Tracker 🏋️‍♀️
Welcome to the FitFriends Fitness Tracker, a personal application designed to help individuals log their fitness activities, set personal goals, and share progress with a small group of friends. This project is built using Python, with a clear separation of concerns between the frontend and backend to ensure a modular and maintainable codebase.

🚀 Key Features
User Profiles: Manage your personal information, including name, email, and weight.

Workout & Progress Tracking: Log new workouts with details like duration and a list of exercises (reps, sets, weight). View a history of your workouts to track progress over time.

Social Connections: Connect with friends to create a social network within the app.

Dynamic Leaderboard: A key feature that ranks friends based on selected metrics, such as total workout minutes for the week.

Goal Setting: Set personal fitness goals and track your progress toward achieving them.

Business Insights Dashboard: Provides an overview of fitness data using aggregate functions like COUNT, SUM, AVG, MIN, and MAX.

🛠️ Technical Stack
Frontend: Streamlit

Backend: Python

Database: PostgreSQL

Database Connector: psycopg2

📂 File Structure
The application is structured into two main files, adhering to the principle of separation of concerns:

backend.py: This file contains all the business logic and database interaction functions. It handles all Create, Read, Update, and Delete (CRUD) operations.

frontend.py: This is the user interface of the application, built with Streamlit. It calls the functions in backend.py to retrieve and store data based on user actions.

⚙️ How to Set Up and Run
Clone the repository:

Bash

git clone https://github.com/your-username/your-repository.git
cd your-repository
Set up the PostgreSQL database:

Ensure PostgreSQL is installed and running.

Create a new database for the application (e.g., fitfriends_db).

Execute the SQL schema from the project to create all necessary tables (users, friends, workouts, exercises, goals).

Install dependencies:

It's recommended to use a virtual environment.

Install the required Python packages:

Bash

pip install streamlit psycopg2-binary
Configure your environment variables:

Create a .env file in the root directory of the project.

Add your database credentials to this file:

Code snippet

DB_NAME=fitfriends_db
DB_USER=your_username
DB_PASS=your_password
DB_HOST=localhost
Run the application:

Navigate to the project's root directory in your terminal and run the Streamlit app:

Bash

streamlit run frontend.py
The application will automatically open in your web browser, and you can begin tracking your fitness journey.
