from flask import Flask, request
from flask_mako import MakoTemplates, render_template
from plim import preprocessor

app = Flask(__name__)
mako = MakoTemplates(app)
app.config['MAKO_PREPROCESSOR'] = preprocessor

@app.route('/', methods=["GET", "POST"])
def hello():
	if request.method == "POST":
		print(1)
		return "Hello World!"
    return render_template('index.html', name='mako')

if __name__ == "__main__":
    app.run(debug=True)