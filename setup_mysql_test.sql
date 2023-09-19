-- this scripted prepared the MySQL server for this project:
-- A database hbnb_test_db, A new user hbnb_test (in localhost)
-- these password for hbnb_test was be setted to hbnb_test_pwd
-- hbnb_test has all the privilegs on the database
-- hbnb_test had SELECTED privilegea on the database
-- hbnb_test_db or the user hbnb_test already exists, your script

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
FLUSH PRIVILEGES;
