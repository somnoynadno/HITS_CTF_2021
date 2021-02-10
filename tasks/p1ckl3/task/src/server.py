#!/usr/bin/env python3

import logging
import os
import tornado.ioloop
import tornado.web

from tornado.options import parse_command_line

from core import make_pickle, load_user

PORT = 8000


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/index.html')


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/login.html')

    def post(self):
        p = self.request.files['pickle'][0]['body']
        logging.info(p)

        user = load_user(p)
        self.set_cookie("auth", "1")

        self.render('templates/login_ok.html', username=user.username)


class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('templates/register.html')

    def post(self):
        username = self.get_body_argument('username', default=None, strip=True)
        password = self.get_body_argument('password', default=None, strip=True)

        logging.info(username)

        path = "tmp/" + make_pickle(username, password)

        self.render('templates/register_ok.html', path=path)


class PlaygroundHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_cookie("auth"):
            self.write("Нет-нет! Сначала нужно залогиниться.")
        else:
            self.render('templates/playground.html')


def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': 'templates/js'}),
        (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': 'templates/css'}),
        (r'/img/(.*)', tornado.web.StaticFileHandler, {'path': 'templates/img'}),
        (r'/sound/(.*)', tornado.web.StaticFileHandler, {'path': 'templates/sound'}),
        (r'/tmp/(.*)', tornado.web.StaticFileHandler, {'path': 'tmp'}),
        (r"/login", LoginHandler),
        (r"/register", RegisterHandler),
        (r"/play", PlaygroundHandler),
    ], autoreload=False, debug=True, compiled_template_cache=False, serve_traceback=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    tornado.options.parse_command_line()

    logging.info("Listening on " + str(PORT))
    tornado.ioloop.IOLoop.current().start()
