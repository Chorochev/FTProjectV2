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
    headers VARCHAR(50),
    texts VARCHAR(500),   
    PRIMARY KEY(id),
    FOREIGN KEY (magazines_id) REFERENCES magazines(id),
    FOREIGN KEY (article_type_id) REFERENCES article_types(id),
    FOREIGN KEY (author_id) REFERENCES author(id)
);

INSERT INTO articles (magazines_id,article_type_id,author_id, headers, texts) VALUES(1, 2, 3, 'Header_001', 'some text 001');
INSERT INTO articles (magazines_id,article_type_id,author_id, headers, texts) VALUES(3, 3, 2, 'Header_002', 'some text 002');
INSERT INTO articles (magazines_id,article_type_id,author_id, headers, texts) VALUES(2, 2, 4, 'Header_003', 'some text 003');
INSERT INTO articles (magazines_id,article_type_id,author_id, headers, texts) VALUES(1, 2, 1, 'Header_004', 'some text 004');
