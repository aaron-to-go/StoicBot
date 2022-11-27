import os

import requests

clientSecret = os.environ["FACEBOOK_CLIENT_SECRET"]
clientId = os.environ["FACEBOOK_CLIENT_ID"] 
accessToken = os.environ["FACEBOOK_ACCESS_TOKEN"]

baseUrl = "https://graph.facebook.com/"

if __name__ == "__main__":

    authentication = requests.get(baseUrl+"oauth/access_token?client_id="+clientId+"&client_secret="+clientSecret+"&grant_type=client_credentials")

    if authentication.status_code == 200:
        accessToken = authentication.json()["access_token"]
    else:
        print(authentication.status_code, authentication.json()["error"])
    
    
    
