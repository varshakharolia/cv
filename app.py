
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def HELLO_WORLD():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Rajan@1234"
app.config['MYSQL_DB'] = "school1"

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        Name = request.form['Name']
        Subject = request.form['Subject']
        Email = request.form['Email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO teacher1 (Name,Subject, Email) VALUES (%s, %s,%s)", (Name,Subject, Email))
        mysql.connection.commit()
        cur.close()
        return "success"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
