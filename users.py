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

class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    # задаем название таблицы
    __tablename__ = 'user'

    # поля таблицы
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)

def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def valid_email(email):
    email_list = [item.split('.') for item in email.split('@')]
    return len(email_list) == 2 and len(email_list[-1]) > 1

gender_set = ('Male', 'Female', 'Other')
def valid_gender(gender):
    return gender in gender_set

def request_data():

    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    # выводим приветствие
    print("Введите данные пользователя:")
    # запрашиваем у пользователя данные
    first_name = str(input("Имя пользователя: "))
    last_name = str(input("Фамилию: "))

    gender =''
    while not valid_gender(gender):
        gender = str(input("Пол:"))
        if not valid_gender(gender):
            print('Попробуйте ввести что-то из следующего списка {}'.format(gender_set))

    email =''
    while not valid_email(email):
        email = input("Адрес электронной почты: ")
        if not valid_email(email):
            print('Неправильный формат электронной почты!')

    user_id = str(uuid.uuid4())
    # создаем нового пользователя
    user = User(
        id=user_id,
        first_name=first_name,
        last_name=last_name,
        gender = gender,
        email = email,
        birthdate = birthdate,
        height = height
    )
    # возвращаем созданного пользователя
    return user

def main():
    """
    Осуществляет взаимодействие с пользователем, обрабатывает пользовательский ввод
    """
    session = connect_db()
    print(request_data())




if __name__ == "__main__":
    main()