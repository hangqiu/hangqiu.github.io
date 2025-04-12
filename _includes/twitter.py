import requests
import json
from twitter_credential import BEARER_TOKEN, TWITTER_ID

headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
}

params = {
    "max_results": 5,
    "tweet.fields": "id",
    "exclude": "retweets,replies",
}

try:
    r = requests.get(f"https://api.twitter.com/2/users/{TWITTER_ID}/tweets", headers=headers, params=params)
    print("Status:", r.status_code)
    print("Headers:", r.headers)

    data = r.json()
    print("Response:\n", json.dumps(data, indent=2))

    with open("twitter.html", "w") as f:
        for tweet in data.get("data", []):
            tweet_id = tweet["id"]
            f.write(f'<blockquote class="twitter-tweet"><a href="https://twitter.com/HangQiu/status/{tweet_id}"></a></blockquote>\n')
except Exception as e:
    print("Error:", e)