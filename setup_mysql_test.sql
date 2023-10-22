-- Script that prepares a MySQL server for the project:
-- A database  hbnb_test_db
-- A new user hbnb_test
-- The password of hbnb_test should be set to hbnb_test_pwd
-- Grant all privileges on the database hbnb_test_db for hbnb_test
-- Grant SELECT privilege on the database performance_schema for hbnb_test

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost;
SET PASSWORD FOR hbnb_test@localhost = 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
FLUSH PRIVILEGES;
