# 使うために

## コンテナイメージの作成と立ち上げ
1. `.env.example`を`.env`にリネームする
2. `cli`で`docker-compose.yml`のあるディレクトリを`カレントディレクトリ`にした状態で`docker-compose build`を実施する
3. `docker-compose up -d`を実施する

## SQLテーブルの作成（いつか勝手に作ってくれるようにしたいな）
4. `docker exec -it mysql-ctr /bin/bash`で`mysql-ctr`内に入る。
5. `BASH`が起動するため、`mysql -p`を入力する
6. passwordを`root`と打つ
7. MYSQLに移行するので`use db`と打つ
8. コマンドで以下をコピペして実行
``` 
  CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`); 
```

## NGINXにアクセスする
9. `127.0.0.1:80`にWEBブラウザでアクセスする(DockerToolboxなら`192.168.99.100:80`)
10.画面が表示されるので`Name`と`Email`を入力する
11.`SUCCESS`と表示されたらブラウザバック
12.`一覧の確認`を押せば入力した値が表示される
