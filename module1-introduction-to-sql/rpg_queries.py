import pandas as pd
import sqlite3

# Establish Connection
conn = sqlite3.connect('rpg_db.sqlite3')

# Define cursor
curs = conn.cursor()

# r is for result, q for query
q_1 = '''SELECT count(*) FROM charactercreator_character;''' # instantiate query
r_1 = curs.execute(q_1) # instantiate result

# print result!
print('#1: Total Characters: ', (r_1.fetchall()[0][0]))
# The answer is 302!

# On to Query 2!
q_2 = '''SELECT (
                SELECT COUNT(*)
                FROM charactercreator_cleric
                ) AS 'Clerics',
                (
                SELECT COUNT(*)
                FROM charactercreator_fighter
                ) AS 'Fighters',
                (
                SELECT COUNT(*)
                FROM charactercreator_thief
                ) AS 'Thieves',
                (
                SELECT COUNT(*)
                FROM charactercreator_mage
                ) AS 'Mages',
                (
                SELECT COUNT(*)
                FROM charactercreator_necromancer
                ) AS 'Necromancers';
                '''

r_2 = curs.execute(q_2) # instantiate result for q_2
counts = r_2.fetchall() # instantiate the results
print('#2: ') # print out which query I'm answering

# create a dataframe from the results
data = [['Cleric', print(counts[0][0])], 
        ['Fighter',print(counts[0][1])], 
        ['Thief',print(counts[0][2])], 
        ['Mage', print(counts[0][3])], 
        ['Necromancer', print(counts[0][4])]]

# create dataframe of subclass/counts
subclass_count_df = pd.DataFrame(data, columns=['Subclass', 'Count'])

# show the dataframe under '#2'
subclass_count_df

# The rest of the queries are mostly similar, so I'm cutting back on the commenting

# Onto Query 3!
q_3 = '''SELECT COUNT(*)
            AS 'TOTAL ITEMS'
        FROM armory_item;'''

r_3 = curs.execute(q_3) 
print('#3: Total Items: ' , r_3.fetchall()[0][0])

# Onto the 4th Query!

q_4 = '''SELECT (
            SELECT count(*)
            FROM armory_weapon
            ) AS 'Total Weapon',
            (
            SELECT COUNT(item_id)
            FROM armory_item
            WHERE item_id NOT IN (SELECT item_ptr_id FROM armory_weapon)
            ) AS 'Non-Weapons';'''

r_4 = curs.execute(q_4)
print('#4: Total Weapons/Non Weapons: ', r_4.fetchall()[0])

# Query the 5th

q_5 = """SELECT COUNT(item_id) AS 'Item Count'
            FROM charactercreator_character_inventory
            GROUP BY character_id
            LIMIT 20"""

r_5 = curs.execute(q_5)
print('#5: Items per Character: ', r_5.fetchall())

q_6 = """SELECT COUNT(item_id) AS 'Item Count'
            FROM charactercreator_character_inventory
            WHERE item_id IN (SELECT item_ptr_id FROM armory_weapon)
            GROUP BY character_id
            LIMIT 20"""

r_6 = curs.execute(q_6)
print('#6: Weapons per Character: ', r_6.fetchall())

# Query 7

q_7 = """SELECT ROUND(1.0 * COUNT(item_id) / 
                        COUNT( DISTINCT character_id), 2) 
                  AS 'Avg. Items/Character'   
           FROM charactercreator_character_inventory"""

r_7 = curs.execute(q_7)
print('#7: Average Items per Character: ', r_7.fetchall()[0][0])

# Query 8: The Ocho

q_8 = """SELECT ROUND(AVG(item_counts),2) AS 'Avg. Weapons Per Character'
           FROM (SELECT count(inventory.item_id) as item_counts
            from charactercreator_character_inventory as inventory
            INNER JOIN armory_weapon
            ON inventory.item_id = armory_weapon.item_ptr_id
            GROUP BY inventory.character_id)"""

r_8 = curs.execute(q_8)
print('#8: Average Weapons per Character: ', r_8.fetchall()[0][0])