
create table content
(
	id INTEGER not null
		primary key,
	description VARCHAR(200) not null,
	gender VARCHAR(200) not null
);

INSERT INTO content (id, description, gender) VALUES (1, 'THIS IS SPARTAAAAAAAAA!!!', 'male');
INSERT INTO content (id, description, gender) VALUES (2, 'What''s your favorite scary movie?', 'female');
INSERT INTO content (id, description, gender) VALUES (3, 'Random content 1', 'female');
INSERT INTO content (id, description, gender) VALUES (4, 'Random content 2', 'male');
INSERT INTO content (id, description, gender) VALUES (5, 'Random content 3', 'female');
INSERT INTO content (id, description, gender) VALUES (6, 'Random content 4', 'female');
INSERT INTO content (id, description, gender) VALUES (7, 'Random content 5', 'male');