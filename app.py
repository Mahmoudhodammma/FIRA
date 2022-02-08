import requests
import flask
from flask import *
app = Flask(__name__)
@app.route("/check/tele/")
def ue():
	User = request.args.get("User")
	re = requests.get(f"https://t.me/{User}").text
	if "tgme_username_link" in re:
		return jsonify(check=True,Telegram="@uufffuu",User=User)
	else:
		return jsonify(check=False,Telegram="@uufffuu",User=User)
if __name__ == "__main__":
	app.run()
