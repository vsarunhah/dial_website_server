import flask
from flask import Flask, json, request, jsonify
from flask_cors import cross_origin, CORS

from rss_feeds_file import get_rss_feeds
from search import all_investors, text_search, get_company_info

import helpers  # load the things
app = Flask(__name__)
CORS(app)


@app.route('/')
@cross_origin()
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/getInvestors')
@cross_origin()
def get_investors():
    return json.jsonify(all_investors())


@app.route('/search', methods=["POST"])
@cross_origin()
def get_text_search():
    body = request.json
    results = text_search(body=body)
    # print(results[0])
    response = flask.jsonify({"results": results})
    return response


@app.route('/startup_news', methods=["GET"])
@cross_origin()
def get_news():
    results = get_rss_feeds()
    return jsonify({"rss_data": results})


@app.route('/company', methods=["GET"])
@cross_origin()
def get_company():
    company = request.args.get("name")
    return jsonify(get_company_info(company))


if __name__ == '__main__':
    app.run(use_reloader=True, debug=False)
