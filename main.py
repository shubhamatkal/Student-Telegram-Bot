from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#GLOBAL VARIABLES
logged_in = False


class WhatsAppBot:
    def __init__(self):
        global logged_in
        self.driver = webdriver.Chrome()
        self.driver.get("https://web.whatsapp.com/")
        print("dear admin kindly scan the qr code and make the login process")
        if input("have you performed login, if yes type Y") == "Y":
            logged_in = True
        # Scan the QR code to log in to your WhatsApp account.

        self.last_messages = []

    def get_messages(self):
        """Returns a list of all the new messages."""

        # messages = []
        new_messages = self.driver.find_elements(By.XPATH,"//div[@class='_2KKXC']" )      #find_elements_by_xpath("//div[@class='_2wP43']")
        for message in new_messages:
            if message.text not in self.last_messages:
                self.last_messages.append(message.text)
                print(message.text)
        # print(self.last_messages)
        return self.last_messages

    def send_message(self, to_number, message):
        """Sends a message to the specified number."""

        self.driver.find_element(By.XPATH,"//input[@title='Search or start new chat']").send_keys(to_number)
        self.driver.find_element(By.XPATH,"//span[@title='" + to_number + "']").click()
        self.driver.find_element(By.XPATH,"//div[@title='Type a message']").send_keys(message)
        self.driver.find_element(By.XPATH,"//button[@title='Send']").click()

    def check_messages(self):
        """Checks for new messages and responds to them."""

        messages = self.get_messages()

        for message in messages:
            if message == "hello":
                self.send_message(message.split(":")[0], "This is automated message")

if __name__ == "__main__":
    bot = WhatsAppBot()

    while logged_in:
        print("checking new messages")
        bot.check_messages()
        time.sleep(10)