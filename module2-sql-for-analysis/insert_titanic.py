import psycopg2
import pandas as pd
import sqlite3

dbname = 'gsoxmjye'
user = 'gsoxmjye'
password = 'd8YqLr3bwSFgTZC2kQ2RntVQV6Cc6VFQ'
host = 'rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname= dbname, user= user, password= password, host=host)
pg_curs = pg_conn.cursor()


df = pd.read_csv('https://raw.githubusercontent.com/dylan0stewart/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv')

df.rename(columns={'Siblings/Spouses Aboard':'Siblings_Spouses_Aboard',
                          'Parents/Children Aboard':'Parents_Children_Aboard',}, 
                 inplace=True)

create_table = '''
    CREATE TABLE titanic_table1 (
        Survived int,
        Pclass int,
        Name text,
        Sex text,
        Age int,
        Siblings_Spouses_Aboard int,
        Parents_Children_Aboard int,
        Fare float
    );
'''
#pg_curs.execute(create_table)
#pg_conn.commit()

for index, r in df.iterrows():
    insert_item = f'''INSERT INTO titanic_table1 VALUES{
    r.Survived, r.Pclass, r.Name, r.Sex, r.Age, r.Siblings_Spouses_Aboard, r.Parents_Children_Aboard, r.Fare};
    '''

pg_curs.execute(insert_item)
