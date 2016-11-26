# Relationship Manager

### Synopsis

Relationship Manager helps users nurture the most important relationships in their lives. Have you ever been a situation where you lost touch with a friend after you transitioned to a new job or to a new city? What about with former coworkers or bosses? Are you as close with them as you would like? Some relationships are too important or too valuable for us to afford losing, yet, many of us do not actively set aside time to remind ourselves to reach out to that person.

Similarly, when was the last time that you were at a networking event or a company party where you couldn't remember a particular fact about someone or didn't have anything to talk about with that important someone? It's good practice to keep track of the likes, dislikes, goals, preferences, etc. about every meaningful person, and that's best accomplished when documented immediately. That's where my app comes in handy. Record observations. Imagine how much more impactful your follow-ups would be if you could accurately recall the details shared in your last interaction with that person. 
 
### Features

 - To get started, users add their closest circle, then categorize each contact by 'Friend,' 'Family' or 'Professional.' A datetime algorithm captures the time that a contact was added, and schedules an event with a tip on how to reach out. The algorithm was created using the Arrow library.
 - Users have the option of signing up using their Facebook account. The JavaScript SDK was used for the OAuth.
 - Receive email notifications about people you haven't talked to in a while.
 - Store a variety of info on each contact.

#### Notifications
 
Emails are sent to the user using Python's SMTP library. Depending on the type of contact, the scheduled frequency of tips and events will vary - quarterly for professional contacts and monthly for friends and family. The Schedule API acts as a cron job, querying the database hourly to see what which events had most recently passed, and sending emails for those events. A notification for a mentor (professional contact), for example, would look like: "Rachel, it's been three months since your last meeting with your mentor, Jane Doe. Send her a quick email to see how she's doing! She would love to hear from you." Reminders about a contact who is a friend would suggest: "Hey Rachel! Jessica has been wondering about you. Take time to grab dinner with her this week."

#### Database

The relational PostgreSQL database was used to store information and SQLAlchemy was used for the queries. Object-oriented programming was used to structure the schema of the model. 


### Install Instructions

1. Create a copy of the project on your local machine.

```python
$ git clone https://github.com/yfalcon8/relationship_manager_project```

2. Create and name a virtual environment.

```python
$ virtualenv env```

3. Download necessary programs, libraries and packages.

```python
$ pip install -r requirements.txt```

4. On line 134 in sendnotif.py, type your email address and email password in place of YOUR_EMAIL_ADDRESS and YOUR_EMAIL_PASSWORD, respectively. For obvious security reasons, I excluded my own information.

5. 





### Tech Stack
- Python
- JavaScript
- jQuery
- Object-oriented programming
- PostgreSQL
- SQL
- SQLAlchemy
- JSON
- AJAX
- Flask
- Jinja
- HTML
- CSS
- Bootstrap
- Arrow library (datetime)
- SMTP library (email)

### APIs
- Facebook OAuth API
- Schedule API

### Building the App

Check out my [blog](http://yfalcon8.wixsite.com/yuki-falcon) fore more about my journey in creating this app!

### Heroku

Check out the deployed version on [Heroku](https://yf-relationship-manager.herokuapp.com/)!
