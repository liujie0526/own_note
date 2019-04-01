import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import time

from billimg import billimg
from tornado.options import define, options

define("port", default=35859, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index_test.html')


class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        billimg()
        time.sleep(3)
        self.render('poem.html')


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/poem', PoemPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
