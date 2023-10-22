-- Script that prepares a MySQL server for the project:
-- A database  hbnb_dev_db
-- A new user hbnb_dev
-- The password of hbnb_dev should be set to hbnb_dev_pwd
-- Grant all privileges on the database hbnb_dev_db for hbnb_dev
-- Grant SELECT privilege on the database performance_schema for hbnb_dev
	
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost;
SET PASSWORD FOR hbnb_dev@localhost = 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema . * TO hbnb_dev@localhost;
FLUSH PRIVILEGES;
