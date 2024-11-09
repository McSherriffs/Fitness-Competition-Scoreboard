# Fitness Competition Scoreboard

A real-time scoreboard application for fitness competitions, built using Python, Flask, and Socket.IO. This app allows coaches to input exercise scores for their teams, which are then dynamically updated on a scoreboard viewable by all participants.

## Main Components
Database Model:

Team: id, name, athletes (3-4), round_scores (list of scores), total_score, rank.
Exercise: id, name, type, team_id, round_id, score.
User: id, username, role (admin/coach/athlete), password.
Round: id, round_number, date.
Backend Logic:

Teams will be able to submit their scores per round for different exercises.
An admin or coach will input the scores; the results will be calculated automatically (using predefined rules) and stored.
The system will calculate total team scores and ranks after each round.
A scoreboard will refresh every 15-30 seconds dynamically.
Roles & Permissions:

Admin: Can access all pages (input, view scoreboards, modify data).
Coach: Can only input team scores but can't modify other parts of the system.
Athlete: Can view scoreboards but can't input or modify anything.
Pages:

Login Page: User authentication.
Input Results Page (restricted to coaches and admin).
Scoreboard Page: Displays results for all teams, refreshing periodically.
Team Rank Page: Displays teams ranked by score.
Admin Dashboard: Overview and administrative control for data.


## Features

- Manage teams and athletes for a competition.
- Input exercise results by coaches, and automatically calculate team scores.
- Real-time scoreboard refresh every 15-30 seconds using Flask-SocketIO.
- User roles: Admin, Coach, Athlete with different access controls.
- Responsive UI for mobile, tablet, and desktop views.

## Tech Stack

- Python (Flask)
- Flask-SocketIO (for real-time updates)
- SQLAlchemy (ORM for database management)
- SQLite (Database, easy to switch to PostgreSQL or MySQL)
- HTML/CSS/JavaScript (Frontend)
- Bootstrap (for responsive UI)
- Flask-Login (for user authentication)
  
## Setup Instructions

### Prerequisites
1. Python 3.x installed.
2. Git installed.

### Local Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/fitness-competition-scoreboard.git
   cd fitness-competition-scoreboard

2. Navigate into the project directory:
bash
cd yourproject

3. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install the dependencies:
pip install -r requirements.txt

5.Run the app: 
flask run

The app will now be running at http://localhost:5000/.

## Running Tests
To run tests, use:
python -m unittest discover -s tests

## Usage
Admin Access: Allows full control over teams, users, and scores.
Coach Access: Can input scores but cannot modify teams or view sensitive data.
Athlete Access: Can only view the scoreboard.

Coaches can input team results via the input page.
The scoreboard updates every 15-30 seconds.
Athletes can view the scoreboard but cannot edit the results.

## Deployment
 - Deploy to Heroku (or another platform):

 - Ensure you have a Procfile for Heroku:
bash
web: gunicorn app:app

- Add requirements.txt and runtime.txt (for Python version).

- Use a database service like Postgres for production.


## Contributing
To contribute:

1. Fork the repository.
  
2. Create a new branch:
bash
git checkout -b feature-branch-name

3. Make your changes.

4. Push to your branch:
git push origin feature-branch-name

5. Submit a pull request with a description of your changes.
