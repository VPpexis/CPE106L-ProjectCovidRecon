from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
import re

ckey="rBcSxk6sGyOt4iRS4kJlvQzxJ"
csecret="KvUGjEsUOshd9EcqJD8CFDGaRtehTGS3AvaQ1HZf8d7yEBEh75"
atoken="115838090-srTO3Pw5NydC4BWSGR7BumJfAZi7f3DyjRIV0k0M"
asecret="dtd6cdRjpxrlKqByvfJq620XReprYLYwyLtc1sXaUvVeW"

class SaveErrortoFile():
    """in progress"""
    pass
    
class DbConnection():
    """in progress"""
    pass

class MyStreamListener(StreamListener):
    def __init__(self, track):
        self.track = track

    def on_data(self, data):
        conn = sqlite3.connect('tweets1.db')
        c = conn.cursor()
        data = json.loads(data)
        _username = data['user']['screen_name']
        try:
            _message = data['text']
            _message = re.sub(r'@[\w]*', '', _message, flags=re.MULTILINE)
            _message = _message.replace('RT : ', '')
        except:
            _message = data['text']
        _language = data['user']['lang']
        _date = data['created_at']
        _creationAccountDate = data['user']['created_at']
        _profileImageUrl = data['user']['profile_image_url']
        _track = str(self.track)
        try:
            c.execute(
                '''INSERT INTO Tweets ('username','lang','track','profileImageUrl','date','creationAccountDate','message') VALUES ("''' + _username + '''","'''
                + _language + '''","''' +_track + '''","''' + _profileImageUrl + '''","''' +_date+'''","'''+_creationAccountDate + '''","'''+_message+'''")''')
            conn.commit()
            conn.close()
            print('up')
        except Exception as _e:
            try:
                _error_file = open('error_file','a')
                _error_file.write('Error: ' + str(_e) +
                'Username: '+ _username +
                'Msg: '+ _message +
                'Lang: '+ _language +
                'Msg Date: '+ _date +
                'Create acnt date: '+ _creationAccountDate +
                'Profile picture: '+ _profileImageUrl)
            except:
                print('error with saving file')
        return(True)

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, MyStreamListener('COVID'))
twitterStream.filter(track=['COVID'], is_async=True)