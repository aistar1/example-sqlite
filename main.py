import argparse
import os
from lib.database import Database

def test(db):

    recordsToInsert = [(4, 'Jos', 'jos@gmail.com', '2019-01-14', 9500),
                    (5, 'Chris', 'chris@gmail.com', '2019-05-15', 7600),
                    (6, 'Jonny', 'jonny@gmail.com', '2019-03-27', 84)]

    db.insertMultipleRecords(recordsToInsert)

    result  = db.selectFromTable('name, salary, email' ,'personal_info')
    print(result)

    db.updateSqliteTable(6, 8400)
    result  = db.selectFromTable('name, salary, email' ,'personal_info')
    print(result)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', type=str, default='0000.db', help='DB file path')
    parser.add_argument('--schema', type=str, default='schema.sql', help='schema file path')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    db_file = args.db
    schema_file = args.schema

    db = Database(str(db_file))
    
    if not os.path.isfile(args.db):
        db.create(schema_file)

    test(db)
