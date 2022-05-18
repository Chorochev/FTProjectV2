#-------------------------------------------------------------------------------
DROP DATABASE IF EXISTS `bookshelf`;
CREATE DATABASE `bookshelf`;
#-------------------------------------------------------------------------------
USE `bookshelf`;
#--------------- table magazines -----------------------------------------------
CREATE TABLE `magazines` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    PRIMARY KEY(`id`)
) ENGINE=INNODB;

INSERT INTO `magazines` (`name`) VALUES('IT herald');
INSERT INTO `magazines` (`name`) VALUES('IT STORIES');
INSERT INTO `magazines` (`name`) VALUES('IT with kids');

#--------------- table article_types -------------------------------------------
CREATE TABLE `article_types` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `type` VARCHAR(50) NOT NULL,
    PRIMARY KEY(`id`)
) ENGINE=INNODB;

INSERT INTO `article_types` (`type`) VALUES('news');
INSERT INTO `article_types` (`type`) VALUES('tech');
INSERT INTO `article_types` (`type`) VALUES('entertainment');

#--------------- table author --------------------------------------------------
CREATE TABLE `author` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `author` VARCHAR(50) NOT NULL,
    PRIMARY KEY(`id`)
) ENGINE=INNODB;

INSERT INTO `author` (`author`) VALUES('Chappie');
INSERT INTO `author` (`author`) VALUES('Wall-e');
INSERT INTO `author` (`author`) VALUES('Atom');
INSERT INTO `author` (`author`) VALUES('T1000');

#--------------- table articles ------------------------------------------------
CREATE TABLE `articles` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `magazines_id` INT,
    `article_type_id` INT,
    `author_id` INT,
    PRIMARY KEY(`id`),
    FOREIGN KEY (`magazines_id`) REFERENCES `magazines`(`id`),
    FOREIGN KEY (`article_type_id`) REFERENCES `article_types`(`id`),
    FOREIGN KEY (`author_id`) REFERENCES `author`(`id`)
) ENGINE=INNODB;

INSERT INTO `articles` (`magazines_id`,`article_type_id`,`author_id`) VALUES(1, 2, 3);
INSERT INTO `articles` (`magazines_id`,`article_type_id`,`author_id`) VALUES(3, 3, 2);
INSERT INTO `articles` (`magazines_id`,`article_type_id`,`author_id`) VALUES(2, 2, 4);
INSERT INTO `articles` (`magazines_id`,`article_type_id`,`author_id`) VALUES(1, 2, 1);

#--------------- users ---------------------------------------------------------
DROP USER IF EXISTS 'alex'@'localhost';
DROP USER IF EXISTS 'alex'@'WebFT.local';

CREATE USER 'alex'@'localhost' IDENTIFIED BY '123';
GRANT ALL ON `bookshelf`.* TO 'alex'@'localhost';

CREATE USER 'alex'@'WebFT.local' IDENTIFIED BY '123';
GRANT ALL ON `bookshelf`.* TO 'alex'@'WebFT.local';