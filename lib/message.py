import setting as s
import json
import urllib.request as req
from itertools import product

'''開発途中 -- ディスコード用実装時の残骸あり'''

# def message(msg,status_code,tweeturl):
def message(msg,status_code):
	# # Discord用ヘッダー
	# headers = {
	# 	"User-Agent": "curl/7.64.1", 
	# 	"Content-Type" : "application/json"
	# }

	# 200以外が返された時の処理
	if status_code != 200:
		data_list = (
			"%dのステータスが返されました！\n" % status_code
			+ "TwitterAPIが利用できません！")
		# content = {
		# 	'content' : s.OWNER + msg
		# }
		# data_list = [content]
		
	else:
		# 気象庁の地震情報TOPページ
		url = "http://www.jma.go.jp/jp/quake/index.html\n"
		# ツイッター「地震」の検索一覧
		tweet = "https://twitter.com/search?q=%E5%9C%B0%E9%9C%87&src=typed_query&f=live\n"
		# ウェザーニュースのチャンネル
		youtube = "https://www.youtube.com/channel/UCNsidkYpIAQ4QaufptQBPHQ\n"
		data_list = (
			url + tweet + youtube + msg
		)
		# embeds = [
		# 	{
		# 	# 赤色
		# 	'color': 16718337,
		# 	'description': "[気象庁の情報]("+ url + ")\n" + msg
		# 	}
		# ]
		# content = {
		# 	"embeds" : embeds,
		# 	'content' : "震度4以上の地震が発生しています！\n"
		# 		+ "> [Twitter地震情報で確認する]("+ tweet + ")\n"
		# 		+ "> [ウェザーニュースで確認する]("+ youtube + ")\n"
		# }
		# content2 = {'content': tweeturl}
		# data_list = [content,content2]
	# return data_list,headers
	return data_list