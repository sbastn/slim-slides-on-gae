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
        presentations = []
        for root, dirs, files in os.walk("presentations"):
            presentations.append([root.replace("presentations", ""), files])

        return render.list(presentations)

class show:
    def GET(self, path):
        current_slide = int(path.split("/")[len(path.split("/")) - 1])
        list_path = path.split("/")[0:len(path.split("/")) - 1]
        file_path = "/".join(list_path)
        try:
            file = open("presentations/" + file_path, "r").read()
            slides = file.split("~~")
            slide = textile.textile(slides[current_slide].strip())
        except IOError:
            slide = "the document '%s' was not found"  % path
            return render.show(path, slide, 0, 0)

        prev_slide, next_slide = self.get_next_and_previous_slides(current_slide, len(slides) - 1)

        return render.show(name=file_path, slide=slide ,next_slide=next_slide, prev_slide=prev_slide)

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
