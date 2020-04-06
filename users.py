#CREATE TABLE athelete("id" integer primary key autoincrement, "age" integer,"birthdate" text,"gender" text,"height" real,"name" text,"weight" integer,"gold_medals" integer,"silver_medals" integer,"bronze_medals" integer,"total_medals" integer,"sport" text,"country" text);
#CREATE TABLE sqlite_sequence(name,seq);
#CREATE TABLE user("id" integer primary key autoincrement, "first_name" text, "last_name" text, "gender" text, "email" text, "birthdate" text, "height" real);

# импортируем модули стандартной библиотеки uuid и datetime
import uuid
import datetime

# импортируем библиотеку sqlalchemy и некоторые функции из нее
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///users.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()