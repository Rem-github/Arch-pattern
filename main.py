from framework.wsgi import Framework
from framework.urls import Url
from framework.view import View
from framework.rend import render

class IndexView(View):

    def get(self, request):
        return [b'Get query']
            # render('index.html')

    def post(self, request):
        return [b'Post query']

urls = [
    Url('/index', IndexView)
]
app = Framework(urls)
