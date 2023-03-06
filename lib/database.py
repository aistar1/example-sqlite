import argparse
import sqlite3
from pathlib import Path

class Database:
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.cursor = None

    def cursorInit(self):
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.conn.close()

    def create(self, schema):
        with open(schema, 'r') as file:
            statements = file.read()
            self.cursorInit()
            self.cursor.executescript(statements)
            self.conn.commit()
            self.cursor.close()

    def selectFromTable(self, columns, table_name, search_condition=None):
        # columns = ','.join(columns)
        self.cursorInit()
        query = self.cursor.execute(f"SELECT {columns} FROM {table_name} {search_condition}")
        rows = query.fetchall()
        self.cursor.close()
        return rows

    def insertMultipleRecords(self, recordList):
        try:
            self.cursorInit()
            sqlite_insert_query = """INSERT INTO personal_info
                            (id, name, email, joining_date, salary) 
                            VALUES (?, ?, ?, ?, ?);"""
            self.cursor.executemany(sqlite_insert_query, recordList)
            self.conn.commit()
            self.cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert multiple records into sqlite table", error)

    def updateSqliteTable(self, id, salary):
        self.cursorInit()
        sql_update_query = """Update personal_info set salary = ? where id = ?"""
        data = (salary, id)
        self.cursor.execute(sql_update_query, data)
        self.conn.commit()
        self.cursor.close()
