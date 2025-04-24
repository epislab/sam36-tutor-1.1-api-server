from flask import Flask, render_template, request, redirect, url_for
from com.epislab.models.titanic.titanic_controller import TitanicController

app = Flask(__name__)
@app.route('/')
def intro():
    controller = TitanicController()
    controller.modeling('train.csv', 'test.csv')
    return render_template("/index.html")

@app.route('/titanic')
def titanic2():

    return render_template("/titanic.html")


if __name__ == '__main__':
   app.run(debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True