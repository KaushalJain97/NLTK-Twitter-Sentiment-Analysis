from flask import Flask,render_template,request,jsonify
import tweepy
from textblob import TextBlob


#---------------------------------------------------------------------------

consumer_key = 'e8xNVgg3k7xxA6a1DjXSLLP9s'
consumer_secret = 'GtX4ALJDWl0mXgLmfPwcxfIkpmbtFuATmkEUXZZOUnl8pOf4mg'

access_token = '743702152917323777-6yBhnFYvMd7C0IBidlMzbNuxmBlu6Cm'
access_token_secret = 'g7bg9JAYt1TTcQjv0lK0Blj43JTRgGSuLFusA6IfZHpap'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    # t = [[]]
    t = []
    tweets = api.search(search_tweet, tweet_mode='extended')
    for tweet in tweets:
        polarity = TextBlob(tweet.full_text).sentiment.polarity
        subjectivity = TextBlob(tweet.full_text).sentiment.subjectivity
        t.append([tweet.full_text,polarity,subjectivity])
        # t.append(tweet.full_text)

    return jsonify({"success":True,"tweets":t})


#---------------------------------------------------------------------------


