# Earthquake-Notify
![Python Version](https://img.shields.io/badge/Python-3.5%2B-orange)
![Twitter V2](https://img.shields.io/badge/Twitter%20API-v2-blue)
## 概要
 - Twitterからツイートを取得してLINEに通知します。
## 仕様について
 - Twitter API v2
 - Python3.5+

## 準備
 - `/bin/env python setup.py install` を実行して必要なモジュールをインストールします。
 - .envを作成します。
 - .env.sampleを参考に内容を記述します。

## 使用方法
 - main.pyを実行します。

## テストについて
 - `pytest` or `pytest -v` を実行するとテストが走ります。
 
## 残骸について
 - 元々はDiscord用に作成していましたが、フルスクラッチで作り直しました。また、Discord用とLINE用とで両用できないか、模索中であり残骸はあえて残してあります。