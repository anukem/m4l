from flask import Flask, request
from flask_mako import MakoTemplates, render_template
from plim import preprocessor
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    location_to_meet = SelectField("Location To Meet? ", choices=[("Somewhere", "Somewhere")], validators=[DataRequired()])
    location_to_eat = SelectField("Location to Eat? ", choices=[("Somewhere", "Somewhere")],validators=[DataRequired()])
    time = SelectField("Time? ", validators=[DataRequired()])
    submit = SubmitField("Lets Eat!")

app = Flask(__name__)
mako = MakoTemplates(app)
app.config['MAKO_PREPROCESSOR'] = preprocessor
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/', methods=["GET", "POST"])
def hello():
    form = LoginForm()
    form.time.choices = [(str(n % 12 + 1) + ":00PM",str(n %12 + 1) + ":00PM") for n in range(11,17)] + [(str(n % 12 + 1) + ":30PM" ,str(n % 12 + 1) + ":30PM" ) for n in range(11, 17)]
    form.time.choices.sort()
    if request.method == "POST":
        print(request.form)
        return "Hello World!"
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)