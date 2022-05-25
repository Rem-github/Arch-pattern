from framework.rend import render
from framework.wsgi import Framework
from framework.urls import Url
from framework.view import View
from framework.response import Response


class IndexView(View):

    def get(self, request):
        return Response(body='GET SUCCESS')


    def post(self, request):
        return Response(status='201 Created', body='POST SUCCESS', headers={'test': '123'})

urls = [
    Url('/index', IndexView)
]

app = Framework(urls)
