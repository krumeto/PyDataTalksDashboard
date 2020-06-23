import os
from googleapiclient.discovery import build
import pandas as pd

API_KEY = os.environ.get('YOUTUBE_API')



def connect_to_youtube_api(key):
    return build('youtube', 'v3', developerKey = key)


def get_channels_videos(client, channel_id):

    #Step 1 - get channels playlist containing all its videos
    channel_request = client.channels().list(part = 'contentDetails', id = channel_id)
    channel_response = channel_request.execute()
    all_videos_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    #Step 2 - get all videos ID from the playlist

    playlist_request = client.playlistItems().list(
        part='contentDetails',
        playlistId=all_videos_id,
        maxResults=50 #!!!!!!!!!!!!!!!!!!!TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!
    )
    playlist_response = playlist_request.execute()

    vid_ids = []
    for item in playlist_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])

    video_string = ','.join(vid_ids)

    return video_string

def get_video_data(client, video_string):

    vid_request = client.videos().list(part="snippet, statistics, contentDetails", id= video_string)
    vid_response = vid_request.execute()

    video_dict = {}

    for video in vid_response['items']:
        hash_dict = {}
        hash_dict['channelID'] = video['snippet']['channelId']
        hash_dict['channelTitle'] = video['snippet']['channelTitle']
        hash_dict['Title'] = video['snippet']['title']
        hash_dict['Publish Date'] = video['snippet']['publishedAt']
        hash_dict['Description'] = video['snippet']['description']

        try: tags = video['snippet']['tags']
        except KeyError: tags = 'No tags'
        hash_dict['Tags'] = tags
        hash_dict['Stats'] = video['statistics']
        hash_dict['Duraction'] = video['contentDetails']['duration']

        video_dict[video['id']] = hash_dict

    return video_dict


youtube = connect_to_youtube_api(API_KEY)

video_string = get_channels_videos(youtube, "UCscdxGKSj4hOaVFYvslW1-g")
print(pd.DataFrame(get_video_data(youtube, video_string)).T)

# youtube = build('youtube', 'v3', developerKey = API_KEY)

# # pychannels = ['PyDataTV', 'EnthoughtMedia', 'Google Cloud Platform', 
# # ('PyData Montreal','UC2d_azMgPLw_8JzgbpNb2oQ'), 'PyDataMCR', 'PyData Madison', ('PyData São Paulo', 'UCejuzULiRcqml_DOnY2IFfA' ),
# # 'PyData Salamanca', 'PyData Krakow', 'PyData Bristol', 'PyData.Osaka',
# # 'PyData Warsaw', 'PyData Bydgoszcz', 'PyData Pune', 'PyData Taipei',
# # 'PyData Manipal', 'San Francisco PyData Meetup Group', 'PyData Mumbai',
# # 'PyData Eindhoven', 'PyData Copenhagen', 'PyData Bangalore', 'Georgi Karadzhov',
# # 'PyData Lancaster', 'PyData Tokyo', 'PyData Tel Aviv', 'PyData Brasilia', 'SciPyLA',
# # 'EuroSciPy', 'Kaggle', 'Explosion']

# channel_request = youtube.channels().list(
#     part = 'contentDetails',
#     #forUsername = 'Jake Vanderplas'
#     id = "UCscdxGKSj4hOaVFYvslW1-g"
#     #id = 'UCOjD18EJYcsBog4IozkF_7w'
# )

# channel_response = channel_request.execute()
# #print(channel_response)
# all_videos_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
# #print(all_videos_id)





# playlist_request = youtube.playlistItems().list(
#         part='contentDetails',
#         playlistId=all_videos_id,
#         maxResults=50
#     )
# playlist_response = playlist_request.execute()

# print(len(playlist_response['items']))
# print(type(playlist_response['items']))


# vid_ids = []
# for item in playlist_response['items']:
#     vid_ids.append(item['contentDetails']['videoId'])

# vid_request = youtube.videos().list(
#     part="snippet, statistics, contentDetails",
#     id=','.join(vid_ids)
#     )

# vid_response = vid_request.execute()

# for video in vid_response['items']:
#     try: tags = video['snippet']['tags']
#     except KeyError: tags = 'No tags'
#     print(video['snippet']['title'], video['snippet']['publishedAt'], tags)
#     print(video['statistics'])
#     print(video['contentDetails']['duration'])
#     print()
# #Not every video has tags - capture if there are

# #print(vid_response)
# #for item in vid_response['items']:
# #   print(item['contentDetails'])
# #print(channel_response['items']['contentDetails']['uploads'])

# #print(channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads'])