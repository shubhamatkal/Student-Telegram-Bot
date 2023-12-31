from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import datetime
# GLOBAL VARIABLES
logged_in = False
first_interation = True


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

        # texted_numbers = []
        num_msg = {}
        new_messages = []
        new_numbers = []
        # find_elements_by_xpath("//div[@class='_2wP43']")
        new_messages = self.driver.find_elements(
            By.XPATH, "//div[@class='_2KKXC']")
        new_numbers = self.driver.find_elements(
            By.XPATH, "//div[@class='Mk0Bp _30scZ']")
        for number in new_numbers:
            value = new_messages[0].text
            # Add the key-value pair to the dictionary.
            num_msg[number.text] = value
            # Remove the first element of the second list.
            new_messages.pop(0)
        # if message.text not in self.last_messages:
        #     self.last_messages.append(message.text)
        #     print(message.text)
        # print(self.last_messages)
        print(num_msg)
        return num_msg

    def send_message(self, to_number, message):
        global first_interation
        """Sends a message to the specified number."""
        print(f"sending to {to_number}")
        # if first_interation:
        #     search_box = self.driver.find_element(By.XPATH, "//div[@class='_3sHED']")
        #     search_box.click()
        #     first_interation = False
        print("clicked the search box")
        self.driver.find_element(
            By.XPATH,
            '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]').send_keys(to_number)
        time.sleep(2)
        print("typed the number")
        try:
            self.driver.find_element(
                By.XPATH, "//span[@title='" + to_number + "']").click()
            time.sleep(1)
            print("selected the contact")
            self.driver.find_element(
                By.XPATH, "//div[@title='Type a message']").send_keys(message)
            print("typed a message")
            self.driver.find_element(
                By.XPATH, "//button[@aria-label='Send']").click()
            print("message sent")
            # Find the element.
            # element = driver.find_element(By.XPATH, "//div[@class='_3sHED']")
        except NoSuchElementException:
            # Do nothing if the element is not found.
            pass

    def check_messages(self):
        """Checks for new messages and responds to them."""

        messages = self.get_messages()
        print(messages)
        for key, value in messages.items():
            if value == "hey":
                self.send_message(key, "hello, this is autmated message")
        print("iterated over all messages , done , waiting for other list")


if __name__ == "__main__":
    bot = WhatsAppBot()

    while logged_in:
        print("checking new messages")
        bot.check_messages()
        time.sleep(10)
