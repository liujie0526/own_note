import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import time

from visitor_statistics import visitor_statistics as vis

from tornado.options import define, options

define("port", default=35859, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index_test.html')


class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        noun3 = self.get_argument('noun3')


        vis(dbuser='nginx_log', dbpassword='nginx_log', dbhost='192.168.1.139', dbbame='nginx_log', dbdate1=noun1, dbdate2=noun2,
            serverid=noun3, outfilename='/usr/local/nginx/html/temp2.html')

        time.sleep(3)
        self.render('poem.html', roads=noun1, wood=noun2,wod=noun3)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/poem', PoemPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
