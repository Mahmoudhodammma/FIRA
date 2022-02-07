import requests
import flask
from flask import *
app = Flask(__name__)
@app.route("/Api/Fira/id=<id>/user=<user>/sessionid=<ses>")
def ue(id,user):
	url = "http://185.231.59.247/xfirax/"
	data = {f'inscoo':'Cookie: mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid='+ses,
 'pkx':id,
 'uname':user,
 'submit':'submit'}
	info = requests.post(url,data=data).text
	like=str(info.split('Like Coin- :')[1])
	likecoin=like.split('<br>')[0]
	follow=str(info.split('Follow Coin- :')[1])
	followcoin=follow.split('\n')[0]
	if 'Status- : ok' in info:
		de = {
	"Telegram":"@uufffuu",
	"Like Coin":likecoin,
	"Follow Coin":followcoin,
	"Status":"True"
	}
		return de
	if 'Status- : nok' in info:
		de = {
	"Telegram":"@uufffuu",
	"Like Coin":likecoin,
	"Follow Coin":followcoin,
	"Status":"False"
	}
		return de
	else:
		de = {
	"Telegram":"@uufffuu",
	"Like Coin":likecoin,
	"Follow Coin":followcoin,
	"Status":"False"
	}
		return de
if __name__ == "__main__":
	app.run(debug=True)