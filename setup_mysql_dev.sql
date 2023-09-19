-- this scripted prepared the MySQL server for this project:
-- A database hbnb_test_db, A new user hbnb_test (in localhost)
-- these password for hbnb_test was be setted to hbnb_test_pwd
-- hbnb_test has all the privilegs on the database
-- hbnb_test had SELECTED privilegea on the database
-- hbnb_test_db or the user hbnb_test already exists, your script






CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO hbnb_dev@localhost;
GRANT SELECT ON performance_schema . * TO hbnb_dev@localhost;
FLUSH PRIVILEGES;
