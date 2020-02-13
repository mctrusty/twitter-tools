import twitter
from pymongo import MongoClient

try:
    from local_settings import *
except ImportError:
    pass

def main():
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN_KEY,
                      access_token_secret=ACCESS_TOKEN_SECRET,
                      tweet_mode='extended')

    client = MongoClient(DB_CONN_STRING)
    db = client.twitter

    my_tl = api.GetHomeTimeline(count=200)
    for item in my_tl:
        rec = item.AsDict()
        try:
            result = db.mytimeline.insert_one(rec)
            print('Created new record as {0}'.format(result.inserted_id))
        except:
            print('duplicate key error')

if __name__ == '__main__':
    main()