import logging
import os
import redis
import uuid

from flask import Flask, Response, abort, jsonify, request, render_template, make_response, redirect

from admin_bot import start_bot
from helpers import zashita_ot_dolboyobov


logging.basicConfig(level=logging.INFO if os.getenv("ENV") == "PRODUCTION" else logging.DEBUG,
        format='[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s', datefmt='%d-%b-%y %H:%M:%S')

r = redis.StrictRedis(host=os.environ.get("REDIS_HOST", "localhost"), 
    port=int(os.environ.get("REDIS_PORT", "6379")), db=0)

app = Flask(__name__)


@app.route('/robots.txt', methods=['GET'])
def handle_robots():
	text = """
User-agent: *
Allow: /
Disallow: /no_bots_allowed/flag.txt
	""".strip()
	return Response(text, mimetype='text/plain')


@app.route('/no_bots_allowed/flag.txt', methods=['GET'])
def handle_no_bots_flag():
	return r"Good job! <br><br> HITS{p4r53rb0t_l3ft_th3_ch4t}"


@app.route('/', methods=['GET', 'POST'])
def handle_index():
	if request.method == "GET":
		return render_template('index.html')
	else:
		k = str(uuid.uuid4())
		v = request.form["text"]
		r.hset("reports", k, v)

		logging.debug("new issue id: " + k)
		logging.debug("content: " + v)

		return render_template("submited.html", report_path="/report/" + k)


@app.route('/reports')
def handle_reports():
	query = request.args.get('query')

	if not query:
		abort(400)

	if not zashita_ot_dolboyobov(query):
		logging.warn("command is not allowed")
		abort(400)

	try:
		keys = r.execute_command(query)
	except Exception as e:
		logging.error(e)
		abort(500)

	logging.info("request completed successfully")

	reports = []
	for elem in keys:
		try:
			reports.append(elem.decode())
		except:
			reports.append(elem)

	return render_template("reports.html", reports=reports)


@app.route('/report/<string:id>')
def handle_single_report(id):
	v = r.hget("reports", id)
	return render_template("report.html", report=v.decode(), id=id)


@app.route('/admin')
def handle_admin():
	if request.cookies.get("FLAG") == r"HITS{p0w3r_0f_X55}":
		logging.debug("admin entered")
		return render_template("admin.html")
	else:
		logging.debug("redirected to /admin/login")
		return redirect("/admin/login")


@app.route('/admin/login', methods=["GET", "POST"])
def handle_login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		if request.form["username"] == "secret_admin_username":
			if request.form["password"] == "secret_admin_password":
				response = make_response(redirect('/admin'))
				response.set_cookie('FLAG', r'HITS{p0w3r_0f_X55}')
				logging.info("login ok")

				return response
			else: 
				logging.warn("wrong password")
				abort(401)
		else:
			logging.warn("wrong username")
			abort(401)


@app.route('/admin/flag')
def handle_flag():
	if not "Debian" in request.headers["User-Agent"]:
		return "Sorry, we can show it only for Debian users"
	else:
		return r"Your flag is HITS{n3v3r_g0nn4_g1v3_y0u_up_l0l}}"


@app.route('/secret_endpoint/start_admin_bot')
def handle_start_admin_bot():
	start_bot(headless=True)
	return "OK"
