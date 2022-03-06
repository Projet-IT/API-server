import sqlite3

class Database:

    def __init__(self):
        self.connect()
        self.query_sql_file('table_devices')

    def connect(self):
        self.db = sqlite3.connect("data.db")
        self.cursor = self.db.cursor()

    def query_sql_file(self, script_name, single = False, *parameter):
        self.connect()
        with open('./sql_script/' + script_name + '.sql', 'r') as sql_file:
            sql_script = sql_file.read()

        if single:
            self.cursor.execute(sql_script, parameter)
            return self.cursor.fetchone()
        else:
            self.cursor.execute(sql_script)
            return self.cursor.fetchall()

    def insert_sql_file(self, script_name, *parameter):
        self.connect()
        with open('./sql_script/' + script_name + '.sql', 'r') as sql_file:
            sql_script = sql_file.read()

        self.cursor.execute(sql_script, parameter)
        self.db.commit()


    def get_devices(self):
        return self.query_sql_file('get_devices')

    def get_device_config(self, id):
        return self.query_sql_file('get_config', True, id)

    def add_device(self, name, type, sensity):
        return self.insert_sql_file('add_device', name, type, sensity)