
import sqlite3


def connect_to_sqlite():
    print('start of connecting to db')
    connection = sqlite3.connect('my_db')
    cursor = connection.cursor()
    status = cursor.execute('''CREATE TABLE if not exists USER  (
                                            id INTEGER primary key , 
                                            Age INTEGER ,
                                            FirstName NVARCHAR(20),
                                            LastName NVARCHAR(20),
                                            Email VARCHAR(30),
                                            Phone VARCHAR(20))'''
                   )
    # connection.commit()
    # cursor.close()
    if status:
        print("talbe USER is already created")
    else:
        print("created new table USER")
    print('after creating db', status)
    cursor.close()
    connection.close()


if __name__ == "__main__":
    connect_to_sqlite()