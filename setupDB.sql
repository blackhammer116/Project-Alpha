-- Create the database
CREATE DATABASE IF NOT EXISTS fullstack;

-- Create the user with a password
CREATE USER IF NOT EXISTS 'username'@'localhost' IDENTIFIED BY 'password';

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON fullstack.* TO 'username'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

