import urllib3
import setting
import json

http = urllib3.PoolManager()
KEY = setting.BEARER_TOKEN

def tweets(max_results):
	url = 'https://api.twitter.com/2/tweets/search/recent'
	params = {
		'query'        : 'from:'+setting.USER_ID,
		'max_results'  : max_results,
		'expansions'   : 'author_id,attachments.media_keys',
		'media.fields' : 'preview_image_url,type',
		'place.fields' : 'country,country_code',
		'tweet.fields' : 'created_at,lang',
		'user.fields'  : 'created_at,description,id,name'
		}
	response = http.request(
		'GET',
		url=url,
		headers= {'Authorization': 'Bearer '+KEY},
		fields = params,
	)
	result = json.loads(response.data)
	status_code = response.status
	if status_code == 200:
		return result,status_code
	else:
		return None,status_code