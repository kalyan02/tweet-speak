Tweet-speak
===========

TweetSpeak is a fun project that uses javascript based Text-To-Speech engine for reading out twitter tweets. 

This is a simple and complete python app that runs at [http://three.lonefish.net/tweets/read/kalyan02](http://three.lonefish.net/tweets/read/kalyan02)

### requirements

  - python-Flask 
  - python-BeautifulSoup
  - nginx
  - uwsgi


# Setup


### nginx

	$ sudo apt-get install nginx
	$ cp ./nginx.conf /etc/nginx/sites-available/default

### upstart init/service config

	$ sudo apt-get install uwsgi
	$ cp uwsgi-upstart.ini /etc/init/uwsgi.conf
	$ sudo service uwsgi restart
	
### running uwsgi for testing
	
	$ uwsgi uwsgi.ini
	
### python

	$ sudo apt-get install python-dev build-essential python-pip
	$ sudo apt-get install virtualenv
	$ virtuanenv ./env
	$ pip install -r requirements.txt
