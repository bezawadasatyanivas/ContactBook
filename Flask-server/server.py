from flask import Flask, redirect
from flask import url_for,render_template
from flask import request, session, flash, jsonify
from flask_mysqldb import MySQL
from datetime import timedelta

import os
os.chdir(r'C:\Users\satya\OneDrive\Desktop\react\project1')

#create flask object

app=Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'satya'
app.config['MYSQL_DB'] = 'cm_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


mysql = MySQL(app)
#for session data, we need to put a secret key..to decrypt the encrypted data
app.secret_key="customer-manager"

#how long a session should be?
app.permanent_session_lifetime=timedelta(minutes=5)



@app.route("/")
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return str(data)
    #return render_template('home.html')


@app.route("/login" ,methods=["post","get"])
def login():
    
        data=request.get_json()
        email=data['email']
        password=data['password']
        cur=mysql.connection.cursor()
        cur.execute("select * from users where email=%s" ,(email,))
        user=cur.fetchone()#dict
        
        if user['username'] in session:
            return redirect(url_for("userop"))
        
        
        if user:
            if user['password']==password:  
                session['name']=user['username']
                session.permanent=True
                return redirect(url_for("userop",u_name=user['f_name'],u_age=user['age'],u_email=user['email'] ))#u_name=user[1],u_age=user[2],u_email=user[3]
            else:
                return jsonify({'message':'Enter corrrect email'})
        else:
            return jsonify({'message':'No user exist???'})
            
        
    
        


@app.route("/register", methods=["POST","GET"])
def register():  

        data=request.get_json()
        username=data['username']
        email=data['email']
        password=data['password']
        cur=mysql.connection.cursor()
        
        cur.execute("select * from users where email=%s" ,(email,))
        user=cur.fetchone()
        
        
        if user:
            return jsonify({'message': 'Username already exists in the database'}),400
            #return render_template('login.html')
            
        
        cur.execute("INSERT INTO users(username,email,password) VALUES ( %s, %s,%s)",(username,email,password))
        mysql.connection.commit()
        cur.close()
        
        return jsonify({'message': "Successfully Registered"}),201

    

    

# =============================================================================
# @app.route("/user") 
# def userop():
#     if "name" in session:
#         user=session['name']
#         return f'<h1>{user}</h1>'
#     
#     else:    
#         return redirect(url_for('login'))
# 
# =============================================================================


# =============================================================================
# @app.route("/user") #/<string:u_name>/<int:u_age>/<string:u_email>
# def userop():
#     if "name" in session:
#             user=session['name']
#             cur=mysql.connection.cursor()
#             cur.execute("select * from users where f_name=%s" ,(user,))
#             logged_user=cur.fetchone()
#             name=logged_user['f_name']
#             age=logged_user['age']
#             email=logged_user['email']
#             return render_template('user.html',naam=name,age=age,email=email)
#             
#     else:   
#             flash("error in login","info")
#             return render_template('login.html')
# 
# 
# 
# @app.route("/edit", methods=["POST","GET"])
# def edit():
#     if "name" in session:
#         user=session['name']
#         cur=mysql.connection.cursor()
#        
#         if request.method=="POST":
#             
#             age=request.form['age']
#             email=request.form['email']
#             print("data updated..1")
#             cur.execute("update users set email=%s,age=%s where f_name=%s" ,(email,age,user))
#             mysql.connection.commit() 
#             print("data updated")
#             cur.execute("select * from users where f_name=%s" ,(user,))
# 
#             changes_user=cur.fetchone()
#             age=changes_user['age']
#             email=changes_user['email']
#             cur.close()
#             return redirect(url_for('userop',age=age,email=email))
#         else: 
#             cur.execute("select * from users where f_name=%s" ,(user,))
#             logged_user=cur.fetchone()
#             age=logged_user['age']
#             email=logged_user['email']
#             cur.close()
#             return render_template("edit.html",naam=user,age=age,email=email)
#     else:
#         return render_template("login.html")
#           
#             
#                 
#             
#             
# # =============================================================================
# # @app.route("/savechanges", methods=['post'])
# # def savechanges():
# #     if "name" in session:
# #         if request.method=='post':
# #             user=session['name']
# #             cur=mysql.connection.cursor()
# #             cur.execute("select * from users where f_name=%s" ,(user,))
# #             logged_user=cur.fetchone()
# #             age=logged_user['age']
# #             email=logged_user['email']
# #      
# #             cur.execute("update users set email=%s,age=%s where f_name=%s" ,(email,age,user))
# #             changes_user=cur.fetchone()
# #             age=changes_user['age']
# #             email=changes_user['email']
# #             return redirect(url_for('userop'),naam=user,age=age,email=email)
# #             
# # =============================================================================
#     
# 
# @app.route("/logout")
# def logout():
#     if 'name' in session:
#             user_logout=session['name']
#             flash(f"you logged out,{user_logout}","info")
#             session.pop("name",None)
#             return redirect(url_for("login"))
#         
# @app.route("/delete")
# def delete():
#     if 'name' in session:
#             user_delete=session['name']
#             cur=mysql.connection.cursor()    
#             cur.execute("delete from users where f_name=%s" ,(user_delete,))
#             mysql.connection.commit() 
#             print("u as user got deleted:(")
#             session.pop("name",None)
#             return redirect(url_for("login"))
#     
# =============================================================================
        
    
if __name__=="__main__":
    app.run(debug=True,use_reloader=False)