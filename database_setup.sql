-- Create the database and start working on the momo_sms_db database

CREATE DATABASE IF NOT EXISTS momo_sms_db;
USE momo_sms_db;

-- Create a users table to record users information
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_type VARCHAR(50) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    number VARCHAR(50)
);

-- Create a table to store information about categories
CREATE TABLE IF NOT EXISTS transaction_categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name ENUM('transfer', 'deposit', 'payment'),
    category_description VARCHAR(155)
);

-- Create a table to store information about fee bands
CREATE TABLE IF NOT EXISTS fee_bands (
    band_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    min_amount INT,
    max_amount INT,
    fee INT
);

-- Add foreign key constraint to the category_id column in the fee_bands table
ALTER TABLE fee_bands
ADD CONSTRAINT fk_category_id
FOREIGN KEY (category_id)
REFERENCES transaction_categories(category_id);

-- Create a table to store transaction information
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    sender_id INT,
    receiver_id INT,
    amount INT,
    fee INT,
    balance_after INT,
    transaction_date_time DATETIME
);

-- Add foreign key constraint to the category_id column in the transactions table
ALTER TABLE transactions
ADD CONSTRAINT fk_category_id_3
FOREIGN KEY (category_id)
REFERENCES transactions_categories(category_id);

-- Add foreign key constraint to the sender_id column in the transactions table
ALTER TABLE transactions
ADD CONSTRAINT fk_sender_id
FOREIGN KEY (sender_id)
REFERENCES users(user_id);

-- Add foreign key constraint to the receiver_id column in the transactions table
ALTER TABLE transactions
ADD CONSTRAINT fk_receiver_id
FOREIGN KEY (receiver_id)
REFERENCES users(user_id);

-- Create a table to store system log information
CREATE TABLE IF NOT EXISTS system_logs(
    log_id VARCHAR(50) PRIMARY KEY,
    user_id INT,
    log_type VARCHAR(50),
    log_action VARCHAR(50),
    log_timestamp DATETIME,
    details VARCHAR(155)
);

-- Add foreign key constraint to the user_id column in the system_logs table
ALTER TABLE system_logs
ADD CONSTRAINT fk_user_id
FOREIGN KEY (user_id)
REFERENCES users(user_id);

-- Add records to the users table and display the entire table
INSERT INTO users (user_type, first_name, last_name, number) VALUES ("phone_number", "Rowan", "Hongo", "0123456789"), ("bank account", "Iradukunda", "Eloi", "167182928"), ("momo code", "Erick", "Kanja", "48045"), ("phone_number", "Leila", "Omol", "0723456119"), ("momo code", "Njenga", "Waruhiu", "48036");
SELECT * FROM users;

-- Add records to the transaction categories table and display the entire table
INSERT INTO transaction_categories (category_name, category_description) VALUES ("transfer", "sender account to another phone or bank account"), ("deposit", "another account to receiver account"), ("payment", "sender account to momo code");
SELECT * FROM transaction_categories;

-- Add records to the transaction categories table and display the entire table
INSERT INTO fee_bands (category_id, min_amount, max_amount, fee) VALUES ("1", "1", "1000", "20"), ("1", "1001", "10000", "100"),("1", "10001", "150000", "250"),("1", "150001", "2000000", "1500"),("1", "2000001", "5000000", "3000"),("1", "5000001", "10000000", "5000");
SELECT * FROM fee_bands;

-- Add records to the transactions table and display the entire table
INSERT INTO transactions (category_id, sender_id, receiver_id, amount, fee, balance_after, transaction_date_time) VALUES (1, 1, 4, 10000, 100, 13000,"2025-06-25T19:50:55+02:00"), (3, 4, 3, 20000, 0, 500,"2025-06-25T19:50:55+02:00"), (2, 4, 2, 10000, 100, 15500,"2025-06-25T19:50:55+02:00"), (1, 4, 2, 10000, 100, 70,"2025-06-25T19:50:55+02:00");
SELECT * FROM transactions;

-- Add records to the system logs table and display the entire table
INSERT INTO system_logs (log_id, user_id, log_type, log_action, log_timestamp, details) VALUES ("1", 1, "error", "fixed", "2025-09-25T19:56:55+02:00", "had a user error that we had to fix");
