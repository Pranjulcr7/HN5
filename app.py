from flask import Flask, request, jsonify, make_response
import textblob as tb
$ pip install TextBlob

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
	text = 'awesome'
	anal = tb.TextBlob(text)
	sent = anal.sentiment
	data = {'sentiment':sent[0]}
	r = make_response( jsonify( data), 20)
	return r


if __name__ == "__main__":
    app.run(port=2000, debug=True)
