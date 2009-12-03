import os

class Presentation(object):
    @staticmethod
    def get_all():
        presentations = []
        for root, dirs, files in os.walk("presentations"):
            presentations.append([root.replace("presentations", ""), files])
        return presentations
