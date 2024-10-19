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

