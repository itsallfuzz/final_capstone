from requests_oauthlib import OAuth1Session
import json

class Tweet():
    CONSUMER_KEY = "SrMXJ0lHfVLLXQKcjQxpAuoju"
    CONSUMER_SECRET = "alu6MHNyTwOx9cfDg4SAXuJAMHCzcvU9Q97PAP9XmVawalVauP"

    _instance = None

    def authenticate(self):

        # Get request token
        request_token_url = "https://api.twitter.com/oauth/request_token"
        oauth = OAuth1Session(
            self.CONSUMER_KEY,
            client_secret=self.CONSUMER_SECRET,
            callback_uri="oob"
            )

        try: fetch_response = oauth.fetch_request_token(request_token_url)
        except ValueError: print(
            "There may have been an issue with the consumer_key or " \
            "consumer_secret you entered." )

        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")
        print("Got OAuth token: %s" % resource_owner_key)

        # Get authorisation
        base_authorization_url = "https://api.twitter.com/oauth/authorize"
        authorization_url = oauth.authorization_url(base_authorization_url)
        print("Please go here and authorize: %s" % authorization_url)
        verifier = input("Paste the PIN here: ")

        # Get the access token
        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = OAuth1Session(
            self.CONSUMER_KEY,
            client_secret=self.CONSUMER_SECRET,
            resource_owner_key=resource_owner_key,
            resource_owner_secret=resource_owner_secret,
            verifier=verifier,
            )
        oauth_tokens = oauth.fetch_access_token(access_token_url)

        access_token = oauth_tokens["oauth_token"]
        access_token_secret = oauth_tokens["oauth_token_secret"]

        # Make the request
        self.oauth = OAuth1Session(
            self.CONSUMER_KEY,
            client_secret=self.CONSUMER_SECRET,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
            )
        return oauth


    def make_tweet(self, tweet_text, image_path=None):
        if not self.oauth:
            raise ValueError ('Authentication failed!')

        media_id = None

        if image_path:
            try:
                media_endpoint = "https://upload.twitter.com/1.1/media/upload.json"

                with open(image_path, 'rb') as image_file:
                    files = {'media': image_file}
                    media_response = self.oauth.post(media_endpoint, files=files)

                if media_response.status_code == 200:
                    media_id = media_response.json()['media_id_string']
                else:
                    print(f"Image upload failed: {media_response.status_code}")
            except Exception as e:
                print(f"Error uploading image: {e}")


        tweet = {"text": tweet_text}
        if media_id:
            tweet["media"] = {"media_ids": [media_id]}

        # Making the request
        response = self.oauth.post(
            "https://api.twitter.com/2/tweets",
            json=tweet,
            )

        if response.status_code != 201:
            raise Exception( "Request returned an error: {} " \
            "{}".format(response.status_code, response.text)
            )
        print("Response code: {}".format(response.status_code))

        # Saving the response as JSON
        json_response = response.json()
        print(json.dumps(json_response, indent=4, sort_keys=True))


    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Tweet, cls).__new__(cls)
            cls._instance.authenticate()

        # Put any initialisation here.
        return cls._instance