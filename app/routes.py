from flask import render_template, redirect, url_for, request, session
from app import app
from format import Format
from format import Formatted

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        # text = request.form["text"]
        # input = request.form
        # formatted = Format(input)
        testvar = "pancakes"
        session['testvar'] = testvar
        return redirect(url_for('formatted'))
        # return redirect(url_for('formatted', text=text))
    return render_template('index.html')

@app.route("/formatted", methods=['GET', 'POST'])
# @app.route('/formatted')
def formatted(testvar="default"):
    # testvar = request.args.get('testvar')
    testvar = session['testvar']
    # testvar="jam"
    # text = request.form.get('text')
    # input = request.form.get('formatted')
    return render_template('formatted.html', testvar=testvar)
    # return 'welcome %s' % testvar
    # return render_template('formatted.html')
    # return render_template('formatted.html', text=text)