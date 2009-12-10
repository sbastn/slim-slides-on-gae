from presentation import PresentationController

import unittest

class SlideDataTest(unittest.TestCase):
    def setUp(self):
        self.p = PresentationController()

    def test_retrieve_welcome_slide_number_0(self):
        slide = self.p.get_slide('/welcome/0')

        self.assertEquals('/welcome', slide.name)
        self.assertEquals(1, slide.next_link)
        self.assertEquals(8, slide.prev_link)
        self.assertTrue('YES' in slide.content)

    def test_retrieve_not_found_file(self):
        slide = self.p.get_slide('/i/do/not/exist')
        
        self.assertEquals('the file [ /i/do/not/exist ] was not found', slide.content)

class SlideNumbersTest(unittest.TestCase):
    def setUp(self):
        self.p = PresentationController()

    def test_extract_slide_num_from_path(self):
        self.assertEquals(1, self.p.extract_slide('/dummy/1'))

    def test_extract_not_found_slide_num_from_path(self):
        self.assertEquals(0, self.p.extract_slide('/no_slide_num'))

class SlideNameTest(unittest.TestCase):
    def setUp(self):
        self.p = PresentationController()

    def test_extract_name_with_slide_number(self):
        self.assertEquals('presentation', self.p.extract_name('presentation/1'))

    def test_extract_name_with_folder_and_slide_number(self):
        self.assertEquals('folder/presentation', self.p.extract_name('folder/presentation/0'))

    def test_extract_name_with_no_slide_number(self):
        self.assertEquals('presentation', self.p.extract_name('presentation'))

    def test_extract_name_with_no_slide_num_ber_and_folder(self):
        self.assertEquals('hello/world', self.p.extract_name('hello/world'))

class SlideNavigationTest(unittest.TestCase):
    def setUp(self):
        self.p = PresentationController()

    def test_get_next_slide(self):
        self.assertEquals(1, self.p.get_next_link(0, 2))

    def test_get_next_slides_wraps_around(self):
        self.assertEquals(0, self.p.get_next_link(1, 1))

    def test_get_prev_slide(self):
        self.assertEquals(0, self.p.get_prev_link(1, 2))

    def test_prev_slides_wraps_around(self):
        self.assertEquals(2, self.p.get_prev_link(0, 2))        
