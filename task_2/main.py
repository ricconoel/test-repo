import tweepy
import json
import os
from dotenv import load_dotenv
from google.cloud import storage

def extract_data(start_time, end_time, hash_tag):

    load_dotenv()
    bearer = os.getenv("BEARER") #export environment variable

    client = tweepy.Client(bearer_token=bearer)
    tweet_data = []
    try:
        tweets = client.search_recent_tweets(query=hash_tag,
                                            max_results=10,
                                            start_time=start_time,
                                            end_time=end_time,
                                            tweet_fields=["created_at"],
                                            user_fields=["username"],
                                            expansions='author_id')
        
        for tweet, user in zip(tweets.data, tweets.includes["users"]):
            tweet_info = {
                "id": tweet.id,
                "created_at": tweet.created_at.strftime("%Y-%m-%d"),
                "text": tweet.text,
                "username": user.username
            }
            tweet_data.append(tweet_info)

    except tweepy.errors.TweepyException as err:
        print(err)

    return tweet_data

def write_to_local(twitter_data, output_json_filename):

    out_file = open(output_json_filename, "w")
    json.dump(twitter_data, out_file, indent=2)


def upload_json_to_gcs(bucket_name, source_file_name, destination_blob_name):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to gs://{bucket_name}/{destination_blob_name}.")

if __name__ == '__main__':

    start_time = "2022-08-18T00:00:00Z"
    end_time = "2022-08-24T00:00:00Z"
    hash_tag = "#ecommerece"
    json_filename = "twitter_data.json"

    data_dict = extract_data(start_time=start_time,
                             end_time=end_time,
                             hash_tag=hash_tag,)

    write_to_local(data_dict,json_filename)

    # cloud params
    bucket_name = "20220824-test" #set bucket name
    
    upload_json_to_gcs(bucket_name=bucket_name,
                       source_file_name=json_filename,
                       destination_blob_name=json_filename)

