import sqlite3
def run(db_path: str, sql: str):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return str(result)
