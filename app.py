from twitter import Twitter
import time
import sys
from media import Media

#deploy heroku
#test kedua pancing worker supaya muncul...

tw = Twitter()
media = Media()
def start():
    print("Starting...")
    dms = list()
    while True:
        if len(dms) != 0:
            print(len(dms))
            for i in range(len(dms)):
                message = dms[i]['message']
                sender_id = dms[i]['sender_id']
                id = dms[i]['id']

                if len(message) != 0 and len(message) <= 500:
                    if "https://" not in message and "http://" not in message:
                        if "By" in message:
                            message = message.replace("By", "")
                            screen_name = tw.get_user_screen_name(sender_id)
                            media.download_image()
                            media.process_image(message, screen_name)
                            tw.post_tweet()
                            tw.delete_dm(id)
                        else:
                            media.download_image()
                            media.process_image(message, None)
                            tw.post_tweet()
                            tw.delete_dm(id)
                    else:
                        tw.delete_dm(id)
            dms = list()

        else:
            print("DM is empty")
            dms = tw.read_dm()
            print(dms)
            if len(dms) == 0:
                time.sleep(10)

if __name__ == "__main__":
    start()