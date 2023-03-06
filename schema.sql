CREATE TABLE personal_info (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email text NOT NULL UNIQUE,
    joining_date datetime,
    salary REAL NOT NULL);
