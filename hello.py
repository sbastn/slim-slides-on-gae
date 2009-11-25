from vendor import web
from vendor import textile
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
        presentations = os.listdir("./presentations")
        return render.list(presentations)

class show:
    def GET(self, path):
        name = path.split("/")[0]
        current_slide = int(path.split("/")[1])
        try:
            file = open("./presentations/" + name, "r").read()
            slides = file.split("~~")
            slide = textile.textile(slides[current_slide].strip())
        except IOError:
            slide = "the document '%s' was not found"  % name
            return render.show(name, slide, 0, 0)

        prev_slide, next_slide = self.get_next_and_previous_slides(current_slide, len(slides) - 1)

        return render.show(name=name, slide=slide ,next_slide=next_slide, prev_slide=prev_slide)

    def get_next_and_previous_slides(self, current_slide, slide_count):
        next_slide = current_slide + 1
        prev_slide = current_slide - 1
        
        if next_slide > slide_count:
            next_slide = 0

        if prev_slide < 0:
            prev_slide = slide_count

        return prev_slide, next_slide


app = web.application(urls, globals())
main = app.cgirun()
