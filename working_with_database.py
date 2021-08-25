# https://gist.github.com/asqd/10c428f00119ae7beb54845ed19e30eb файлы с данными
# https://gist.github.com/asqd/be4bac6d15e638e0068dfa5f097614dc пример скрипта
#
# - Дописать функции select_query, update_query и delete_query
# - Дописать скрипт, чтобы он загрузил в базу не только заказы, но и клиентов. То есть создал таблицу clients и загрузил туда данные из csv


import sqlite3


conn = sqlite3.connect('example.db')