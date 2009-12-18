from vendor import textile
import os

SLIDE_FOLDER = 'slides'
SLIDE_LINE_BREAK = '~~'

class PresentationBrowser(object):
    """ Retrieves all the presentations under the 'slides' folder.
    The slide folder can contain nested folders or symbolic links to other folders
    """ 

    @staticmethod
    def get_all():
        presentations = []
        for root, dirs, files in os.walk(SLIDE_FOLDER):
            presentations.append([root.replace(SLIDE_FOLDER, ''), files])

        return presentations


class PresentationController(object):
    """ Coordinates the work to get a presentation based on the path """

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
           return 0
       else:
           return current_slide + 1

    def get_prev_link(self, current_slide, slide_count):
        if current_slide - 1 < 0:
            return slide_count
        else:
            return current_slide - 1


class Loader(object):
    """ loads a presentation based on a url """
    @staticmethod
    def load(name):
        p = Presentation()
        p.name = name
        try:
            file = open('slides/' + name, 'r').read()
            p.slides = file.split(SLIDE_LINE_BREAK)
        except IOError:
            p.slides = []

        return p


class Presentation(object):
    """ representation of a container of one or more slides """
    def __init__(self):
        self.name = ''
        self.slides = []
    

class Slide(object):
    """ this is the slide object that the view is rendering """
    def __init__(self, name, content, prev_link, next_link):
        self.name = name
        self.content = content
        self.prev_link = prev_link
        self.next_link = next_link


next_link = lambda x, y: x + 1 if x + 1 <= y else 0
