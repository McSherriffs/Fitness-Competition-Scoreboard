from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Team, Exercise, User, Round
from flask_login import login_user, logout_user, login_required, current_user
from forms import ScoreInputForm, LoginForm
from flask_socketio import SocketIO

# Initialize the Flask app
app = Flask(__name__)

# Set the database URI and secret key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness_competition.db'
app.config['SECRET_KEY'] = 'your-secret-key'  #TODO Replace with your actual secret key

# Initialize the database and SocketIO (for real-time updates)
db.init_app(app)
socketio = SocketIO(app)


# Home route for the landing page
@app.route('/')
def home():
    return render_template('index.html')  # Render the homepage


# Login route for user authentication
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Initialize login form
    if form.validate_on_submit():  # If form is submitted and valid
        # Check if the user exists and the password is correct
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)  # Log the user in
            return redirect(url_for('dashboard'))  # Redirect to the dashboard
        else:
            flash('Invalid credentials')  # Show error if credentials are invalid
    return render_template('login.html', form=form)  # Render login page


# Restricted dashboard for coaches/admins
@login_required  # Only logged-in users can access this route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')  # Render the dashboard


# Scoreboard route to display current standings
@login_required
@app.route('/scoreboard')
def scoreboard():
    teams = Team.query.all()  # Query all teams from the database
    return render_template('scoreboard.html', teams=teams)  # Render the scoreboard


# Route to input scores (accessible to coaches and admins only)
@login_required
@app.route('/input_scores', methods=['GET', 'POST'])
def input_scores():
    # Restrict access to only coaches and admins
    if current_user.role not in ['coach', 'admin']:
        return redirect(url_for('scoreboard'))  # Redirect non-authorized users to scoreboard

    form = ScoreInputForm()  # Initialize score input form
    if form.validate_on_submit():  # If form is submitted and valid
        team = Team.query.get(form.team_id.data)  # Get the selected team
        round_id = form.round_id.data  # Get the selected round
        team.round_scores[round_id] = form.scores.data  # Store the scores for the team and round
        db.session.commit()  # Save changes to the database

        # Emit a socket.io event to notify all clients to refresh the scoreboard
        socketio.emit('update_scoreboard')
        return redirect(url_for('scoreboard'))  # Redirect back to the scoreboard

    return render_template('input_scores.html', form=form)  # Render the score input form


# Websocket handler for real-time updates to the scoreboard
@socketio.on('connect')
def handle_connect():
    pass  # Placeholder for any logic when a user connects via WebSocket


# Main entry point to run the Flask app with SocketIO
if __name__ == "__main__":
    socketio.run(app)  # Run the Flask-SocketIO server
