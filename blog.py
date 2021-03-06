from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Stone John',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 22, 2018'
    },
    {
        'author': 'Anderson Eugenia',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 23, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pst=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
