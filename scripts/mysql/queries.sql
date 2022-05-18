show databases;

use `mysql`;
show tables;
# show users
SELECT `user`, `host`, `Grant_priv` FROM `mysql`.`user`;

# show columns
SELECT COLUMN_NAME
  FROM information_schema.COLUMNS
 WHERE TABLE_SCHEMA = 'mysql' AND TABLE_NAME = 'user';

#------------------- bookshelf -------------------------------------------------
use bookshelf;
SELECT m.name as 'magazine', t.type as 'article type', a.author as 'author'
  FROM articles as ar INNER JOIN magazines as m ON ar.magazines_id = m.id
                      INNER JOIN article_types as t ON ar.article_type_id = t.id
                      INNER JOIN author as a ON ar.author_id = a.id 
LIMIT 100;                      
