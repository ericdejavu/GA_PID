import json,MySQLdb


class DataRecord:
    def __init__(self,dna):
        self.columns = dna.keys()
        with open('private/mysql.json') as f:
            json.dump(sqli,f)
        self.db = MySQLdb.connect(sqli['host'],sqli['user'],sqli['passwd'],sqli['db'],charset=sqli['charset'])
        self.cursor = db.cursor()
        create_table_body = ', '.join([column + COLUMN_TYPE for column in columns])
        create_table_sql = CREATE_TABLE_FH + create_table_body[:-2] + CREATE_TABLE_END
        self.cursor.execute(create_table_sql)

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
