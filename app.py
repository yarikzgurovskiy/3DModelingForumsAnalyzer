from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html',
                           topics=[{"name": "machine learning", "_id": "asd"},
                                   {"name": "kek", "_id": "123"}, {"name": "lol", "_id": "qwerty"}])


@app.route('/<id>')
def forum(id):
    author_mess_amount = {"Yarik": 1, "Max": 6, "Andrian": 5, "Vadem": 8}
    max_amount = 0
    for value in author_mess_amount.values():
        if value > max_amount:
            max_amount = value
    return render_template('forum.html', author_mess_amount=author_mess_amount, max_amount=max_amount)


if __name__ == '__main__':
    app.run(port=3000)
