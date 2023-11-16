import os
import csv


class User:
    parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    db_directory = os.path.join(parent_directory, "db")
    def __init__(self):
        # Create the 'db' directory if it doesn't exist
        if not os.path.exists(self.db_directory):
            os.makedirs(self.db_directory)
        self.csv_file = os.path.join(self.db_directory, 'users.csv')
        print(self.csv_file)
        self.headers = ['chat id', 'username', 'registered Subjects', 'is admin', 'last login']
        if not os.path.exists(self.csv_file):
            self._create_csv()

    def _create_csv(self):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.headers)

    def is_chat_id_registered(self, chat_id):
        with open(self.csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['chat id'] == str(chat_id):
                    return True
            return False

    def register_chat_id(self, chat_id):
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow({chat_id: "chat id"})  # Empty placeholders for other columns
        print(f"chat id : {chat_id} added to database")


# #FOR TESTING ABOVE CLASS
# if __name__ == '__main__':
#     #Test the User class
#     user = User()
#     if user.is_chat_id_registered(1234567) == False:  # Check if chat ID 123456 is registered
#         user.register_chat_id(1234567)  # Register chat ID 123456
#     else:
#         print("User already exists")
