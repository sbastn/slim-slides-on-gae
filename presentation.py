from vendor import textile
import os

class PresentationBrowser(object):
    @staticmethod
    def get_all():
        presentations = []

        for root, dirs, files in os.walk('slides'):
            presentations.append([root.replace('slides', ''), files])

        return presentations

class PresentationController(object):
    """ Coordinates the work to get a presentation based on the path
    """
    def get_slide(self, url):
        name = self.extract_name(url)
        slide_number = self.extract_slide(url)
        presentation = self.load(name)
        if len(presentation.slides) == 0:
            return self.empty_slide(name)

        return self.build_slide(presentation, slide_number)

    def extract_name(self, url):
        path = url.split('/')

        if path[-1].isdigit():
            return '/'.join(path[0:-1])
        else:
            return '/'.join(path[0:])

    def extract_slide(self, url):
        path = url.split('/')
        try:
            return int(path[-1])
        except ValueError:
            return 0

    def load(self, name):
        return Loader.load(name)

    def build_slide(self, presentation, slide_number):
        content = textile.textile(presentation.slides[slide_number].strip())
        slide = Slide(presentation.name, 
                      content,
                      self.get_prev_link(slide_number, len(presentation.slides) - 1),
                      self.get_next_link(slide_number, len(presentation.slides) - 1))
        return slide

    def empty_slide(self, name):
        return Slide(name, 'the file [ %s ] was not found' % name, 0 , 0)

    def get_next_link(self, current_slide, slide_count):
        if current_slide + 1 > slide_count:
            next_slide = 0
        else:
            next_slide = current_slide + 1
        return next_slide

    def get_prev_link(self, current_slide, slide_count):
        if current_slide - 1 < 0:
            prev_slide = slide_count
        else:
            prev_slide = current_slide - 1
        return prev_slide

class Loader(object):
    @staticmethod
    def load(name):
        p = Presentation()
        p.name = name

        try:
            file = open('slides/' + name, 'r').read()
            p.slides = file.split('~~')
        except IOError:
            p.slides = []

        return p

class Presentation(object):
    def __init__(self):
        self.name = ''
        self.slides = []
    

class Slide(object):
    def __init__(self, name, content, prev_link, next_link):
        self.name = name
        self.content = content
        self.prev_link = prev_link
        self.next_link = next_link
