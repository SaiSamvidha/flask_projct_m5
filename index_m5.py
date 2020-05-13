from flask import *
import mysql.connector
import os
import csv
app=Flask(__name__)#object creation for flask
myconn=mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="college"
	)

@app.route("/")#index page or first page 
@app.route("/home")
def home():
	return render_template("index.html",name="samvidha")


@app.route("/register",methods=['GET','POST'])
def register():
	if request.method == "POST":
		rollno=request.form['rollno']
		name=request.form['name']
		email=request.form['email']
		phno=request.form['phno']
		college=request.form['college']
		branch=request.form['branch']
		section=request.form['section']
		gen=request.form['gender']
		lan=request.form.getlist('lan')
		lan=','.join(lan)
		mycur=myconn.cursor()
		mycur.execute("select * from student where rollno=%s"%(rollno))
		data=mycur.fetchall()
		
		if len(data)==0:
			mycur.execute("""insert into student(rollno,name,
				college,branch,section,email,phno,gender,languages)
				values(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
				(rollno,name,college,branch,section,email,phno,gen,lan))

			myconn.commit()
		else:
			print("already inserted")
		return redirect(url_for('register'))

	else:
		return render_template("about.html")
	








#last lines
if __name__=="__main__":
	app.run(debug=True)



