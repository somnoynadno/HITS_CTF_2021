import os

from server import app, r


if __name__ == "__main__":
	r.ping() # healthcheck
	r.set("flag", r"HITS{pl3453_d0_n0t_try_t0_r3wr1t3_m3}")

	debug = False if os.getenv("ENV") == "PRODUCTION" else True
	app.run(host="0.0.0.0", port=8000, debug=debug)