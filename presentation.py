from vendor import textile
import os

class Presentation(object):
    @staticmethod
    def get_all():
        presentations = []
        for root, dirs, files in os.walk("presentations"):
            presentations.append([root.replace("presentations", ""), files])
        return presentations

class Slide(object):
    def __init__(self, path):
        self.path = path

    def get_data(self):
        self.current_slide = int(self.path.split("/")[len(self.path.split("/")) - 1])
        self.list_path = self.path.split("/")[0:len(self.path.split("/")) - 1]
        self.name = "/".join(self.list_path)
        try:
            file = open("presentations/" + self.name, "r").read()
            slides = file.split("~~")
            self.content = textile.textile(slides[self.current_slide].strip())
        except IOError:
            slides = []
            self.content = "the document '%s' was not found"  % path
        
        self.prev_slide, self.next_slide = self.get_next_and_previous_slides(self.current_slide, len(slides) - 1)

        return self

    def get_next_and_previous_slides(self, current_slide, slide_count):
        next_slide = current_slide + 1
        prev_slide = current_slide - 1
        
        if next_slide > slide_count:
            next_slide = 0

        if prev_slide < 0:
            prev_slide = slide_count

        return prev_slide, next_slide
    

