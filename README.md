# 作り途中です

作り途中なのでまだ適当です。

まず`.env.example`を`.env`にリネームしてください。

リネーム後、`.env`内の以下の設定を変更してください。（やらなくても動くけどメールフォームは動きません）

```
# Gmailのアドレス
mail_username=example@gmail.com 
# 上記Gmailのアドレス。なお、Gmailのセキュリティ警告が出る可能性があります。
mail_password=example
# mail_usernameと同じアドレス
default_mail_sender=example@gmail.com
```

`docker-compose.yml`の置いてあるディレクトリをカレントディレクトリにした状態で

以下のコマンドを実施してください。


```
docker-compose up -d mysql
docker-compose up -d nginx
```

mysqlコンテナが立ち上がり、起動時の設定が終わるまで待ちます。

`docker-compose logs mysql`コマンドを使い、下記のようなログが出てきたら立ち上がりが完了です。

```
mysql_ctr | Version: '5.7.22'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306  MySQL Community Server (GPL)
```

そうしましたら、下記のコマンドを打ってください。

```
docker-compose up -d flask
```

`127.0.0.1`でウェブブラウザを開いてください。

DockerMachineやDocker-Toolboxを使っている場合は、その起動したDockerMachineのIPアドレス
(たぶん`192.168.99.100`)で開いてみてください。

`Nginx`で80番ポートを開けているので見られるはずです。

loginはメールアドレスが`metarion@email.com`　パスワードが`secret`です。

`www/db_create_200.py`は`mysql`コンテナが動いている時に動作させると、適当なブログデータを200個作成します。ページネーションを確認するために作りました。

遊び終わったら`docker-compose down`を押してください。

## 参考リンク
https://github.com/planset/study_flask/blob/master/docs/05.rst

https://flask-migrate.readthedocs.io/en/latest/

https://qiita.com/wasanx25/items/d47caf37b79e855af95f

https://qiita.com/yasunori/items/64606e63b36b396cf695
