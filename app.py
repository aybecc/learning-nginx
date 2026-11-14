from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app_1 = Flask(__name__)

#connect to database



@app_1.route("/login", methods=["GET", "POST"])

def validate_data_():
    if request.method == "POST":
        userEmail = request.form.get("email")
        userPassword = request.form.get("password")
        stored_password = validation_config(userEmail)
        if userPassword == stored_password:
            print ("Login Successful")
        else:
            print ("Wrong Password")
        return redirect(url_for("get_data_"))
    return render_template("welcome.html")

@app_1.route("/signup", methods=["GET", "POST"])
def get_data_():

    if request.method == "POST":
        uName = request.form.get("name")
        uEmail = request.form.get("email")
        uPassword = request.form.get("password")
        write_data_(uName, uEmail, uPassword)
        print ("Recieved:", uName, uEmail, uPassword)
        return redirect(url_for("get_data_"))
    return render_template("welcome.html")
        
def write_data_(form_name, form_email, form_password):
    conn = psycopg2.connect(database="userinfo", user="site_admin", password="test1234", host="localhost", port="5432")

    #create cursor

    cur = conn.cursor()

    cur.execute(
        "insert into user_details_ (name_, email_, password) values (%s, %s, %s)", (form_name, form_email, form_password)
    )
    conn.commit()
    
    cur.close()
    conn.close()
    return


def validation_config(form_user_email):
    conn = psycopg2.connect(database="userinfo", user="site_admin", password="test1234", host="localhost", port="5432")

    cur = conn.cursor()

    cur.execute(
        "select password from user_details_ where email_= (%s)", (form_user_email,)
    )
    result = cur.fetchone()
    if result:
        stored_password = result[0]
    else:
        stored_password = None

    cur.close()
    conn.close()
    return stored_password

if __name__ == "__main__":
    app_1.run()
