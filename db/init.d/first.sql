CREATE DATABASE db_blog;

USE db_blog

CREATE TABLE blog(
    id INT(3) NOT NULL AUTO_INCREMENT,
    title VARCHAR(30),
    honbun VARCHAR(400),
    created_at datetime  default current_timestamp,
    updated_at timestamp default current_timestamp on update current_timestamp,
    primary key(id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO blog (title,honbun)
VALUES ('テスト','本文のテストだよおおおおおおおおん');