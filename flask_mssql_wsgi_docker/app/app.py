from typing import List, Dict
from flask import Flask
import mysql.connector
import json
import os

app = Flask(__name__)

def favorite_colors() -> List[Dict]:
    config = {
        # this user has SELECT permissions only. If you wanted to update table entries, you would need to use the admin credentials.
        'user': os.environ['MYSQL_USER'],
        'password': os.environ['MYSQL_PASSWORD'],
        ## if you wanted to use admin , you would use this user/password combination instead.
        # 'user': 'root',
        # 'password': os.environ['MYSQL_ROOT_PASSWORD'],
        'host': 'db',
        'port': os.environ['SQLPORT'],
        'database': os.environ['MYSQL_DB']
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM ' + os.environ['MYSQL_TABLE'])
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results

@app.route('/')
def index() -> str:
    return json.dumps({'favorite_colors': favorite_colors()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ['FLASKPORT'])