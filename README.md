# [WIP] mjai-review
AIがあなたの牌譜をレビューします！

天鳳の牌譜をレビューするWEBサイト。

## バグ報告・要望など
[issue](https://github.com/yuarasino/mjai-review/issues/new) にお願いします。

## 開発の始め方
vscodeとdockerを利用します。

### vscode拡張機能のインストール
- ms-azuretools.vscode-docker
- ms-vscode-remote.vscode-remote-extensionpack
- editorconfig.editorconfig

### 開発コンテナの立ち上げ

1. `docker-compose build`

2. 左下の><アイコンから、 `Remote-Containers: Open Folder in Container...` を選択し、 `mjai-review/docker/python` を開いて、pythonコンテナに入る

3. 左下の><アイコンから、 `Remote-Containers: Open Folder in Container...` を選択し、 `mjai-review/docker/node` を開いて、nodeコンテナに入る


## 設計

### Dockerコンテナ構成
- postgres　　　DB
- django　　　　バックエンド
  - mjai　　　　　　天鳳牌譜からmjson形式テキストへ変換する
  - akochan　　　　mjson形式テキストからレビューを出力する
- celery　　　　非同期タスク
- redis　　　　　メッセージキュー
- vue　　　　　　フロントエンド
- nginx　　　　　WEB

### レビューフロー
1. 画面 >> (API) >> 天鳳観戦URL
2. 天鳳観戦URL >> (天鳳サイト) >> 天鳳牌譜(gzip)
3. 天鳳牌譜(gzip) >> (mjai) >> mjson形式テキスト
4. mjson形式テキスト>> (akochan) >> レビュー


## 関連プロジェクト

### [critter-mj/akochan](https://github.com/critter-mj/akochan)
牌譜のレビューを行う麻雀AI、akochanのリポジトリ。強さ的には、天鳳七段〜九段とのこと。

### [Equim-chan/akochan-reviewer](https://github.com/Equim-chan/akochan-reviewer)
開発のきっかけとなった、akochanを利用して牌譜をレビューするツールのリポジトリ。設計をする上で、参考にさせていただきました。
