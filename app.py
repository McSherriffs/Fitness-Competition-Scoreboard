from flask import Flask, render_template, request, redirect
import sqlite3

#Initialise Flask app
app = Flask(_name_)

# Function to initialise the database (this should only run when the app starts)
def init_db():
    """
    This function sets up the SQLite database if it doesn't already exist.
    It creates a table to store participant names and their scores.
    """
    conn = sqlite3.connect('database.bd') #connect to the database file
    c = conn.cursor() #cursor allows us to execute SQL commands
    c.execute('''
        CREATE TABLE IF NOT EXISTS participants(
            id INTEGER PRIMARY KEY AUTOINCREMENT,    # Unique ID for each participant
            name TEXT NOT NULL,                      # Participants name
            score INTEGER NOT NULL DEFAULT 0         # Initial score (defaults to 0)
            )
    ''')
    conn.commit()   # Saves changes
    conn.close()    # Close the connection


# Route for the main page
@app.route('/')
def index():
    """
    This is the main page of the app. It fetched all the participants form the database
    and displays them in descending order of their scores.
    """
    conn = sqlite3.connect('database.db')   # Connect to the database
    c = conn.cursor()
    c.execute('SELECT * FROM participants ORDER BY score DESC')     # Fetchs all the participants
    participants = c.fetchall() # fetches the results
    conn.close()    # closing the databas connection
    return render_template('index.html', participants=participants)

# Route to add a new participant
@app.route('/add', methods=['POST'])
def add_participant():
    """
    This handles the addition of new participants to the database.
    It expects the participants name and initial scores from a form submission.
    """
    name = request.form['name'] # Get name from the form
    score = int(request.form['score']) # Get the score from the form
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO participants (name, score) VALUES (?, ?)', (name, score))
    conn.commit()
    conn.close()
    return redirect('/')    #redirect back to the main page

# Route to update an existing participant's score
@app.route('/update', methods=['POST'])
def update_score():
    """
    This will update the score of an existing participant in the database.
    It expects participant IF and a new score from a form submission
    """
