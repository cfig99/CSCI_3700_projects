# Import necessary libraries
from flask import Flask
from util import connect_db

# Create a Flask app
app = Flask(__name__)

# Define a route for updating basket A
@app.route('/api/update_basket_a')
def update_basket_a():
    # Establish a database connection
    conn = connect_db()
    
    # Check if the connection is an error message
    if isinstance(conn, str):
        return conn
    
    # Create a cursor for the database connection
    cur = conn.cursor()
    
    try:
        # Insert data into basket_a
        cur.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')")
        conn.commit()
        return "Success!"
    except Exception as e:
        return str(e)
    
    # Close the cursor and the database connection
    finally:
        cur.close()
        conn.close()

# Define a route for retrieving unique fruits from both baskets
@app.route('/api/unique')
def unique_fruits():
    # Establish a database connection
    conn = connect_db()
    
    # Check if the connection is an error message
    if isinstance(conn, str):
        return conn
    
    # Create a cursor for the database connection
    cur = conn.cursor()
    
    try:
        # Retrieve unique fruits from basket_a and basket_b
        cur.execute("SELECT DISTINCT fruit_a FROM basket_a")
        fruits_a = cur.fetchall()
        
        cur.execute("SELECT DISTINCT fruit_b FROM basket_b")
        fruits_b = cur.fetchall()
        
        # Create an HTML table to display the results
        table = "<table><tr><th>Unique in Basket A</th><th>Unique in Basket B</th></tr>"
        for a, b in zip(fruits_a, fruits_b):
            table += f"<tr><td>{a[0]}</td><td>{b[0]}</td></tr>"
        table += "</table>"
        return table
        
    except Exception as e:
        return str(e)
    
    # Close the cursor and the database connection
    finally:
        cur.close()
        conn.close()

# Start the Flask app in debug mode if this script is run as the main program
if __name__ == '__main__':
    app.run(debug=True)


