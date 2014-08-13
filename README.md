Tweet-speak
===========

TweetSpeak is a fun project that uses javascript based Text-To-Speech engine for reading out twitter tweets. The app uses the awesome Python Flask backend to fetch tweets, python BeautifulSoup package to scrape HTML and runs behind nginx web server and uwsgi app server.

This is a simple and complete python app that runs at [http://three.lonefish.net/tweets/read/kalyan02](http://three.lonefish.net/tweets/read/kalyan02)


# Setup

### nginx

	$ sudo apt-get install nginx
	$ cp ./nginx.conf /etc/nginx/sites-available/default

### uwsgi

#### upstart init/service config

	$ sudo apt-get install uwsgi
	$ cp uwsgi-upstart.ini /etc/init/uwsgi.conf
	$ sudo service uwsgi restart
	
#### running uwsgi for testing
	
	$ uwsgi uwsgi.ini
	
### python

	$ sudo apt-get install python-dev build-essential python-pip
	$ sudo apt-get install virtualenv
	$ virtuanenv ./env
	$ pip install -r requirements.txt
