import os
from googleapiclient.discovery import build

API_KEY = os.environ.get('YOUTUBE_API')

youtube = build('youtube', 'v3', developerKey = API_KEY)

pychannels = ['PyDataTV', 'EnthoughtMedia', 'Google Cloud Platform', 
('PyData Montreal','UC2d_azMgPLw_8JzgbpNb2oQ'), 'PyDataMCR', 'PyData Madison', ('PyData São Paulo', 'UCejuzULiRcqml_DOnY2IFfA' ),
'PyData Salamanca', 'PyData Krakow', 'PyData Bristol', 'PyData.Osaka',
'PyData Warsaw', 'PyData Bydgoszcz', 'PyData Pune', 'PyData Taipei',
'PyData Manipal', 'San Francisco PyData Meetup Group', 'PyData Mumbai',
'PyData Eindhoven', 'PyData Copenhagen', 'PyData Bangalore', 'Georgi Karadzhov',
'PyData Lancaster', 'PyData Tokyo', 'PyData Tel Aviv', 'PyData Brasilia', 'SciPyLA',
'EuroSciPy', 'Kaggle', 'Explosion']

channel_request = youtube.channels().list(
    part = 'contentDetails',
    #forUsername = 'Jake Vanderplas'
    id = "UCscdxGKSj4hOaVFYvslW1-g"
    #id = 'UCOjD18EJYcsBog4IozkF_7w'

)

channel_response = channel_request.execute()
#print(channel_response)
all_videos_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
#print(all_videos_id)

playlist_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=all_videos_id,
        maxResults=50
    )
playlist_response = playlist_request.execute()

print(len(playlist_response['items']))
print(type(playlist_response['items']))


vid_ids = []
for item in playlist_response['items']:
    vid_ids.append(item['contentDetails']['videoId'])

vid_request = youtube.videos().list(
    part="snippet, statistics, contentDetails",
    id=','.join(vid_ids)
    )

vid_response = vid_request.execute()

for video in vid_response['items']:
    try: tags = video['snippet']['tags']
    except KeyError: tags = 'No tags'
    print(video['snippet']['title'], video['snippet']['publishedAt'], tags)
    print(video['statistics'])
    print(video['contentDetails']['duration'])
    print()
#Not every video has tags - capture if there are

#print(vid_response)
#for item in vid_response['items']:
#   print(item['contentDetails'])
#print(channel_response['items']['contentDetails']['uploads'])

#print(channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads'])