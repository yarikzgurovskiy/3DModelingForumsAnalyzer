from flask import Flask, render_template
from database.mongoDB import Database

db = Database()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', topics=db.get_topics())


@app.route('/topics/<topic_id>')
def topic(topic_id):
    author_mess_amount = db.get_messages_counter_by_topic(topic_id)
    max_amount = get_max_value(author_mess_amount)
    return render_template('topic.html', author_mess_amount=author_mess_amount, max_amount=max_amount)


def get_max_value(dictionary: dict):
    max_amount = 0
    for value in dictionary.values():
        if value > max_amount:
            max_amount = value
    return max_amount


if __name__ == '__main__':
    app.run(port=3000)
