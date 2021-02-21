import os
from dotenv import load_dotenv

dotenv_path = '.env'
load_dotenv(dotenv_path)

'''Line'''
LINE_TOKEN = os.environ.get("LINE_TOKEN")
LINE_USER_ID = os.environ.get("LINE_USER_ID")

'''Twitter'''
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
USER_ID = os.environ.get("USER_ID")

''' Discord '''
# API = [os.environ.get("TESTSRV"),os.environ.get("YUNSRV"),os.environ.get("MAMANSRV")]
# API = [os.environ.get("TESTSRV")]
# OWNER = os.environ.get("OWNER")