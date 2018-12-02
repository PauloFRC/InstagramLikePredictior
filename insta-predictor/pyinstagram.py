from InstagramAPI import InstagramAPI
import numpy as np 
import matplotlib.pyplot as plt
from mlpredictor import predict_next_like

username = input('Your instagram username: ')
password = input('Your instagram password: ')
person_id = int(input('ID from the person you will predict: '))

API = InstagramAPI(username, password)
API.login()

API.getProfileData()

#
#my_id = API.LastJson['user']['pk']
#API.getUsernameInfo(person_id)
#n_media = API.LastJson['user']['media_count']

media_infos = []
max_id = ''
likes_per_post = []
comment_count = []

for i in range(10): 
    API.getUserFeed(usernameId=person_id, maxid = max_id)
    media_infos += API.LastJson['items'] 
    if API.LastJson['more_available']==False:          
        break
    max_id = API.LastJson['next_max_id']

media_ids = []
for media_info in media_infos:
	media_ids.append(media_info['id'])

media_likes = []
for media_info in media_infos:
    media_likes.append(media_info['like_count'])
    comment_count.append(media_info['comment_count'])
media_likes = media_likes[::-1]
comment_count = comment_count[::-1]

likers = []

for media_id in media_ids:
	API.getMediaLikers(media_id)
	likes_per_post.append(len(API.LastJson['users']))
	for user in API.LastJson['users']:
		likers.append(user['username'])

x = []
for i in range(len(media_likes)-1):
    x.append([media_likes[i], comment_count[i+1]])
y = media_likes[1:]
next_pred = [media_likes[::-1][0], comment_count[::-1][0]]

last_input = [media_likes[::-1][0],comment_count[::-1][0]]

predict_next_like(x,y,next_pred, evaluate=True)


