CREATE DATABASE Hackutdx;
USE Hackutdx;
CREATE TABLE Users (
  email VARCHAR(255) NOT NULL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL
);
CREATE TABLE Chats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    messages TEXT NOT NULL ,
    transcriptions TEXT NOT NULL 
    FOREIGN KEY (email) REFERENCES Users(email)
);
    
