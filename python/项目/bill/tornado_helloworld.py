import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import time

from insert_bill import insert_bill_weixin as ibw
from insert_bill import insert_bill_zhifubao as ibz
from insert_bill import insert_bill_bankcard as ibb
from insert_bill import insert_bill_account as ibc

from insert_bill import insert_bill_ccbcredit 
from insert_bill import insert_bill_bcmcredit 
from insert_bill import insert_bill_cmbcredit 
from insert_bill import insert_bill_zhongxincredit 
from insert_bill import insert_bill_cmbccredit 
from insert_bill import insert_bill_huabei 
from insert_bill import insert_bill_baitiao 
from insert_bill import insert_bill_jiebei 
from insert_bill import insert_bill_jingdongjinrong 

from tornado.options import define, options

define("port", default=35858, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun4 = self.get_argument('noun4')
        noun5 = self.get_argument('noun5')
        noun2 = time.strftime("%Y-%m-%d", time.localtime())
        if noun1 == '1':
            ibb( date=noun2,detail=noun4,jine=noun5)
        elif noun1 == '2':
            ibz( date=noun2,detail=noun4,jine=noun5)
        elif noun1 == '3':
            ibw( date=noun2,detail=noun4,jine=noun5)
        elif noun1 == '5':
            insert_bill_ccbcredit( date=noun2,detail=noun4,jine=noun5)
        elif noun1 == '6':
            insert_bill_bcmcredit( date=noun2,detail=noun4,jine=noun5)
        elif noun1 == '7':
            insert_bill_cmbcredit( date=noun2,detail=noun4,jine=noun5)
        elif noun1 == '8':
            insert_bill_zhongxincredit( date=noun2,detail=noun4,jine=noun5)
        elif noun1 == '9':
            insert_bill_cmbccredit( date=noun2,detail=noun4,jine=noun5)
        elif noun1 == '10':
            insert_bill_huabei( date=noun2,detail=noun4,jine=noun5)
        elif noun1 == '12':
            insert_bill_baitiao( date=noun2,detail=noun4,jine=noun5)
        elif noun1 == '13':
            insert_bill_jiebei( date=noun2,detail=noun4,jine=noun5)
        elif noun1 == '13':
            insert_bill_jingdongjinrong( date=noun2,detail=noun4,jine=noun5)
        else:
            ibc( date=noun2,detail=noun4,jine=noun5)

        #self.render('poem.html', roads=noun1, wood=noun2)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler), (r'/poem', PoemPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
