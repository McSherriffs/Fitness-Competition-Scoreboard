# Fitness Competition Scoreboard

A real-time scoreboard application for fitness competitions, built using Python, Flask, and Socket.IO. This app allows coaches to input exercise scores for their teams, which are then dynamically updated on a scoreboard viewable by all participants.

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

### Usage
Coaches can input team results via the input page.
The scoreboard updates every 15-30 seconds.
Athletes can view the scoreboard but cannot edit the results.

### Contributing
To contribute:

1. Fork the repository.
  
2. Create a new branch:
bash
git checkout -b feature-branch-name

3. Make your changes.

4. Push to your branch:
git push origin feature-branch-name

5. Submit a pull request with a description of your changes.
