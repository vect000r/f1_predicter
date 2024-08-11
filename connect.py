import mysql.connector

with open("password.txt", 'r') as f:
    password = f.read()
    config = {
        'user': 'root',
        'password': f'{password}',
        'host': '127.0.0.1',
        'database': 'f1'
    }


def connect_mysql(config, attempts=0):
    while attempts <= 3:
        try:
            cnx = mysql.connector.connect(**config)
            return cnx
        except mysql.connector.Error as err:
            print('Failed connecting to MySQL server', err)
            attempts += 1
            if attempts == 3:
                cnx.close()