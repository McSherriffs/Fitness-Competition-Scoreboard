#  This is the core of the Flask application, where you’ll define routes for each page and logic for handling data.

from flask import Flask, render_template, request, redirect, url_for

#Initialise Flask app
app = Flask(__name__)

# Sample data structure to hold team information
# Each team has a name and a score, starting at 0
teams = [
    {"name": "Team A", "score": 0},
    {"name": "Team B", "score": 0},
    {"name": "Team C", "score": 0},
]

# Route for the main scoreboard
@app.route('/')
def index():
    # Render the index.html template and pdd the team data
    return render_template('index.html', teams=teams)

# Route for the input results page (for coaches top enter the scores)
@app.route('/input-scores', methods=['GET', 'POST'])
def input_results():
    if request.method == 'POST':
        # Retrieve data from the form submission
        team_name = request.form.get("team_name")
        score = int(request.form.get("score"))

        # Update the score for the specified team
        for team in teams:
            if team['name'] == team_name:
                team['score'] += score

       # Redirect back to the main scoreboard page after updating the score
        return redirect(url_for('index'))

    # Render the input_scores.html template, passing the teams list
    return render_template('input_scores.html', teams=teams)






