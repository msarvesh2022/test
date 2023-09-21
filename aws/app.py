from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/profile')

def profile():
    return "This Is Profile Page"


@app.route('/success/<int:score>')

def show(score):
    if score >33:
        return "Passed"
    else:
        return "Fail"

if __name__=="__main__":
    app.run(debug=True)