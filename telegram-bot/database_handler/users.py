import json
import os

class UserDataManager:
    def __init__(self, file_path):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            # Create a default JSON structure if the file doesn't exist
            self.data = {}
            self._save_data()
        else:
            # Load existing JSON data
            with open(self.file_path, 'r') as file:
                self.data = json.load(file)

    def _save_data(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def register_chat_id(self, chat_id):
        self.data['chat_id'] = chat_id
        self._save_data()
        
    def is_chat_id_exist(self, chat_id):
        return chat_id in self.data
