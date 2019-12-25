# Eventapp API v1

### API Requirements and Goals

**Functional Requirements:**

* The tool should be submitted with a pre-defined events in the data store. Events should have the following fields identified:
* An event will have a name
* An event will have a location
* An event will have a start and end time
* An event will have a unique identifier
* The tool should accept an email address as a unique identification for a user (when signing up for an event)
* The tool should allow the user to
* List all events
* Sign up for an event
* Remove email address from event
* When signing up for an event the tool should email a pre-defined email address with a notification.
* All properties (i.e. the pre-defined email address) should be easy to change before deployment.
* All event times will be in the same timezone.
* An event can span multiple days.


###  API Documentations

Postman API documentaion here :
https://documenter.getpostman.com/view/9898598/SWLZfAV5?version=latest#9312a3c6-8ae9-4bf3-b1cc-d44db9673274

![API endpoints](https://raw.githubusercontent.com/sidlinux22/eventapp-api/master/docs/Api-endpoints.png)

###  Database Design

![DB Design](https://raw.githubusercontent.com/sidlinux22/eventapp-api/master/docs/dbdesign.png)

ref : https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

### Setup locally
-------------
1.  clone repository (git clone https://github.com/sidlinux22/eventapp-api.git),
2.  install [virtualenv](https://flask.palletsprojects.com/en/1.1.x/installation/),
2.  `cd path/to/repo`,
3.  `virtualenv venv`,
4.  `. venv/bin/activate`,
5. 
~~~~
  pip3 install Flask-SQLAlchemy
  pip3 install flask_jwt
  pip3 install flask_restful
  pip3 install flask_mail
~~~~

6.  `python app.py`
7.  in your favourite web browser `localhost:5000`


## Test
1. Install Postman
https://www.getpostman.com/downloads/

2. Import Request Collection from repository postman directory

3. Collection Runner Test

![Postman](https://raw.githubusercontent.com/sidlinux22/eventapp-api/master/test/postman/postman_collection/EventappAPIv1postmapcollection.png)

