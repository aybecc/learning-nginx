from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app_1 = Flask(__name__)

#connect to database



@app_1.route("/", methods=["GET", "POST"])
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

if __name__ == "__main__":
    app_1.run()