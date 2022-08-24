## Prerequisites 

### Installation
---
- Install tweepy
  - `pip install tweepy`
- Install Google Cloud Storage (if you have a GCP account)
  - `pip install google-cloud-storage` 
- Install dotenv to load environmente variables from .env file
  - `pip install python-dotenv`

### Set Environment variable or create .env file
---
- Set environment variable `BEARER` with bearer token from Twitter
  - `export BEARER=xxxxxx`

  OR

- Create .env file in the same directory with main.py and set variable `BEARER` with bearer token from Twitter

----

### NOTES on the script:

- Used twitter v2 API.
- Used [search_recent_tweets()](https://developer.twitter.com/en/docs/twitter-api/tweets/search/introduction) since this is accessible using the essential account.
- `search_recent_tweets()` is limited to the tweets that were posted the last week.
- Composed of three functions `extract_data()`, `write_to_local()`, `upload_json_to_gcs()`.
- `extract_data()` extracts data from twitter using `search_recent_tweets()` and builds the json to write. Currently limited `max_results` to 10 for testing purposes.
- `write_to_local()` writes the json locally on the current directory.
- `upload_json_to_gcs()` uploads the created json to Google Cloud Storage
- Required inputs are currently hard coded for testing purposes (see inputs below)

Required inputs:

- start_time -> start date for searching in format YYYY-MM-DDT00:00:00Z
- end_time -> end date for searching in format YYYY-MM-DDT00:00:00Z
- hash_tag -> hash tag to search (**#ecommerce**)
- json_filename  -> output filename
