from flask import Flask, render_template
from forum_grabber.forum_grabber.database.mongoDB import Database
from forum_grabber.scraper import Scraper

scraper = Scraper()
scraper.scrap_topics()
scraper.scrap_messages()
scraper.run()

db = Database()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html',
                           topics=db.get_topics())


@app.route('/topics/<topic_id>')
def topic(topic_id):
    author_mess_amount = db.get_messages_counter_by_topic_url(topic_id)
    max_amount = max(author_mess_amount.values())
    return render_template('topic.html',
                           author_mess_amount=author_mess_amount,
                           max_amount=max_amount)


if __name__ == '__main__':
    app.run(port=3000)
