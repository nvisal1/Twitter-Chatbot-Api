from flask import Flask, jsonify, request
from interactor import buildTweetQuery
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/actors')
@cross_origin()
def fetchTweets():
    text = request.args.get('text')
    if text is None:
        return jsonify({"Error": "Bad Request"}), 400
    else:
        tweets = buildTweetQuery(text);
        if tweets is None:
            return jsonify({"Error": "Not Found"}), 404
        else:
            return jsonify({"tweets": map(convertToJson, tweets)}), 200

def convertToJson(tweet):
    return tweet._json

if __name__ == '__main__':
  app.run(debug=True)