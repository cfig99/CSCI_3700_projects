from flask import Flask
from util import connect_db

app = Flask(__name__)

@app.route('/api/update_basket_a')
def update_basket_a():
    conn = connect_db()
    if isinstance(conn, str):
        return conn
    
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')")
        conn.commit()
        return "Success!"
    except Exception as e:
        return str(e)
    finally:
        cur.close()
        conn.close()

@app.route('/api/unique')
def unique_fruits():
    conn = connect_db()
    if isinstance(conn, str):
        return conn
    
    cur = conn.cursor()
    try:
        cur.execute("SELECT DISTINCT fruit_a FROM basket_a")
        fruits_a = cur.fetchall()
        
        cur.execute("SELECT DISTINCT fruit_b FROM basket_b")
        fruits_b = cur.fetchall()
        
        table = "<table><tr><th>Unique in Basket A</th><th>Unique in Basket B</th></tr>"
        for a, b in zip(fruits_a, fruits_b):
            table += f"<tr><td>{a[0]}</td><td>{b[0]}</td></tr>"
        table += "</table>"
        
        return table
    except Exception as e:
        return str(e)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)

