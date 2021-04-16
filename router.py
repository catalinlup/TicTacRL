from flask import Flask, render_template

app = Flask(__name__, static_folder='frontend/tictacrl/build/static', template_folder='frontend/tictacrl/build')




@app.route('/')
def mainPage():
  return render_template('index.html')

app.run(debug=True, port=8080)
