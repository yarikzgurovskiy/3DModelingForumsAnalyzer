from bson import ObjectId
from pymongo import MongoClient


class Database:
    def __init__(self, to_clear=False, uri="mongodb://localhost:27017/"):
        self.__client = MongoClient(uri)
        self.__db = self.__client["forum_analyzer"]
        self.__messages_coll = self.__db.messages
        self.__topics_coll = self.__db.topics
        if to_clear:
            self.clear_database()

    def __del__(self):
        self.close()

    def select_database(self, database: str):
        self.__db = self.__client[database]
        self.__messages_coll = self.__db.messages
        self.__topics_coll = self.__db.topics

    def save_message(self, message: dict):
        if len(message["text"]) > 0 and self.__messages_coll.find_one(message) is None:
            self.__messages_coll.save(message)

    def save_topic(self, topic: dict):
        if self.__topics_coll.find_one(topic) is None:
            self.__topics_coll.save(topic)

    def get_topics(self) -> list:
        return list(self.__topics_coll.find())

    def get_topic_by_id(self, topic_id) -> dict:
        return self.__topics_coll.find_one({"_id": ObjectId(topic_id)})

    def get_messages_counter_by_topic_id(self, topic_id: str) -> dict:
        topic = self.get_topic_by_id(topic_id)
        messages = list(self.__messages_coll.find({"topic_url": topic["url"]}))
        author_mess_amount = dict.fromkeys([message["author"] for message in messages], 0)
        for message in messages:
            author_mess_amount[message["author"]] += 1
        return author_mess_amount

    def clear_database(self):
        self.__messages_coll.remove()
        self.__topics_coll.remove()

    def close(self):
        self.__client.close()
