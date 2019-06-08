from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'baab100b5828f75fe53b346b43de8316'

posts = [
    {
        'user': 'Joel Olivero',
        'email': 'joelolivero@outlook.com',
        'birthday': '02/25/1991',
        'title': 'Beginner',
        'content': 'First post, How is everyone doing?',
        'date_posted': 'april 10, 2019'
    },
    {
        'user': 'Bella Koudriavsteva',
        'email': 'bellybean92@yahoo.com',
        'birthday': '07/26/1992',
        'title': 'Morning',
        'content': 'Good Morning',
        'date_posted': 'April 27, 2019',
    }
]


@app.route("/")
@app.route("/home")
def facebook():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('login.html', posts=posts)


@app.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.user.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('registration.html', title='Registration', form=form)


@app.route("/reset")
def email():
    form = LoginForm
    return render_template('reset.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
