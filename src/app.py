from flask import Flask
from flask_mako import MakoTemplates, render_template
from plim import preprocessor

app = Flask(__name__)
mako = MakoTemplates(app)
app.config['MAKO_PREPROCESSOR'] = preprocessor

@app.route('/')
def hello():
    return render_template('index.html', name='mako')

if __name__ == "__main__":
    app.run(debug=True)