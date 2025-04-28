import random
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'any-secret-key'

eras = [
    "Ancient-Egypt",
    "Medival Europe",
    "Industrial Revolution",
    "World War Era",
    "Modern Day",
    "Distant Future",
    "Alien World"
]




@app.route('/')
def home():
    # return "👋 Hello, Time Traveler!"
    return render_template("home.html")

@app.route("/play", methods=['GET','POST'])
def play():
    if request.method == 'GET' or 'choice' not in request.form:
        session['step'] = 0
    else:
        choice = request.form['choice']
        correct = random.choice(['left', 'right'])
        
        if choice == correct:
            session['step'] = session.get('step', 0) + 1
            if session['step'] >= len(eras):
                return redirect(url_for('victory'))
        else:
            return redirect(url_for('gameover'))
    
    
    current_era = eras[session['step']]
    return render_template('era.html', era = current_era)    

@app.route('/victory')
def victor():
    return render_template('victory.html')



@app.route('/gameover')
def gameover():
    return render_template('gameover.html')


if __name__ == '__main__':
    app.run(debug=True)
    
    # return "🌟 The adventure begins!"
    
    