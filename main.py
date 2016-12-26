from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3#,db

app = Flask(__name__)


@app.route('/')
def home():
   return render_template('home.html')



@app.route('/enternew')
def new_student():
   return render_template('student.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            sid=request.form['sid']
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO info (sid,name,addr,city,pin) VALUES(?,?, ?, ?, ?)",(sid,nm,addr,city,pin) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from info")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)


@app.route('/find_rec')
def find_rec():
   return render_template('find.html')

@app.route('/update_db', methods=['POST', 'GET'])
def update_db():


    sid = request.form['sid']
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    if(request.form['sbtn']=='find'):
        cur.execute("select * from info where sid='"+sid+"'")
        rows = cur.fetchall();
        return render_template("update_db.html", rows=rows)

    elif(request.form['sbtn']=='delete'):
        cur.execute("DELETE FROM info WHERE sid=?", (sid,))
        con.commit()
        con.close
        return render_template("result.html",msg="Record Deleted.")

@app.route('/update_info', methods=['POST', 'GET'])
def update_info():
    if request.method == 'POST':
        try:
            sid=request.form['sid']
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("UPDATE info  SET name='"+nm+"',addr='"+addr+"',city='"+city+"',pin='"+pin+"' where sid='"+sid+"'")

                con.commit()
                msg = "Record successfully Updated"
        except:
            con.rollback()
            msg = "error in update operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()




if __name__ == '__main__':
    app.run()
