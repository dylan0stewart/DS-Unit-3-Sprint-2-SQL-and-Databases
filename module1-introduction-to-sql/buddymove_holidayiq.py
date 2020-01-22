import pandas as pd 
import sqlite3

# Import CSV file as df(dataframe)
df = pd.read_csv('buddymove_holidayiq.csv')

# Convert to Sqlite3
conn = sqlite3.connect('buddymove_holidayiq.sqlite3') # instantiate my connection
df.to_sql(name='review', con=conn, if_exists='replace') # cast df to SQL
curs = conn.cursor()

# Query 1
q1 = ''' SELECT count(*) FROM review'''
r1 = curs.execute(q1)
print('#1: ', (r1.fetchall()[0][0]))

# Query 2 - # of Users who reviewed at least 100 Nature
q2 = """ SELECT COUNT(*)
            FROM review
            WHERE Nature >= 100 AND Shopping >=100"""

r2 = curs.execute(q2)
print('#2: Users who reviewed at least 100 Nature & 100 Shopping: ', r2.fetchall()[0][0])

# Query 3 - # AVG # Reviews for each cat
q3 = """SELECT AVG(sports),  
            AVG(Religious), 
            AVG(Nature), 
            AVG(Theatre), 
            AVG(Shopping), 
            AVG(Picnic)
            FROM review"""
r3 = pd.read_sql_query(q3, conn)

print('#3: Average Number of Reviews per Category:', r3)