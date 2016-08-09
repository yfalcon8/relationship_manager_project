-- Serial indicates an auto-incrementing integer.
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(20) NOT NULL,
    bday DATE NOT NULL
);

INSERT INTO users (first_name, last_name, email, password, bday)
VALUES ('Yuki', 'Falcon', 'yfalcon8@gmail.com', 02/27/1991)