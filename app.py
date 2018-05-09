from flask import Flask, render_template, Response, request
from forum_grabber.forum_grabber.database.mongoDB import Database
from forum_grabber.scraper import Scraper

scraper = Scraper()
db = Database()
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        scraper.scrap_topics()
        scraper.run()
    return render_template('home.html', topics=db.get_topics(), update='topics')


@app.route('/topics/<topic_id>', methods=['GET', 'POST'])
def topic(topic_id):
    if request.method == 'POST':
        scraper.scrap_messages()
        scraper.run()
    author_mess_amount = db.get_messages_counter_by_topic_id(topic_id)
    topic_url = db.get_topic_by_id(topic_id)['url']
    key_with_max_value = max(author_mess_amount.keys(), key=(lambda k: author_mess_amount[k]))
    max_amount = author_mess_amount[key_with_max_value]
    return render_template('topic.html',
                           author_mess_amount=author_mess_amount, max_amount=max_amount,
                           topic_url=topic_url, update='messages')


@app.route('/update', methods=['POST'])
def update():
    print()
    return Response('Updated successfully', status=200)


if __name__ == '__main__':
    app.run(port=3000)
