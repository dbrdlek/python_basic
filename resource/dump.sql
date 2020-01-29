BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'kang','abcdefg@aaa.com','010-0000-0000','kang.com','2020-01-29 02:03:50');
INSERT INTO "users" VALUES(2,'Park','Park@aaa.aaa','010-0000-0001','Park.com','2020-01-29 02:03:50');
INSERT INTO "users" VALUES(3,'Lee','Lee@Lee.com','010-1111-1111','Lee.com','2020-01-29 02:03:50');
INSERT INTO "users" VALUES(4,'Lee','Cho@Cho.com','010-2222-2222','Cho.com','2020-01-29 02:03:50');
INSERT INTO "users" VALUES(5,'Yoo','Yoo@Yoo.com','010-4444-4444','Yoo.com','2020-01-29 02:03:50');
COMMIT;
