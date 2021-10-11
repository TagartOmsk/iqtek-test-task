CREATE TABLE Users (
    user_id BIGINT NOT NULL UNIQUE,
    last_name VARCHAR(20) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    middle_name VARCHAR(20),
    PRIMARY KEY (user_id)
);

CREATE SEQUENCE user_id_seq START WITH 1;
