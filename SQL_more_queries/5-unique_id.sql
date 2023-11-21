-- 5-unique_id.sql

CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1, name VARCHAR(256), UNIQUE KEY unique_id (id));
