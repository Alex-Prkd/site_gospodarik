import os


class PathImg:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    IMG_PATH = os.path.join(BASE_DIR, "static", "img")

    @classmethod
    def Services(cls):
        path_big_img = os.path.join(cls.IMG_PATH, "services", "big_size")
        path_middle_img = os.path.join(cls.IMG_PATH, "services", "middle_size")
        path_small_img = os.path.join(cls.IMG_PATH, "services", "small_size")
        return path_big_img, path_middle_img, path_small_img

    @classmethod
    def BackgroundPricePage(cls):
        path = os.path.join(cls.IMG_PATH, "background_price_page")
        return path

    @classmethod
    def PhotosMainPage(cls):
        path_big_img = os.path.join(cls.IMG_PATH, "photos_main_page", "big_size")
        path_middle_img = os.path.join(cls.IMG_PATH, "photos_main_page", "middle_size")
        path_small_img = os.path.join(cls.IMG_PATH, "photos_main_page", "small_size")
        return path_big_img, path_middle_img, path_small_img

    @classmethod
    def Icon(cls):
        path = os.path.join(cls.IMG_PATH, "icon")
        return path

    @classmethod
    def Link(cls):
        path = os.path.join(cls.IMG_PATH, "link")
        return path

    @classmethod
    def Logo(cls):
        path = os.path.join(cls.IMG_PATH, "logo")
        return path