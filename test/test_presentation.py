import unittest
from presentation import Slide

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
    def test_get_next_slide(self):
        s = Slide(None)
        self.assertEquals(1, s.get_next_slide(0, 2))

    def test_get_next_slides_wraps_around(self):
        s = Slide(None)
        self.assertEquals(0, s.get_next_slide(1, 1))

    def test_get_prev_slide(self):
        s = Slide(None)
        self.assertEquals(0, s.get_prev_slide(1, 2))

    def test_prev_slides_wraps_around(self):
        s = Slide(None)
        self.assertEquals(2, s.get_prev_slide(0, 2))
        
        
