This is the start of learning nginx.

Whatever I learn, I will note it down here so I can refer to this later and get an idea.

This is something important to be noted. I first made a mistake by replacing the existing text in the README.txt file
However I reverted that change using git restore README.txt command.

What I wanted to append was, going forward I have to note down everything that is happening in my journy of learning nginx and I thought I would do that in README.txt file but i don't want to open nano editor and do the changes so I foudn a command to make things easier.
cat >> README.txt << EOF is the command. Whatever I type after that get's appended to README.txt. After the matter I just have to type EOF. That is all.

I learned how to host static files in nginx. I have created a simple login page. Next step is to make this login page work by configuring backend logic along with database foir holding user accounts and see how nginx get's integrated into all of this. Let's see hwo that goes in the next session.

We also learned how to configure file in sites-available and activate them by creating a symbolic link to sites-enabled.

We have only created one static page, next step is to create more staticpages and lavigate them accordingly to grasp the full concept of nginx.
