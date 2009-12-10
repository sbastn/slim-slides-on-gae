from vendor import web
from presentation import PresentationBrowser
from presentation import PresentationController
import os

urls = (
  '/', 'index',
  '/list', 'list',
  '/show/(.*)', 'show'
)

render = web.template.render('templates', base='base') 

class index:
    def GET(self):
        return render.index()

class list:
    def GET(self):
        return render.list(PresentationBrowser.get_all())

class show:
    def GET(self, path):
        controller = PresentationController()
        return render.show(slide=controller.get_slide(path))

app = web.application(urls, globals())
main = app.cgirun()
