from flask import Flask, jsonify, Response, send_from_directory, request
import jinja2
from BeautifulSoup import BeautifulSoup as BS
import urllib2
import json, os,time

# Cache a remote URL for expires timeout
def remote_cache(url,local,expires=5*60*60):
    local = local.replace('/','_').replace('_tmp_','/tmp/')

    if os.path.exists(local):
        ct = os.path.getctime(local)
        nt = time.time()
        delta = nt - ct
        if delta > expires:
            os.unlink(local)

    if os.path.exists(local):
        return open(local,'r').read()
    else:
        con = urllib2.urlopen(url).read()
        fh = open(local,'w')
        fh.write(con)
        fh.close()

    return con

app = Flask(__name__)

@app.route('/tweets/static/<path:path>')
@app.route('/static/<path:path>')
def static_stuff(path):
    print app.root_path
    return send_from_directory(app.root_path + '/static/', path)

@app.route('/tweets/read/<user>')
@app.route('/read/<user>')
def showtweets(user):
    print user, app.root_path, request.data, request
    tmpf = "/tmp/%s.txt" % (user)
    tweetcon = remote_cache( "https://twitter.com/%s" % user, tmpf )
    tweetbs = BS(tweetcon)
    tweets = tweetbs.findAll('p',attrs={'class':'ProfileTweet-text js-tweet-text u-dir'})
    tt = []

    for each in tweets:
        tt.append( each.text )

    tpl = open('template.html','r').read()
    jtpl = jinja2.Template(tpl)
    return jtpl.render({ 
        'items' : tt,
        'user' : user
        })
    
@app.route('/tweets/')
@app.route('/')
def hello_world():
    #tpl = open('index.html','r').read()
    #return tpl
    return 'Hello world! Read tweets using /tweets/read/&lt;username&gt;'

app.debug=True
if __name__ == '__main__':
    app.run(debug=True,port=9091,host='three.lonefish.net',)
