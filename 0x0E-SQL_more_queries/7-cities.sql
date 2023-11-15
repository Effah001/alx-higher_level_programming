-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                              state_id INT NOT NULL,
                                              name VARCHAR(256)
                                              FOREIGN KEY(state_id) REFERENCES states(id));
