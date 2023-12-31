import pymongo
from datetime import datetime

current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class UsersDBHandler:
    def __init__(self, connection_string, database_name, collection_name):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
        print("connection successful for db")

    def add_chat_id(self, chat_id):
        user_data = {
            chat_id: {
                "subjects": [],
                "last_login": current_datetime   # Set the last login to the current time
            }
        }
        self.collection.insert_one(user_data)
        print(f"chat_id '{chat_id}' added.")

    def add_subjects_to_user(self, chat_id, subjects):
        user = self.collection.find_one({chat_id: {"$exists": True}})
        if user:
            existing_subjects = user[chat_id].get("subjects", [])
            updated_subjects = existing_subjects + subjects
            self.collection.update_one({chat_id: {"$exists": True}}, {
                                       "$set": {f"{chat_id}.subjects": updated_subjects}})
            print(f"Subjects added for user: {chat_id}")
        else:
            print(f"User '{chat_id}' does not exist in the database.")

    def user_exists(self, chat_id):
        user = self.collection.find_one({chat_id: {"$exists": True}})
        return user is not None

    def add_new_subkey_to_all_users(self, new_subkey, default_value):
        self.collection.update_many({},
                                    {"$set": {f"$[user].{new_subkey}": default_value}},
                                    array_filters=[{"user": {"$exists": True}}])
        print(f"Added new subkey '{new_subkey}' to all users.")

    def close_connection(self):
        self.client.close()
        print("connection closed with database")


# class for notes


class MongoDBNotes:
    def __init__(self, connection_string, database_name, collection_name):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
        print("Connection successful for DB")

    def add_subject(self, subject_name):
        if not self.collection.find_one({'subject': subject_name}):
            self.collection.insert_one({'subject': subject_name, 'notes': []})
            print(f"Subject '{subject_name}' added.")

    def add_note(self, subject_name, note_name, note_link, tag_name=None):
        subject = self.collection.find_one({'subject': subject_name})
        if subject:
            notes = subject['notes']
            for note in notes:
                if note['name'] == note_name:
                    print(
                        f"Note '{note_name}' already exists in '{subject_name}'")
                    return
            if tag_name:
                notes.append(
                    {'name': note_name, 'link': note_link, 'tags': [tag_name]})
            else:
                notes.append({'name': note_name, 'link': note_link})
            self.collection.update_one({'subject': subject_name}, {
                                       '$set': {'notes': notes}})
            if tag_name:
                print(
                    f"Note '{note_name}' added to '{subject_name}' with tag '{tag_name}'.")
            else:
                print(f"Note '{note_name}' added to '{subject_name}'.")

    def add_tag_to_note(self, subject_name, note_name, tag_name):
        subject = self.collection.find_one({'subject': subject_name})
        if subject:
            notes = subject['notes']
            for note in notes:
                if note['name'] == note_name:
                    note_tags = note.get('tags', [])
                    if tag_name not in note_tags:
                        note_tags.append(tag_name)
                        note['tags'] = note_tags
                        self.collection.update_one({'subject': subject_name}, {
                                                   '$set': {'notes': notes}})
                        print(
                            f"Tag '{tag_name}' added to note '{note_name}' in '{subject_name}'.")
                        return
                    else:
                        print(
                            f"Tag '{tag_name}' already exists for note '{note_name}' in '{subject_name}'.")
                        return
            print(f"Note '{note_name}' not found in '{subject_name}'.")
        else:
            print(f"Subject '{subject_name}' not found.")


# class for PYQ
class MongoDBPYQ:
    def __init__(self, connection_string, database_name, collection_name):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]
        print("Connection successful for DB")

    def add_subject(self, subject_name):
        if not self.collection.find_one({'subject': subject_name}):
            self.collection.insert_one({'subject': subject_name, 'pyq': []})
            print(f"Subject '{subject_name}' added.")

    def add_pyq(self, subject_name, pyq_name, pyq_link, tag_name=None):
        subject = self.collection.find_one({'subject': subject_name})
        if subject:
            pyq = subject['pyq']
            for py in pyq:
                if py['name'] == pyq_name:
                    print(
                        f"pyq '{pyq_name}' already exists in '{subject_name}'")
                    return
            pyq.append(
                {'name': pyq_name, 'link': pyq_link, 'tags': [tag_name]})
            self.collection.update_one({'subject': subject_name}, {
                                       '$set': {'pyq': pyq}})
            print(
                f"pyq '{pyq_name}' added to '{subject_name}' with tag '{tag_name}'.")
        else:
            print("Subject is not present , kindly add the subject first")

    def add_tag_to_pyq(self, subject_name, pyq_name, tag_name):
        subject = self.collection.find_one({'subject': subject_name})
        if subject:
            pyqs = subject['pyqs']
            for pyq in pyqs:
                if pyq['name'] == pyq_name:
                    pyq_tags = pyq.get('tags', [])
                    if tag_name not in pyq_tags:
                        pyq_tags.append(tag_name)
                        pyq['tags'] = pyq_tags
                        self.collection.update_one({'subject': subject_name}, {
                                                   '$set': {'pyqs': pyqs}})
                        print(
                            f"Tag '{tag_name}' added to pyq '{pyq_name}' in '{subject_name}'.")
                        return
                    else:
                        print(
                            f"Tag '{tag_name}' already exists for pyq '{pyq_name}' in '{subject_name}'.")
                        return
            print(f"pyq '{pyq_name}' not found in '{subject_name}'.")
        else:
            print(f"Subject '{subject_name}' not found.")

    def close_connection(self):
        self.client.close()
        print("connection closed with database")
