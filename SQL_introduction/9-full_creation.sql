-- 9-full_creation.sql CREATE TABLE second_table(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256), score INT);INSERT INTO second_table (name, score) VALUES ('John', 10), ('Alex', 3), ('Bob', 14), ('George', 8);CREATE TABLE second_table(id INT, name VARCHAR(256), score INT);INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8);

CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT );
INSERT INTO second_table VALUES (1, 'John', 10);
INSERT INTO second_table VALUES (2, 'Alex', 3);
INSERT INTO second_table VALUES (3, 'Bob', 14);
INSERT INTO second_table VALUES (4, 'George', 8);
