CREATE TABLE IF NOT EXISTS telegram_users(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  surname TEXT,
  phone TEXT UNIQUE,
  nick TEXT UNIQUE,
  bio TEXT
);


CREATE TABLE IF NOT EXISTS students(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  surname TEXT NOT NULL,
  phone TEXT UNIQUE,
  email TEXT UNIQUE,
  about TEXT
);


CREATE TABLE IF NOT EXISTS mentors(
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  surname TEXT NOT NULL,
  phone TEXT UNIQUE,
  username TEXT UNIQUE,
  bio TEXT
);


CREATE TABLE IF NOT EXISTS courses(
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT,
  price TEXT NOT NULL,
  slug TEXT UNIQUE
);


INSERT INTO telegram_users 
(id, name, surname, phone, nick, bio) 
VALUES
(1, 'Ali', NULL, '997002187', 'true2187', NULL),
(2, 'Vali', 'Aliyev', '901234567', 'vali01', 'Men Valiyman'),
(3, 'Hasan', 'Karimov', '933334455', 'hasan_dev', 'Backend dev'),
(4, 'Zafar', NULL, '998887766', 'zaf_code', NULL);


INSERT INTO students 
(id, name, surname, phone, email, about) 
VALUES
(1, 'Aziza', 'Rahimova', '901112233', 'aziza@mail.com', 'A’lochi'),
(2, 'Bekzod', 'Qodirov', '933445566', 'bekzod@mail.com', NULL),
(3, 'Dilshod', 'Tursunov', '998776655', 'dilshod@mail.com', 'Python learner'),
(4, 'Madina', 'Aliyeva', '911223344', 'madina@mail.com', NULL);


INSERT INTO mentors 
(id, name, surname, phone, username, bio) 
VALUES
(1, 'Alibek', 'Ollayorov', '900000001', 'alibek_dev', 'Python mentor'),
(2, 'Javlon', 'Karimov', '900000002', 'javlon_it', NULL),
(3, 'Nodira', 'Xasanova', '900000003', 'nodira_eng', 'English teacher'),
(4, 'Timur', 'Aliyev', '900000004', 'timur_code', 'Backend dev');


INSERT INTO courses 
(id, title, description, price, slug) 
VALUES
(1, 'Python Basic', 'Boshlang‘ich kurs', 0, 'python-basic'),
(2, 'Django Pro', 'Web development', 100, 'django-pro'),
(3, 'English B1', 'O‘rta daraja', 50, 'english-b1'),
(4, 'SQL Mastery', NULL, 80, 'sql-mastery');





