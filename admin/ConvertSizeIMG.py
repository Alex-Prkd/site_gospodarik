import os
from PIL import Image


class CreateCopySmallSizeIMG:
        def __init__(self, name_img: str, path: str):
            self.__sizes: list = [2, 5]    # Уменьшаем исходно изобр. в 2 и 5 раз
            self.__pathNewSmallIMG: str = os.path.join(os.path.abspath("static/img/small_size"))
            self.__pathNewMiddleIMG: str = os.path.join(os.path.abspath("static/img/middle_size"))
            self.createMobileIMG(name_img, path)

        def createMobileIMG(self, name_img: str, path: str) -> None:
            for size in self.__sizes:
                with Image.open(os.path.join(path,name_img)) as img:
                    width, height = img.size
                    new_size = (width/size, height/2)
                    img.thumbnail(new_size)
                    if size == 2:
                        img.save(f"{self.__pathNewMiddleIMG}\\{name_img}")
                    else:
                        img.save(f"{self.__pathNewSmallIMG}\\{name_img}")