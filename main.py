import os
import requests
import logging

logger = logging.getLogger(__name__)

clientSecret = os.environ["FACEBOOK_CLIENT_SECRET"]
clientId = os.environ["FACEBOOK_CLIENT_ID"] 
accessToken = os.environ["FACEBOOK_ACCESS_TOKEN"]
businessAccountId = os.environ["INSTAGRAM_BUSINESS_ID"]

baseUrl = "https://graph.facebook.com/"
apiVersion = "v15.0/"

dummyImageUrl = "https://raw.githubusercontent.com/aaron-to-go/StoicBot/master/assets/images/triangle_peach.png"
dummyCaption = "example post via graph api"

def getLongLivedAccessToken():
    authentication = requests.get(baseUrl+"oauth/access_token?client_id="+clientId+"&client_secret="+clientSecret+"&grant_type=client_credentials")

    if authentication.status_code == 200:
        return authentication.json()["access_token"]
    else:
        return f'{authentication.status_code}, {authentication.json()["error"]}'

def createMediaContainer(imageUrl, caption):
    try:
        containerResponse = requests.post(
            baseUrl
            + apiVersion
            + businessAccountId
            + "/media?image_url=" + imageUrl
            + "&caption=" + caption
            + "&access_token=" + accessToken
            )
        return containerResponse.json()["id"]

    except Exception as err:
        logging.error(err)
        raise


def publishMediaContainer(mediaContainerId):
    try: 
        postResponse = requests.post(
            baseUrl
            + apiVersion
            + businessAccountId
            + "/media_publish?creation_id=" + mediaContainerId
            + "&access_token=" + accessToken
        )

        return postResponse.json()["id"]

    except Exception as err:
        logging.error(err)
        raise



if __name__ == "__main__":

    try:
        mediaContainerId = createMediaContainer(dummyImageUrl, dummyCaption)
        postId = publishMediaContainer(mediaContainerId)
        
        print(f'Post successfull \nmediaContainerId: {mediaContainerId} \npostId: {postId}')

    except ValueError as err:
        print(err.args) 
    
