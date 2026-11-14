This is the start of learning nginx.

Whatever I learn, I will note it down here so I can refer to this later and get an idea.

This is something important to be noted. I first made a mistake by replacing the existing text in the README.txt file
However I reverted that change using git restore README.txt command.

What I wanted to append was, going forward I have to note down everything that is happening in my journy of learning nginx and I thought I would do that in README.txt file but i don't want to open nano editor and do the changes so I foudn a command to make things easier.
cat >> README.txt << EOF is the command. Whatever I type after that get's appended to README.txt. After the matter I just have to type EOF. That is all.

I learned how to host static files in nginx. I have created a simple login page. Next step is to make this login page work by configuring backend logic along with database foir holding user accounts and see how nginx get's integrated into all of this. Let's see hwo that goes in the next session.

We also learned how to configure file in sites-available and activate them by creating a symbolic link to sites-enabled.

We have only created one static page, next step is to create more staticpages and lavigate them accordingly to grasp the full concept of nginx.

So I made everything a but more structured so we know what is going on. All the static files into a folder called static and all the template files into a folder called template. 

I also made a python file called app.py which holds simple logic. I already installed postgreql in wsl. So I think we are all set to make a small working webpage which accepts userdata, logs in, fetches the corret webpage and delivers it to the user. Let's see how that goes.


installed flask and used flask to build a minimal backend logic. installed postgresql as well, connected postgresql and flask in app.py application.

Now when user visits localhost and signs up by entering details those details are inserted into the database. Very basic but I had to get an idea on how everything comes together in an actual production environment.


Added a simple login logic. Now once the user's data is entered into the table user_details_ in database userinfo, the user can try to login to the website. Currently the there is no useful redirection if the login succeeds so the redirection is towards signup page. However the backend logic checks the password and confirms it. So it works.

Next, need to look into loadbalancers or  maybe Docker.

Peace
