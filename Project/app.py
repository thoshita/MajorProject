from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/facultyHome')
def faculty():
    return render_template('facultyHome.html')

@app.route('/facultyOngoing')
def facultyOngoing():
    return render_template('facultyOngoing.html')

@app.route('/studentHome')
def studentHome():
    return render_template('studentHome.html')

@app.route('/studentWork')
def studentWork():
    return render_template('studentWork.html')
    
@app.route('/studentPerformance')
def studentPerformance():
    return render_template('studentPerformance.html')
if __name__ == '__main__':
    app.run(DEBUG=True)
