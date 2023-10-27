import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# Set your API credentials JSON file path
credentials_file = 'your-credentials.json'

# Set the path to the folder containing videos
folder_path = 'output'

# Initialize the YouTube Data API client
credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=['https://www.googleapis.com/auth/youtube.upload'])
youtube = build('youtube', 'v3', credentials=credentials)

# List all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.mp4'):
        video_file_path = os.path.join(folder_path, filename)

        # Define video metadata
        request_body = {
            'snippet': {
                'title': 'Your Video Title',
                'description': 'Your Video Description',
                'tags': ['tag1', 'tag2'],
            },
            'status': {
                'privacyStatus': 'public',  # Change privacy settings as needed
            }
        }

        # Upload the video
        media = MediaFileUpload(video_file_path, chunksize=-1, resumable=True)
        insert_request = youtube.videos().insert(part='snippet,status', body=request_body, media_body=media)
        response = insert_request.execute()

        print(f'Video uploaded: {filename}, Video ID: {response["id"]}')
