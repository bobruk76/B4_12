import uuid
import datetime
import math

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
    height = sa.Column(sa.Float)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.Integer)
    gold_medals = sa.Column(sa.Integer)
    silver_medals = sa.Column(sa.Integer)
    bronze_medals = sa.Column(sa.Integer)
    total_medals  = sa.Column(sa.Integer)
    sport  = sa.Column(sa.Text)
    country  = sa.Column(sa.Text)

    def __repr__(self):
        return "'%s', '%s', '%s', '%s'" % (self.id, self.name, self.birthdate, self.height)

def find_by_id(id, query):
    result = [item for item in query if item.id == id]

    return result[0] if len(result) > 0 else None

def find_athelete(user, query):

    def str_to_date(date_text):
        return datetime.datetime.strptime(date_text, '%Y-%m-%d')

    def days_between_two_date(str_d1,str_d2):
        d1 = str_to_date(str_d1)
        d2 = str_to_date(str_d2)

        return (d2 - d1 if d2 > d1 else d1 - d2).days

    def difference(f1, f2):
        if f1 == None:
            f1 = 0

        if f2 == None:
            f2 = 0

        return abs(f1-f2)

    result = [[item.id, days_between_two_date(user.birthdate, item.birthdate), difference(item.height, user.height)] for item in query if item.id != user.id]
    list_result = [it[0] for it in sorted(result, key=lambda item: item[1])][:1]
    list_result += [it[0] for it in sorted(result, key=lambda item: item[2])][:1]

    return [item for item in query if item.id in list_result]

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
    query = session.query(Athelete).all()
    user_id = int(input('Введите ID спортсмена:'))
    user = find_by_id(user_id, query)
    if user is None:
        print('К сожалению такого спортсмена найти не удалось!(((')
    else:
        print('Найден следующий спортсмен: {}'.format(user))
        users = find_athelete(user, query)
        print('Ближайший по дате рождения: %s' % users[1])
        print('Ближайший по росту: %s' % users[0])




if __name__ == "__main__":
    main()