from flask import Flask, render_template
from com.epislab.models.crime_controller import CrimeController
app = Flask(__name__)
@app.route('/')
def index():
    crime_controller = CrimeController()
    crime_controller.modeling('cctv_in_seoul.csv', 'crime_in_seoul.csv', 'pop_in_seoul.xls')
    return render_template('index.html')