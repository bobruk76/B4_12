import uuid
import datetime

# импортируем библиотеку sqlalchemy и некоторые функции из нее
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# константа, указывающая способ соединения с базой данных
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
# базовый класс моделей таблиц
Base = declarative_base()

class Athelete(Base):
    """
    Описывает структуру таблицы athelete для хранения регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = 'athelete'

    # поля таблицы
    id = sa.Column(sa.Integer, primary_key=True,  autoincrement=True)
    age = sa.Column(sa.Integer)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.Integer)
    gold_medals = sa.Column(sa.Integer)
    silver_medals = sa.Column(sa.Integer)
    bronze_medals = sa.Column(sa.Integer)
    total_medals  = sa.Column(sa.Integer)
    sport  = sa.Column(sa.Text)
    country  = sa.Column(sa.Text)

def find_by_id(id, session):
    query = session.query(Athelete).filter(Athelete.id == id)

    return [item for item in query.all()]

def str_to_date(date_text):
    return datetime.datetime.strptime(date_text, '%Y-%m-%d')

def days_between_two_date(d1,d2):
    return (d2 - d1 if d2 > d1 else d1 - d2).days

def my_map(function, iterable):
    # создаем переменную для хранения результата
    result = []
    # пробегаемся по всем элементам контейнера iterable
    for item in iterable:
        # вычисляем значение функции function на текущем элементе item
        value = function(item)
        # сохраняем полученное значение
        result.append(value)
    # возвращаем полученный список
    return resul

def find_by_birthdate(date_text, cnt_ath, session):
    query = session.query(Athelete).filter(Athelete.id == id)

    return [item for item in query.all()]




def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()
    user_id = int(input('Введите ID спортсмена:'))
    users = find_by_id(user_id, session)
    if len(users) == 0:
        print('К сожалению такого спортсмена найти не удалось!(((\n')
    else:
        user = users[0]
        print('{} -- {} -- {} -- {}'.format(user.id, user.name, user.birthdate, user.height))




if __name__ == "__main__":
    main()