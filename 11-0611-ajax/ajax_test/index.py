#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado.options import define, options
import os
import random

define('port', default=9000, help='run port', type=int)


# 主函数
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<h1>hello world</h1>')


# form 请求视图
class RegHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Reg的get返回')
        # # 用户名
        # username = self.get_argument('uName')
        # # 密码
        # password = self.get_argument('password')
        # print('用户名', username, '密码', password)

    def post(self):
        # 用户名
        username = self.get_argument('uName')
        # 密码
        password = self.get_argument('password')
        # 性别
        gender = self.get_argument('gender')
        # 爱好
        hobby = self.get_arguments('hobby')
        # 地址
        address = self.get_arguments('address')
        # 个人简介
        personal = self.get_argument('personal')
        print('用户名', username, '密码', password)
        print('性别', gender, '爱好', hobby)
        print('地址', address, '个人简介', personal)


# Ajax 请求视图
class AjaxHandler(tornado.web.RequestHandler):
    # get 请求
    def get(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        print(username, password)

    # post 请求
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')
        # 后台逻辑判断
        if username and password:
            print('post', username)
            print('post', password)
        else:
            # 如果没有用户名和密码 就返回提示消息
            self.write('用户名或密码不能为空')


# 数据视图
class DataHandler(tornado.web.RequestHandler):
    def get(self):
        articles = []
        for i in range(5):
            article = {}
            article['title'] = 'title' + str(random.randint(100, 1000))
            articles.append(article)
        self.write({'articles': articles})


application = tornado.web.Application(
    handlers=[
        (r'/', MainHandler),
        # reg 路由
        (r'/reg', RegHandler),
        # ajax 路由
        (r'/ajax', AjaxHandler),
        # 返回数据的路由
        (r'/data', DataHandler),
    ],
    # 设置静态路径
    static_path= os.path.join(os.path.dirname(__file__), "static"),
    # 设置模板文件
    # template_path = os.path.join(os.path.dirname(__file__), "template"),
    # 开启debug模式
    debug=True
)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    print('端口是', options.port)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
