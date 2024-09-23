import requests
import threading
import time

class Trashmail:
    def __init__(self):
        res = requests.get("https://futquest.com/generate/email")
        body = res.json()
        self.adress = body['email']
        self.sessionId = body['sessionId']
        self.active = True
        self.last_inbox = [] 

    def getAdress(self):
        return self.adress

    def revokeAdress(self):
        self.adress = ""
        self.sessionId = ""
        self.last_inbox = []
        return True

    def renewAdress(self):
        res = requests.get("https://futquest.com/generate/email")
        body = res.json()
        self.adress = body['email']
        self.last_inbox = []
        self.sessionId = body['sessionId']
        return self.adress

    def getInbox(self):
        inbox = requests.get(f"https://futquest.com/inbox/{self.adress}?sessionId={self.sessionId}")
        inbox_json = inbox.json()
        return inbox_json

    def onEmail(self, callback):
        def check_for_new_email():
            while self.active:
                current_inbox = self.getInbox()
                if current_inbox != self.last_inbox:
                    new_emails = [email for email in current_inbox if email not in self.last_inbox]
                    if new_emails:
                        callback(new_emails)
                    self.last_inbox = current_inbox
                time.sleep(3)
        listener_thread = threading.Thread(target=check_for_new_email)
        listener_thread.daemon = True
        listener_thread.start()
