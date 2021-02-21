import re
import setting as s
from lib.tweets import tweets
from lib.message import message

def eq_data(data,status_code,intensity):
	msg = None
	value = 0
	if data is None:
		msg = message(None,status_code)
	else:
		data_list = [[tweet['text'],tweet['id']] for tweet in data['data'] \
			if '地震' in tweet['text'] and '最大震度' in tweet['text']]
		# 空データであれば回避
		if data_list == []: return
		# 日付の取得
		day = re.search(r'\d+年\d.+】',data_list[value][0]).group()[:-1]
		# 時間の取得
		time = re.search(r'\d+時\d+分', data_list[value][0]).group()
		# 震源地の取得
		eq_point = re.search(r'、\w+を',data_list[value][0]).group()[1:-1]
		# 震源の深さを取得。取得できない場合、計測中とする。
		try:
			eq_km = re.search(r'約\d+km',data_list[value][0]).group()
		except AttributeError: eq_km = "計測中"
		# 地震の規模の取得(M)
		eq_m = re.search(r'M\d+.\d+',data_list[value][0]).group()
		# 最大震度の取得
		eq_max = re.search(r'最大震度+\d.',data_list[value][0]).group()
		# 震度5「強」の文字列対応
		if eq_max[-1] == "を": eq_max = eq_max[:-1]
		# 詳細情報取得部分
		eq_info = data_list[value][0].split('。')[2]
		# イメージURL作成
		url_base = "https://twitter.com/"+s.USER_ID+"/status/"
		image_num = data_list[value][1]
		url = url_base + image_num
		e = re.search(r'(\d+)', eq_max).group()

		if int(e) >= intensity:
			msg = (
				"発生日時　：　" + day +" "+ time + "\n"
				+ "最大震度　：　" + eq_max + "\n" 
				+ "震源地　　：　" + eq_point + "\n"
				+ "震源の距離：　" + eq_km + "\n"
				+ "地震の規模：　" + eq_m + "\n"
				+ "情報　　　：　" + eq_info + "\n"
				)
			
			msg = message(msg,status_code) + url
	return msg