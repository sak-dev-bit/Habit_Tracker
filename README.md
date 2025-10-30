 Habit Tracker App

## 🎯 Project Goal

The Habit Tracker is a web application designed to help users build and maintain positive habits by providing a simple interface to track daily completions, measure streak duration, and visualize progress.

## ✨ Key Features

  * **Create Habits:** Easily add new habits (e.g., "Drink Water," "Read 30 mins," "Exercise").
  * **Daily Completion:** A one-click action to mark a habit as complete for the day.
  * **Streak System:** Automatically calculates and updates the current consecutive completion streak.
  * **Automated Reset:** An integrated system that automatically resets a streak to $0$ if a day is missed.
  * **Progress Visualization:** Uses a **Bootstrap progress bar** to show progress towards a goal (e.g., a 30-day streak).
  * **Leaderboard:** Displays habits ranked by the longest current streak.

## 🛠️ Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend** | **Django** (Python) | Core application logic, routing, and database ORM. |
| **Database** | SQLite (Default) | Simple, file-based database for development. |
| **Frontend** | HTML, CSS, JavaScript | Structure and styling. |
| **Styling** | Custom CSS & Basic HTML | Simple, clean interface for focus on functionality. |
| **Scheduling** | **Django Management Commands** & **System Cron** | Handling daily streak checks and resets. |

## ⚙️ Local Setup and Installation

Follow these steps to get a development copy of the project running on your local machine.

### 1\. Prerequisites

You must have **Python 3.8+** and **pip** installed.

### 2\. Clone the Repository

```bash
git clone <your_repository_url>
cd habit-tracker-app
```

### 3\. Create and Activate Virtual Environment

It's highly recommended to use a virtual environment.

```bash
# Create the environment
python -m venv venv

# Activate the environment (on Linux/macOS)
source venv/bin/activate

# Activate the environment (on Windows)
.\venv\Scripts\activate
```

### 4\. Install Dependencies

Install all required packages (Django, etc.).

```bash
pip install -r requirements.txt
```

### 5\. Database Migration

Apply the initial migrations to create the database schema.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6\. Run the Development Server

Start the application\!

```bash
python manage.py runserver
```

The application will now be accessible at `http://127.0.0.1:8000/`.

-----

## 🧠 Core System Logic

The **streak reset** is handled by a background process that checks the completion date of every habit.

### **Daily Streak Reset Command**

To manage streaks, a custom Django Management Command must be run daily.

1.  **Run the Command Manually (Testing):**

    ```bash
    python manage.py check_streaks
    ```

2.  **Deployment (Production):**
    This command is designed to be scheduled using a **system-level Cron Job** to ensure it runs automatically every day, typically just after midnight (e.g., 1:00 AM local time).

    The command checks the `last_completed` date: if it is older than yesterday's date, the `current_streak` is reset to $0$.

-----

## ⬆️ Future Enhancements

  * **User Authentication:** Allow multiple users to have separate habit lists (currently single-user focused).
  * **Habit Editing/Deletion:** Add CRUD functionality beyond just creating habits.
  * **Goal Setting:** Allow users to define a specific streak goal (e.g., "30 days") and calculate progress relative to that goal.
  * **Notifications:** Implement email or in-app notifications for missed days or streak milestones.
  * **Advanced Visualization:** Use a JavaScript charting library (like Chart.js) to show completion history on a calendar.
