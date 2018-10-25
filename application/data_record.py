# -*- coding:utf-8 -*-
import json,MySQLdb
from const_str import *
import os

# data is important so no deletetion
class DataRecord:
    def __init__(self):
        self.PATH_PREFIX = ''
        if os.getcwd().find('application') < 0:
            self.PATH_PREFIX = 'application/'
        with open(self.PATH_PREFIX+'private/mysql.json') as f:
            sqli = json.loads(f.read())
        self.db = MySQLdb.connect(sqli['host'],sqli['user'],sqli['passwd'],sqli['db'])
        self.cursor = self.db.cursor()
        self.update_from_json()

    def dynamic_create_table(self, dna):
        self.columns = dna.keys()
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

    def write_update(self,params):
        with open(self.PATH_PREFIX+'config/params.json') as f:
            _params = json.loads(f.read())
        with open(self.PATH_PREFIX+'config/params.json','w') as f:
            for key in params.keys():
                if params[key] == ADD:
                    _params[key] += 1
                else:
                    _params[key] = params[key]
            json.dump(_params,f)
        self.set_dict(_params)


    def update_from_json(self):
        with open(self.PATH_PREFIX+'config/params.json') as f:
            params = json.loads(f.read())
        self.set_dict(params)


    def set_dict(self,params):
        self.project_group = params[PROJECT_GROUP]
        self.pid_group = params[PID_GROUP]
        self.sub_group_sequence = params[SUB_GROUP_SEQUENCE]
        self.continue_group_sequence = params[CONTINUE_GROUP_SEQUENCE]

    def execute(self,sql):
        self.cursor.execute(sql)

    def commit(self):
        self.db.commit()

    def insert_id(self):
        return self.cursor.lastrowid

    def save_origin(self,org):
        insert_sql = INSERT_ORIGIN.format(
            self.project_group,self.pid_group,
            str(org['kp']),str(org['ki']),str(org['kd']),
            str(MAX_OUTPUT)
        )
        self.execute(insert_sql)
        return self.insert_id()

    def save_measure(self,angles):
        insert_sql = INSERT_MEASURE.format(
            self.pid_group,self.continue_group_sequence,self.sub_group_sequence,
            str(angles['angle']),str(angles['light'])
        )
        self.execute(insert_sql)

    def save_analyse(self,analysis):
        insert_sql = INSERT_ANALYSE.format(
            self.pid_group,self.sub_group_sequence,
            analysis[FIRST_REACT_DELTA_TIME],
            analysis[FIRST_RESPONSE_DELTA_TIME],
            analysis[EXECUTABLE_SCORE],
            analysis[PEAK],
            analysis[STABLE]
        )
        self.execute(insert_sql)
        return self.insert_id()

    # alive = this data weather in population_pool
    def update_origin(self,data):
        update_sql = UPDATE_ORIGIN.format(
            data["alive"],
            data["force_break"],
            data["id"]
        )
        self.execute(update_sql)


# usage:
#
# data_record = DataRecord()
# print data_record.save_origin({"kp":10,"kd":1,"ki":2})
# data_record.save_measure({"angle":"100","light":"100"})
# data_record.save_analyse({
#     'first_react_delta_time':'10.1212',
#     'first_response_delta_time':'12.123',
#     'executable_score':'123',
#     'peak':'108',
#     'stable':'0.000115648'
# })
# data_record.update_origin({"id":1,"alive":1,"force_break":0})
