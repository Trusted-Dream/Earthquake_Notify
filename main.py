import setting as s
from linebot import LineBotApi
from linebot.models import TextSendMessage
from lib.data import eq_data,tweets

def main():
	# 地震情報保存ファイル
	eq_file = "eq.txt"
	# ツイートの取得数
	max_results = 10
	# 震度
	intensity = 4
	data,status_code = tweets(max_results)
	msg = eq_data(data,status_code,intensity)
	if msg == None: return

	# ファイルから旧情報の読み込み
	try:
		with open(eq_file) as f: text = f.read()
	except FileNotFoundError:
		# ファイルが無ければ作成
		with open(eq_file, mode="w") as f: text = None
	# 旧情報と取得した情報の差分チェック
	if text != msg:
		with open(eq_file, mode="w") as f: f.write(msg)
		if msg != None:
			line_bot_api = LineBotApi(s.LINE_TOKEN)
			line_bot_api.push_message(
				s.LINE_USER_ID, 
				messages=(TextSendMessage(text=msg))
			)
if __name__ == "__main__": main()