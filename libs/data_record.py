# -*- coding:utf-8 -*-
import json,MySQLdb

# data is important so no deletetion and update
class DataRecord:
    def __init__(self,dna):
        self.columns = dna.keys()
        with open('private/mysql.json') as f:
            json.dump(sqli,f)
        self.db = MySQLdb.connect(sqli['host'],sqli['user'],sqli['passwd'],sqli['db'],charset=sqli['charset'])
        self.cursor = db.cursor()
        create_table_body = ', '.join([column + COLUMN_TYPE for column in columns])
        create_table_sql = CREATE_TABLE_FH + create_table_body + CREATE_TABLE_END
        self.cursor.execute(create_table_sql)
        self.db.commit()
        self.cursor.execute(TABLE_STRUCTURE)
        columns = self.cursor.fetch()
        add_columns = set(self.columns) - set(columns)
        for column in add_columns:
            alter_table = ALTER_TABLE_HEAD + '(' + column + COLUMN_TYPE + ');'
            self.cursor.execute(alter_table)
            self.db.commit()


    def __del__(self):
        self.db.close()

    def save(self,dna):
        try:
            save_body_keys = ', '.join([column for column in self.columns])[:-2]
            save_body_values = ', '.join([str(value) for dna[column] in self.columns])[:-2]
            insert_sql = INSERT_HEAD+'('+save_body_keys+INSERT_MID+'('+save_body_values+INSERT_END
            self.cursor.execute(insert_sql)
            self.db.commit()
        except:
            print '[-] db is not init'
