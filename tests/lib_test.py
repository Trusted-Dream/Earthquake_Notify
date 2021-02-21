import pytest
import re
from lib.message import message
from lib.tweets import tweets
from lib.data import eq_data

class TestClass(object):

	# リスエスト通りか確認とステータスコード200で返すことを確認
	@pytest.mark.parametrize("x", [10,20,30])
	def test_tweet_passed(self,x):
		data,status = tweets(x)
		assert 200 == status
		assert len(data['data']) == x

	# リクエスト要求拒否時の挙動確認
	def test_tweet_error(self):
		data,status = tweets(0)
		assert 400 == status
		assert data == None 

	# 引数のメッセージが正常に反映されているか確認
	def test_msg_passed(self):
		text = "TestMessage."
		data_list = message(text,200)
		assert text in data_list

	# ステータスコード200以外のエラーメッセージ確認
	def test_msg_error(self):
		text = "TestMessage."
		err_msg = "TwitterAPIが利用できません！"
		data_list = message(text,400)
		assert err_msg in data_list

	# それぞれ取得する震度を変えて正常に動作するかチェック
	# ※実際の地震で判定
	@pytest.mark.parametrize("x", [10,20,30])
	@pytest.mark.parametrize("y", [1,2,3,4])
	def test_data_passed(self,x,y):
		eq = ""
		data,status = tweets(x)
		msg = eq_data(data,status,y)
		if msg != None:
			eq = re.search(r'最大震度+\d',msg).group()
		assert msg is None or y <= int(eq[-1])