from flask import Flask, render_template, request
from forum_grabber.forum_grabber.database.mongoDB import Database
from subprocess import call
import os

db = Database()
app = Flask(__name__)
os.chdir('forum_grabber')
call(['scrapy', 'crawl', 'topics'])
call(['scrapy', 'crawl', 'messages'])


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        call(['scrapy', 'crawl', 'topics'])
    return render_template('home.html', topics=db.get_topics())


@app.route('/topics/<topic_id>', methods=['GET', 'POST'])
def topic(topic_id):
    if request.method == 'POST':
        call(['scrapy', 'crawl', 'messages'])
    author_mess_amount = db.get_messages_counter_by_topic_id(topic_id)
    topic_url = db.get_topic_by_id(topic_id)['url']
    key_with_max_value = max(author_mess_amount.keys(), key=(lambda k: author_mess_amount[k]))
    max_amount = author_mess_amount[key_with_max_value]
    return render_template('topic.html',
                           author_mess_amount=author_mess_amount, max_amount=max_amount,
                           topic_url=topic_url)


if __name__ == '__main__':
    app.run(port=3000)
