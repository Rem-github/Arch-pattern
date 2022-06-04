from framework.rend import render
from framework.wsgi import Framework
from framework.urls import Url
from framework.view import View
from framework.response import Response



class IndexView(View):

    def get(self, request):
        return '200 OK', render('templates/index.html', title='Main page', body='Главная страница'), \
               [('Content-Type', 'text/html')]


    def post(self, request):
        return 'POST SUCCESS'

class AboutView(View):

    def get(self, request):
        return '200 OK', render('templates/index.html', title='About page', body='About page'), [('Content-Type', 'text/html')]


    def post(self, request):
        return 'POST SUCCESS'

class ContactsView(View):

    def get(self, request):
        return '200 OK', render('templates/contacts.html', title='Contacts page', body='Контакты'), \
               [('Content-Type', 'text/html')]


    def post(self, request):
        return '200 OK', render('templates/contacts.html', title='Contacts page', body='Контакты', data=request.data), \
               [('Content-Type', 'text/html')]


urls = [
    Url('', IndexView),
    Url('index', IndexView),
    Url('about', AboutView),
    Url('contacts', ContactsView),
]


app = Framework(urls)
