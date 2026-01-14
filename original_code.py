import mysql.connector

db_config = {
    'user': 'root',
    'password': '66666666',
    'host': 'localhost',
    'database': 'fish'
}

def get_db_connection():
    """原项目中的数据库连接函数"""
    conn = mysql.connector.connect(**db_config)
    return conn

def get_ponds_old():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, name FROM ponds")
        ponds = cursor.fetchall()
        return ponds
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()