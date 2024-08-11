from connect import *

connection = connect_mysql(config)


class Driver:
    def __init__(self, name, team, driver_id):
        self.name = name
        self.team = team
        self.driver_id = driver_id
        self.points = []

    def get_points(self, cnx):
        if cnx and cnx.is_connected():
            cursor = cnx.cursor()
            query = "SELECT points FROM driverstandings WHERE driverId=" + self.driver_id + " AND raceId IN ('1144','1143','1142','1141','1140','1139','1138','1137','1136','1135','1134','1133','1132','1131','1130','1129','1128','1127','1126','1125','1124','1123','1122','1121')"
            cursor.execute(query)
            self.points.append(cursor.fetchall())

driver_names = [
    ('Verstappen', 'Red Bull'),
    ('Norris', 'McLaren'),
    ('Leclerc', 'Ferrari'),
    ('Sainz', 'Ferrari'),
    ('Piastri', 'McLaren'),
    ('Hamilton', 'Mercedes'),
    ('Perez', 'Red Bull'),
    ('Russell', 'Mercedes'),
    ('Alonso', 'Aston Martin'),
    ('Stroll', 'Aston Martin'),
    ('Hulkenberg', 'Haas'),
    ('Tsunoda', 'RB'),
    ('Ricciardo', 'RB'),
    ('Gasly', 'Alpine'),
    ('Magnussen', 'Haas'),
    ('Albon', 'Williams'),
    ('Ocon', 'Alpine'),
    ('Guanyu', 'Sauber'),
    ('Sargeant', 'Williams'),
    ('Bottas', 'Sauber')
]

driver_ids = ['830', '846', '844', '832', '857', '1', '815', '847', '4', '840', '807', '852', '817', '842', '825', '848', '839', '855', '858', '822']
drivers = dict(zip(driver_names, driver_ids))


def get_drivers(cnx):
    for entry in drivers.items():
        # (('Bottas', 'Sauber'), 822)
        driver = Driver(list(entry)[0][0], list(entry)[0][1], list(entry)[1])
        driver.get_points(cnx)
        print(driver.points)
