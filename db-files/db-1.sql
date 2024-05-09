create database if not exists cm_db;
use cm_db;
create table users(
id int(2) auto_increment primary key,
username varchar(30),
email varchar(50),
password varchar(10)
);

create table contacts(
contact_id int(2) auto_increment primary key,
users_id int(2),
contacts varchar(20),
FOREIGN KEY (users_id) REFERENCES users(id)
);

select * from users;