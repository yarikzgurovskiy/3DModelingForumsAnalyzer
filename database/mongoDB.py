from bson import ObjectId
from pymongo import MongoClient

from database.message import Message
from database.topic import Topic


class Database:
    def __init__(self, uri="mongodb://localhost:27017/"):
        self.__client = MongoClient(uri)
        self.__db = self.__client["admin"]
        self.__messages_coll = self.__db.messages
        self.__topics_coll = self.__db.topics

    def select_database(self, database: str):
        self.__db = self.__client[database]
        self.__messages_coll = self.__db.messages
        self.__topics_coll = self.__db.topics

    def save_message(self, message: Message):
        self.__messages_coll.save(message.__dict__)

    def save_topic(self, topic: Topic):
        self.__topics_coll.save(topic.__dict__)

    def get_topics(self) -> list:
        return self.__topics_coll.find()

    def get_messages_counter_by_topic(self, topic_id: str) -> dict:
        messages = list(self.__messages_coll.find({"topic_id": ObjectId(topic_id)}))
        dictionary = dict.fromkeys([message["author"] for message in messages], 0)
        for message in messages:
            dictionary[message["author"]] += 1
        return dictionary
