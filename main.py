import requests
import configparser
import datetime
import threading
import win10toast
import os

dirname = os.path.dirname(__file__)

# Row headers
TIME = 1
CATEGORY = 4

# Load config file
config = configparser.ConfigParser()
config.read(dirname + "\\config.ini")

# Create toaster for notifications
toaster = win10toast.ToastNotifier()

lastTime = 0


class MainLoop(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(int(config['OTHER']['delay'])):
            update()


def format_string(s):
    s = s.replace(" ", '')
    s = s.lower()
    return s


def update():
    global lastTime

    response = requests.get("https://www.rescuetime.com/anapi/data",
                            params={'key': config["SECRET"]["apikey"], 'format': 'json'})
    if response.ok:

        total = 0
        for row in response.json()['rows']:
            if format_string(row[CATEGORY]) in format_string(config['OTHER']['categories']).split(','):
                total += row[TIME]

        if total != lastTime:
            lastTime = total
            time = datetime.timedelta(seconds=total)
            toaster.show_toast(str(time), config['OTHER']['message'],
                               duration=int(config['OTHER']['duration']))
            print(time)
    else:
        print('Wrong Api key')


if __name__ == '__main__':
    stopFlag = threading.Event()
    thread = MainLoop(stopFlag)
    update()
    thread.start()
