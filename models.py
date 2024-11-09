from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

# Initialize the SQLAlchemy object (handles database operations)
db = SQLAlchemy()

# User model for authentication and roles
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    username = db.Column(db.String(150), unique=True, nullable=False)  # Username, must be unique
    password = db.Column(db.String(150), nullable=False)  # Password for login
    role = db.Column(db.String(50))  # Role can be 'admin', 'coach', or 'athlete'

# Team model to store team details
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each team
    name = db.Column(db.String(100), nullable=False)  # Team name
    athletes = db.Column(db.JSON, nullable=False)  # List of athlete names, stored as JSON
    round_scores = db.Column(db.JSON, nullable=True)  # Scores for each round, stored as JSON
    total_score = db.Column(db.Integer, default=0)  # Sum of all rounds' scores for the team
    rank = db.Column(db.Integer, nullable=True)  # Current rank of the team, based on total_score

# Exercise model to store individual exercise results for each team and round
class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each exercise
    name = db.Column(db.String(100), nullable=False)  # Exercise name (e.g., Push-up, Squat)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)  # Foreign key linking to a team
    round_id = db.Column(db.Integer, nullable=False)  # The round in which this exercise occurs
    score = db.Column(db.Integer, nullable=False)  # The score achieved for this exercise

# Round model to track different rounds in the competition
class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each round
    round_number = db.Column(db.Integer, nullable=False)  # The number of the round
    date = db.Column(db.DateTime, nullable=False)  # The date/time of the round
