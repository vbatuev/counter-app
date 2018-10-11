from pymongo import MongoClient
from pymongo import errors
from time import gmtime, strftime
import flask
import os


app = flask.Flask(__name__)
mongodb_conn_string = os.getenv('MONGODB_URL')
client = MongoClient(mongodb_conn_string)
# Get database
db = client.countdb
# Get collection
collection_count = db.collection_count


def get_count():
    try:
        # Check connection
        c = client.admin.command("ismaster")
    except errors.ConnectionFailure:
        return "Server unavailable"
    else:
        # Get documents count
        count_list = collection_count.count_documents({})
        return count_list


@app.route("/")
def home():
    count_dict = {"date": strftime("%Y-%m-%d %H:%M:%S", gmtime())}
    counts = get_count()
    collection_count.insert_one(count_dict)
    return flask.render_template('index.html', counts=counts)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
