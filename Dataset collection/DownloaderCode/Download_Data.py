import csv
import pandas as pd
import sys
import os
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import argparse
import pickle
import json



# python Download_Data.py   -ct 'iOMDZeuyTMqdr1dvR7R5dZWAi' -cs 'e9YllCfH6ydwmKUwCzzTrJXsFdaOQgNfLOR2umHP5rKFvpmPoq' -at '775533408780849152-1RydoG7NUVlrm5jPWTEby25U75uBf7e' -ats 'z9nHxSPfEoB9S7KlNJJxut7cBkQUVvBCYZ1lqZ1JERX6L'


# python Download_Data.py   -ct '5rY55GKj7BOUV5O7s9K7vM59e' -cs 'ZSAsmNQe8cWvjvbR2e40Fuy758D6afHmxqnoVsiU3W7Dc4xUuP' -at '1313722585964703745-hUuhmOXwhe2MGKzSIBt3hL77w7Jd1P' -ats 'fM9eDZCLi4zOu9hk8rugAASZoCvblaGttBLpOtaAECQAo'


# test_dict = {'created_at': 'Mon Mar 02 10:23:41 +0000 2015', 'id': 572341498827522049, 'id_str': '572341498827522049', 'text': "Drasko they didn't cook half a bird you idiot #mkr", 'truncated': False, 'entities': {'hashtags': [{'text': 'mkr', 'indices': [46, 50]}], 'symbols': [], 'user_mentions': [], 'urls': []}, 'source': '<a href="http://twitter.com/download/iphone" rel="nofollow">Twitter for iPhone</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 110114783, 'id_str': '110114783', 'name': 'patricia hilder', 'screen_name': 'trish2295', 'location': '', 'description': '', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 14, 'friends_count': 62, 'listed_count': 0, 'created_at': 'Sun Jan 31 11:35:37 +0000 2010', 'favourites_count': 253, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': False, 'statuses_count': 184, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/450615765431894016/yt-wPy5f_normal.jpeg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/450615765431894016/yt-wPy5f_normal.jpeg', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': {'type': 'Point', 'coordinates': [-28.07334137, 153.37975174]}, 'coordinates': {'type': 'Point', 'coordinates': [153.37975174, -28.07334137]}, 'place': {'id': '017453ae077eafd3', 'url': 'https://api.twitter.com/1.1/geo/id/017453ae077eafd3.json', 'place_type': 'city', 'name': 'Gold Coast', 'full_name': 'Gold Coast, Queensland', 'country_code': 'AU', 'country': 'Australia', 'contained_within': [], 'bounding_box': {'type': 'Polygon', 'coordinates': [[[153.186551712, -28.2003171475], [153.552171232, -28.2003171475], [153.552171232, -27.708126368], [153.186551712, -27.708126368]]]}, 'attributes': {}}, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 4, 'favorited': False, 'retweeted': False, 'lang': 'en'}





def save_object(obj, filename):
    with open(filename, 'wb') as fp:
        pickle.dump(obj, fp)
        
def retrieveData(consumer_token,consumer_secret,access_token,access_token_secret):
    csvfile =  open("reconstruct_paper_dataset2.csv","w")


    
    writer = csv.writer(csvfile)
    # writer.writerow(["Tweet Id","Tweets","User Id", "Screen Name", "Class"])




    auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    import json

    #archivos con los ids de los doferentes datasets
    names = ['Waseem_Dataset']
    # names = ['Data_new']
    # names = ['SemEval_Dataset']
    archivos_ids = ['./indexData/Waseem_IDS.csv']
    # archivos_ids = ['./indexData/Data_new_IDS.csv']
    # archivos_ids = ['/home/qiqingh/Desktop/User_distribution_experiments/Data/trial_en.tsv']
    total = 0
    for current_file in range(len(archivos_ids)):
        c = 0
        print('Downloading ' + str(current_file + 1)+ '\r\n')
        data =  pd.read_csv(archivos_ids[current_file],'r',delimiter = ',',encoding = 'utf-8')

        # str_json = []
        
        for j in data.values:
            total += 1
            print("process the " + str(total) + " \r\n")

            try:

                # writeFile = open("./new_dataset.txt", "a+")
                tweet = api.get_status(j[0].split('\t')[0])._json
                print("get the API return\r\n")
                # print(tweet)

                # writer.writerows([tweetId, tweet, userId, screenName, classType])
                # print(type(tweet))
                # tweetId = str(tweet['id_str'])
                # print(tweetId)
                # tweet = str(tweet['text'])
                # print(tweet)

                # userId = str(tweet['user']['id'])
                # print(userId)
                # screenName = str(tweet["user"]["screen_name"])
                # print(screenName)
                # classType = str(j[0].split('\t')[1])
                # print(classType)
                writer.writerow([str(tweet['id_str']), str(tweet['text']), str(tweet['user']['id']), str(tweet["user"]["screen_name"]), str(j[0].split('\t')[1])])
          

                c += 1

                # writer.writerow([tweetId, tweet, userId, screenName, classType])
      
                # writeFile.write(str(tweet['id_str']) + "," + str(tweet['text']) + "," + str(tweet['user']['id_str']) + "," + str(tweet["user"]["screen_name"]) + "," + j[0].split('\t')[1] + "\r\n")
                # str_json.append({"id":tweet['id'],"name": tweet['user']['name'], "text":tweet['text'], "label": j[0].split('\t')[1]})
                
                # writeFile.close()




            except Exception as e: 
                print(str(e))
                pass


        print(str(c) + ' tweets downloaded')
        csvfile.close()

        
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Descargar datos usando el api de twitter')
    parser.add_argument('-ct', '--consumer_token', required=True)
    parser.add_argument('-cs', '--consumer_secret', required=True)
    parser.add_argument('-at', '--access_token', required=True)
    parser.add_argument('-ats', '--access_token_secret', required=True)

    consumer_token = parser.parse_args().consumer_token
    consumer_secret = parser.parse_args().consumer_secret
    access_token = parser.parse_args().access_token
    access_token_secret = parser.parse_args().access_token_secret
    
    retrieveData(consumer_token,consumer_secret,access_token,access_token_secret)
    