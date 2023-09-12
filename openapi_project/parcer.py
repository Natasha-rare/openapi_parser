import pandas as pd
import sqlite3

data = pd.read_csv('cinemas_data.csv')
# print(data.info())

conn = sqlite3.connect('cinemas_data.db')
cursor = conn.cursor()
#need to add not null parametrs
cursor.execute('''CREATE TABLE IF NOT EXISTS cinemas (
                    id INTEGER PRIMARY KEY,
                    cinema_name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    description TEXT,
                    legal_entity TEXT,
                    website TEXT,
                    category TEXT,
                    inn INTEGER)''')


for _, row in data.iterrows():
    name, address, description, ent,\
        website, category,  inn = row['Название'], row['Адрес'], row['Примечание'], \
        row['Юридическое лицо'], row['Адрес сайта'], row['Категория'], row['ИНН']
    # print(name, address, description, ent, website, category,  inn)
    cursor.execute('''INSERT INTO cinemas (cinema_name, address, description, legal_entity, website, category, inn )
                              VALUES (?, ?, ?, ? , ?, ?, ?)''', (name, address, description, ent, website, category, inn))

conn.commit()
conn.close()