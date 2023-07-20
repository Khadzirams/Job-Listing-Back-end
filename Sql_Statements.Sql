--Creating job_lisiting Table
CREATE TABLE job_lisiting(
id SERIAL PRIMARY KEY,
job_title VARCHAR (40) NOT NULL,
address VARCHAR (40)   NOT NULL,
about_company VARCHAR (1000) NOT NULL,
employement VARCHAR (100) NOT NULL,
roles_responsibilities VARCHAR(3000) NOT NULL,
qualification VARCHAR (100) NOT NULL,
experience VARCHAR (100)
);