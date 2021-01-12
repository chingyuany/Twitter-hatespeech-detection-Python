
# -*- coding:utf-8 -*-
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterPager
 
 
def search_tweets(the_consumer_key, the_consumer_secret, the_access_token_key,
                  the_access_token_secret):

  api = TwitterAPI(consumer_key=the_consumer_key,
                     consumer_secret=the_consumer_secret,
                     access_token_key=the_access_token_key,
                     access_token_secret=the_access_token_secret
                  )
  r = TwitterPager(api, 'search/tweets', {'q': 'pizza', 'count': 10, 'lang': 'en'})
  for item in r.get_iterator():


    # print item

    if 'id' in item:
      print item['id']
    if 'text' in item:
      print item['text']
    # if 'entities' in item:
      # print item['entities']

    if 'message' in item and item['code'] == 88:
      print 'SUSPEND, RATE LIMIT EXCEEDED: %s\n' % item['message']
      break
    print '\r\n\r\n\r\n'
 
 
if __name__ == "__main__":
  consumerKey = "iOMDZeuyTMqdr1dvR7R5dZWAi"  
  consumerSecret = "e9YllCfH6ydwmKUwCzzTrJXsFdaOQgNfLOR2umHP5rKFvpmPoq"
  accessToken = "775533408780849152-1RydoG7NUVlrm5jPWTEby25U75uBf7e"
  accessTokenSecret = "z9nHxSPfEoB9S7KlNJJxut7cBkQUVvBCYZ1lqZ1JERX6L"


  search_tweets(the_consumer_key=consumerKey,
                the_consumer_secret=consumerSecret,
                the_access_token_key=accessToken,
                the_access_token_secret=accessTokenSecret)