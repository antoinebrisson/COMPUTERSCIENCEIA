from flask import Flask
import mysql.connector
from views import views

# create a Flask application instance
app = Flask(__name__)

# configure the application instance
app.config["UPLOAD_FOLDER"] = "/path/to/upload/folder"

# register the views blueprint with the application instance
app.register_blueprint(views, url_prefix="/")

# start the Flask development server
if __name__ == "__main__":
    app.run(debug=True, port=8000)
