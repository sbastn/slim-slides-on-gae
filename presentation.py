from vendor import textile
import os

class Presentation(object):
	
    @staticmethod
    def get_all():
        presentations = []

        for root, dirs, files in os.walk('slides'):
            presentations.append([root.replace('slides', ''), files])

        return presentations

class Retriever(object):
    def __init__(self):
        self.slides = 0
        self.content = ''

    def open(self, path, current_slide):
        try:
            file = open('slides/' + path, 'r').read()
            self.slides = file.split('~~')
            self.content = textile.textile(self.slides[current_slide].strip())
        except IOError:
            self.slides = 0
            self.content = 'the document [ %s ] was not found' % path

        return self.content

class Slide(object):
    def __init__(self, path):
        self.path = path
        self.slide_separator = '~~'
        self.retriever = Retriever()

    def get_data(self):
        self.current_slide = self.extract_slide_num_from_path()
        self.name = self.extract_name_from_path()
        
        self.content = self.retriever.open(self.name, self.current_slide)
        
        self.prev_slide = self.get_prev_slide(self.current_slide, self.retriever.slides)
        self.next_slide = self.get_next_slide(self.current_slide, self.retriever.slides)

        return self

    def extract_slide_num_from_path(self):
        try:
            return int(self.path.split('/')[len(self.path.split('/')) - 1])
        except ValueError:
            return 0

    def extract_name_from_path(self):
        if len(self.path.split('/')) < 2:
            name = self.path.split('/')[0:len(self.path.split('/'))]
        else:
            name = self.path.split('/')[0:len(self.path.split('/')) - 1]
        return "/".join(name)

    def get_next_slide(self, current_slide, slide_count):
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
    
