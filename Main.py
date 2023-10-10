import requests
import webbrowser
import sys
import multiprocessing

from threading import Timer, Thread
channelName = 'riotgames'



contents = requests.get('https://www.twitch.tv/' +channelName).content.decode('utf-8')

chacker = False
def isOnline():
        global chacker
        if 'isLiveBroadcast' in contents:
            print(channelName + ' is live')
            webbrowser.open("https://lolesports.com/live/worlds/riotgames")
            active = multiprocessing.active_children()
            chacker = True


def call_at_interval(time, callback, args):
    while True:
        timer = Timer(time, callback, args=args)
        timer.start()
        timer.join()
        if(chacker):
            print("exit")
            sys.exit()


def setInterval(time, callback, *args):
    Thread(target=call_at_interval, args=(time, callback, args)).start()

#checks every 15 min if riot is live on twitch and opens the riot website if true
setInterval(900000, isOnline)