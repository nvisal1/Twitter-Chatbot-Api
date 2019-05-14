from flask import Flask, jsonify, request
from interactor import buildTweetQuery

app = Flask(__name__)

@app.route('/actors')
def fetchTweets():
    text = request.args.get('text')
    if text is None:
        return jsonify({"Error": "Bad Request"}), 400
    else:
        tweets = buildTweetQuery(text);
        if tweets is None:
            return jsonify({"Error": "Not Found"}), 404
        else:
            return jsonify({"tweets": tweets}), 200

if __name__ == '__main__':
    app.run(debug=True)