from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def template_test():
    return render_template('home.html',
                           themes=[{"theme": "machine learning"}, {"theme": "kek"}, {"theme": "lol"}])


@app.route('/<code>')
def template_test2(code):
    authors = [{"author": "Yarik", "messagesAmount": 1}, {"author": "Max", "messagesAmount": 6},
               {"author": "Andrian", "messagesAmount": 4}, {"author": "Vadem", "messagesAmount": 8}]
    return render_template('forum.html', authors=authors)


if __name__ == '__main__':
    app.run(port=3000)
