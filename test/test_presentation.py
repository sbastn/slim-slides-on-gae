from presentation import Slide
from mockito import *

import unittest

class SlideDataTest(unittest.TestCase):
    def test_content_is_retrieved(self):
        s = Slide('/dummy/0')
        s.retriever = Mock()
        when(s.retriever).open('/dummy', 0).thenReturn('simple content')
        s.get_data()
        self.assertEquals('simple content', s.content)

class SlideNumbersTest(unittest.TestCase):
    def test_extract_slide_num_from_path(self):
        s = Slide('/dummy/0')
        self.assertEquals(0, s.extract_slide_num_from_path())

    def test_extract_not_found_slide_num_from_path(self):
        s = Slide('/no_slide_num')
        self.assertEquals(0, s.extract_slide_num_from_path())

class SlideNameTest(unittest.TestCase):
    def test_extract_name_from_path(self):
        s = Slide('presentation/0')
        self.assertEquals('presentation', s.extract_name_from_path())

    def test_extract_name_with_folder_from_path(self):
        s = Slide('folder/presentation/0')
        self.assertEquals('folder/presentation', s.extract_name_from_path())

    def test_extract_name_with_no_slide_num_from_path(self):
        s = Slide('presentation')
        self.assertEquals('presentation', s.extract_name_from_path())

class SlideNavigationTest(unittest.TestCase):
    def setUp(self):
        self.s = Slide('presentation')

    def test_get_next_slide(self):
        self.assertEquals(1, self.s.get_next_slide(0, 2))

    def test_get_next_slides_wraps_around(self):
        self.assertEquals(0, self.s.get_next_slide(1, 1))

    def test_get_prev_slide(self):
        self.assertEquals(0, self.s.get_prev_slide(1, 2))

    def test_prev_slides_wraps_around(self):
        self.assertEquals(2, self.s.get_prev_slide(0, 2))        
