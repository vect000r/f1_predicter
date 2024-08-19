from connect import *


class Constructor:
    def __init__(self, name, constructor_id):
        self.name = name
        self.constructor_id = constructor_id
        self.points = []

    def get_constructor_points(self, cnx):
        if cnx and cnx.is_connected():
            cursor = cnx.cursor()
            query = "SELECT points FROM constructorstandings WHERE constructorId=" + self.constructor_id + " AND raceId IN ('1144','1143','1142','1141','1140','1139','1138','1137','1136','1135','1134','1133','1132','1131','1130','1129','1128','1127','1126','1125','1124','1123','1122','1121')"
            cursor.execute(query)
            self.points.append(cursor.fetchall())


constructor_names = ['Red Bull', 'Mercedes', 'Ferrari', 'McLaren', 'Aston Martin', 'RB', 'Williams', 'Alpine', 'Sauber', 'Haas']
constructor_ids = ['9', '131', '6', '1', '117', '215', '3', '214', '15', '210']
constructors = dict(zip(constructor_names, constructor_ids))


def get_constructors(cnx):
    constructor_data = []
    for entry in constructors.items():
        # ('Red Bull' : '9')
        constructor = Constructor(list(entry)[0], list(entry)[1])
        constructor.get_constructor_points(cnx)
        constructor_data.append(constructor.points)
    return constructor_data
