import requests
import json

api_Key = "AIzaSyChpdAHXZdhtXjO7mjElyCOWipUHEsI-yE"
contentOwner = "MrBeast"

def getPlaylistId():

    url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={contentOwner}&key={api_Key}"

    response = requests.get(url)
    print(response)

    data = response.json()
    print(json.dumps(data,indent=4))

    channel_items = data['items'][0]
    channel_playListId = channel_items['contentDetails']['relatedPlaylists']['uploads']

    print(channel_playListId)
    return channel_playListId

if __name__ == "__main__":
    getPlaylistId()