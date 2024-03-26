# Lee el archivo create_tables.sql, y  ejecuta comandos SQL dentro del archivo 
# y crea las tablas en la base de datos tbl_data.db

import sqlite3
import os

def execute_sql_from_file(db_file, sql_file):
    if not os.path.exists(sql_file):
        print(f"El archivo '{sql_file}' no existe.")
        return

    if not os.path.exists(db_file):
        print(f"La base de datos '{db_file}' no existe.")
        return

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        with open(sql_file, 'r') as f: 
            sql_commands = f.read().split('\n\n')

            for sql_command in sql_commands:
                if sql_command.strip():
                    cursor.execute(sql_command)
            
            conn.commit()
            print("El archivo SQL se ejecutó correctamente.")

        # Imprimir el contenido de las tablas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        for table in tables:
            table_name = table[0]
            print(f"\nTabla: {table_name}")
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            column_names = [col[1] for col in columns]
            print(" | ".join(column_names))
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    
    except sqlite3.Error as e:
        print("Error de SQLite:", e)
    finally:
        if conn:
            conn.close()

# Nombre del archivo de la base de datos SQLite
db_file = "tbl_data.db"

# Nombre del archivo SQL con las instrucciones
sql_file = "create_tables.sql"

# Ejecutar el código SQL desde el archivo
execute_sql_from_file(db_file, sql_file)



