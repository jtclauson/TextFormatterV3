from flask import render_template, redirect, url_for, request, session
from app import app
from app.scripts.format import Format

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form["text"]
        filename = request.form["filename"]
        origin = request.form["origin"]
        formatted = Format(text, filename, origin)
        if(formatted['error']):
            session['error'] = formatted['error']
            return redirect(url_for('error'))

        session['formatted'] = formatted
        return redirect(url_for('formatted'))
    return render_template('index.html')

@app.route("/formatted", methods=['GET', 'POST'])
def formatted():
    formatted = session['formatted']
    return render_template('formatted.html', formatted=formatted)

@app.route("/error", methods=['GET', 'POST'])
def error():
    error = session['error']
    session.pop('error', None)
    return render_template('error.html', error=error)
