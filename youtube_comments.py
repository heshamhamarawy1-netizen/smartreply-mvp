# youtube_comments.py
from googleapiclient.discovery import build

API_KEY = "AIzaSyDYa9UaKzsSkXRud_6jYxmrGGbXjNs_dmQ"

def get_comments(video_id, max_results=10):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText',
        maxResults=max_results
    )
    response = request.execute()
    
    comments = []
    for item in response.get('items', []):
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
    return comments

