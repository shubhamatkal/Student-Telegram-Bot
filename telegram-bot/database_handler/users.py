import pymongo
from datetime import datetime

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class MongoDBHandler:
    def __init__(self, connection_string, database_name, collection_name):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
        print("connection successful for db")

    def add_chat_id(self, chat_id):
        user_data = {
            chat_id: {
                "subjects": [],
                "last_login":current_datetime   # Set the last login to the current time
            }
        }
        self.collection.insert_one(user_data)
        print(f"chat_id '{chat_id}' added.")

    def add_subjects_to_user(self, chat_id, subjects):
        user = self.collection.find_one({chat_id: {"$exists": True}})
        if user:
            existing_subjects = user[chat_id].get("subjects", [])
            updated_subjects = existing_subjects + subjects
            self.collection.update_one({chat_id: {"$exists": True}}, {"$set": {f"{chat_id}.subjects": updated_subjects}})
            print(f"Subjects added for user: {chat_id}")
        else:
            print(f"User '{chat_id}' does not exist in the database.")

    def user_exists(self, chat_id):
        user = self.collection.find_one({chat_id: {"$exists": True}})
        return user is not None

    def add_new_subkey_to_all_users(self, new_subkey, default_value):
        self.collection.update_many({}, {"$set": {f"$[user].{new_subkey}": default_value}}, array_filters=[{"user": {"$exists": True}}])
        print(f"Added new subkey '{new_subkey}' to all users.")

    def close_connection(self):
        self.client.close()
        print("connection closed with database")

