from vendor import web
from presentation import Presentation
from presentation import Slide
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
        return render.list(Presentation.get_all())

class show:
    def GET(self, path):
        slide = Slide(path)
        return render.show(slide=slide.get_data())

app = web.application(urls, globals())
main = app.cgirun()
