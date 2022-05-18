--------------- drop tables ---------------------------------------------------
DROP TABLE IF EXISTS articles;
DROP TABLE IF EXISTS magazines;
DROP TABLE IF EXISTS article_types;
DROP TABLE IF EXISTS author;

--------------- table magazines -----------------------------------------------
CREATE TABLE magazines (
    id INT NOT NULL GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO magazines (name) VALUES('IT herald');
INSERT INTO magazines (name) VALUES('IT STORIES');
INSERT INTO magazines (name) VALUES('IT with kids');

--------------- table article_types -------------------------------------------
CREATE TABLE article_types (
    id INT NOT NULL GENERATED ALWAYS AS IDENTITY,
    type VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO article_types (type) VALUES('news');
INSERT INTO article_types (type) VALUES('tech');
INSERT INTO article_types (type) VALUES('entertainment');

--------------- table author --------------------------------------------------
CREATE TABLE author (
    id INT NOT NULL GENERATED ALWAYS AS IDENTITY,
    author VARCHAR(50) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO author (author) VALUES('Chappie');
INSERT INTO author (author) VALUES('Wall-e');
INSERT INTO author (author) VALUES('Atom');
INSERT INTO author (author) VALUES('T1000');

--------------- table articles ------------------------------------------------
CREATE TABLE articles (
    id INT NOT NULL GENERATED ALWAYS AS IDENTITY,
    magazines_id INT,
    article_type_id INT,
    author_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY (magazines_id) REFERENCES magazines(id),
    FOREIGN KEY (article_type_id) REFERENCES article_types(id),
    FOREIGN KEY (author_id) REFERENCES author(id)
);

INSERT INTO articles (magazines_id,article_type_id,author_id) VALUES(1, 2, 3);
INSERT INTO articles (magazines_id,article_type_id,author_id) VALUES(3, 3, 2);
INSERT INTO articles (magazines_id,article_type_id,author_id) VALUES(2, 2, 4);
INSERT INTO articles (magazines_id,article_type_id,author_id) VALUES(1, 2, 1);
