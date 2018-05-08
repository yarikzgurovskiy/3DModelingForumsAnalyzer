from pymongo import MongoClient


class Database:
    def __init__(self, to_clear=False, uri="mongodb://localhost:27017/"):
        self.__client = MongoClient(uri)
        self.__db = self.__client["admin"]
        self.__messages_coll = self.__db.messages
        self.__topics_coll = self.__db.topics
        if to_clear:
            self.clear_database()

    def select_database(self, database: str):
        self.__db = self.__client[database]
        self.__messages_coll = self.__db.messages
        self.__topics_coll = self.__db.topics

    def save_message(self, message: dict):
        if self.__messages_coll.find_one(message) is None:
            self.__messages_coll.save(message)

    def save_topic(self, topic: dict):
        if self.__topics_coll.find_one(topic) is None:
            self.__topics_coll.save(topic)

    def get_topics(self) -> list:
        return list(self.__topics_coll.find())

    def get_messages_counter_by_topic_url(self, topic_url: str) -> dict:
        messages = list(self.__messages_coll.find({"topic_url": topic_url}))
        print(len(messages))
        author_mess_amount = dict.fromkeys([message["author"] for message in messages], 0)
        for message in messages:
            author_mess_amount[message["author"]] += 1
        return author_mess_amount

    def clear_database(self):
        self.__messages_coll.remove()
        self.__topics_coll.remove()

    def close(self):
        self.__client.close()

#
# db = Database()
# db.save_message({"text": "2", "author": "2", "date": "3", "topic_url": "4"})
# db.save_topic(Topic("1", "11"))
# db.save_topic(Topic("2", "11"))
# db.save_topic(Topic("3", "11"))
# db.save_topic(Topic("4", "11"))
# db.save_topic(Topic("5", "11"))
# db.save_topic(Topic("6", "11"))
# db.save_topic(Topic("7", "11"))
# db.save_topic(Topic("8", "11"))
# print(db.get_messages_counter_by_topic_url("http://polycount.com/discussion/200381/choosing-gift-for-3d-artist"))
