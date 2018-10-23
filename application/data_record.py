# -*- coding:utf-8 -*-
import json,MySQLdb

# data is important so no deletetion and update
class DataRecord:
    def __init__(self,dna):
        self.columns = dna.keys()
        with open('private/mysql.json') as f:
            sqli = json.loads(f)
        self.db = MySQLdb.connect(sqli['host'],sqli['user'],sqli['passwd'],sqli['db'],charset=sqli['charset'])
        self.cursor = db.cursor()
        self.update_from_json()

    def dynamic_create_table(self):
        create_table_body = ', '.join([column + COLUMN_TYPE for column in columns])
        create_table_sql = CREATE_TABLE_FH + create_table_body + CREATE_TABLE_END
        self.cursor.execute(create_table_sql)
        self.db.commit()
        self.cursor.execute(TABLE_STRUCTURE)
        columns = self.cursor.fetch()
        # columns dynamic
        add_columns = set(self.columns) - set(columns)
        for column in add_columns:
            alter_table = ALTER_TABLE_HEAD + '(' + column + COLUMN_TYPE + ');'
            self.cursor.execute(alter_table)
            self.db.commit()


    def __del__(self):
        self.db.close()

    def update_from_json(self):
        with open('config/params.json') as f:
            params = json.loads(f)
        self.project_group = params.project_group
        self.pid_group = params.pid_group
        self.sub_group_sequence = params.sub_group_sequence
        self.continue_group_sequence = params.continue_group_sequence


    def insert_id(self):
        self.db.insert_id()

    def execute(self,insert_sql):
        self.cursor.execute(insert_sql)
        self.db.commit()

    def save_origin(self,org):
        insert_sql = INSERT_ORIGIN.format(
            self.project_group,self.pid_group,
            org['kp'],org['ki'],org['kd'],MAX_OUTPUT,
        )
        self.execute(insert_sql)
        return self.insert_id()

    def save_measure(self,angles):
        insert_sql = INSERT_MEASURE.format(
            self.pid_group,self.continue_group_sequence,self.sub_group_sequence
            angles['angle'],angles['light']
        )
        self.execute(insert_sql)

    def save_analyse(self,analysis):
        insert_sql = INSERT_ANALYSE.format(
            self.pid_group,self.sub_group_sequence,
            analysis['first_react_delta_time'],
            analysis['first_response_delta_time'],
            analysis['peak'],
            analysis['stable']
        )
        self.execute(insert_sql)
        return self.insert_id()
