from __future__ import absolute_import, print_function
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import dataset
from sqlalchemy.exc import ProgrammingError

consumer_key = "rBcSxk6sGyOt4iRS4kJlvQzxJ"
consumer_secret = "KvUGjEsUOshd9EcqJD8CFDGaRtehTGS3AvaQ1HZf8d7yEBEh75"
access_token = "115838090-srTO3Pw5NydC4BWSGR7BumJfAZi7f3DyjRIV0k0M"
access_token_secret = "dtd6cdRjpxrlKqByvfJq620XReprYLYwyLtc1sXaUvVeW"

class StdOutListener(StreamListener):
    def on_status(self, status):
        print(status.text)
        if status.retweeted:
            return

        id_str = status.id_str
        created = status.created_at
        text = status.text
        fav = status.favorite_count
        name = status.user.screen_name
        description = status.user.description
        loc = status.user.location
        user_created = status.user.created_at
        followers = status.user.followers_count

        table = db['myTable']

        try:
            table.insert(dict(
                id_str=id_str,
                created=created,
                text=text,
                fav_count=fav,
                user_name=name,
                user_description=description,
                user_location=loc,
                user_created=user_created,
                user_followers=followers,
            ))
        except ProgrammingError as err:
            print(err)

    def on_error(self, status_code):
        if status_code == 420:
            return False

if __name__ == '__main__':
<<<<<<< HEAD
    db = dataset.connect("sqlite:///tweets.db")
=======
    db = dataset.connect("sqlite:///tweets-2.db")
>>>>>>> 6b42f9c5980a22d5bd520d4382b39df79a5bf087
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['COVID19', 'COVID', 'Coronavirus', 'Manila'])