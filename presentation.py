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
        self.current_slide = self.current_slide_from_path(self.path)
        self.name = "/".join(self.extract_name_from_path(self.path))
        try:
            file = open("presentations/" + self.name, "r").read()
            slides = file.split("~~")
            self.content = textile.textile(slides[self.current_slide].strip())
        except IOError:
            slides = []
            self.content = "the document '%s' was not found"  % path
        
        self.prev_slide = self.get_prev_slide(self.current_slide, len(slides) - 1)
        self.next_slide = Slide.get_next_slide(self.current_slide, len(slides) - 1)

        return self

    def current_slide_from_path(self, path):
        return int(path.split("/")[len(path.split("/")) - 1])

    def extract_name_from_path(self, path):
        return path.split("/")[0:len(path.split("/")) - 1]

    @staticmethod
    def get_next_slide(current_slide, slide_count):
        if current_slide + 1 > slide_count:
            next_slide = 0
        else:
            next_slide = current_slide + 1
        return next_slide

    def get_prev_slide(self, current_slide, slide_count):
        if current_slide - 1 < 0:
            prev_slide = slide_count
        else:
            prev_slide = current_slide - 1
        return prev_slide
    

