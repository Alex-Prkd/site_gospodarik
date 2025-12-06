import os
from PIL import Image


class CreateCopySmallSizeIMG:
    # Класс создаёт копии фото для других устр-в.
        def __init__(self):
            self.__sizes: list = [2, 5]    # Уменьшаем исходно изобр. в 2 и 5 раз

        def createMobileIMG(self, name_img: str,
                            path_big_img: str,
                            path_middle_img: str,
                            path_small_img: str) -> None:
            for size in self.__sizes:
                with Image.open(os.path.join(path_big_img, name_img)) as img:
                    width, height = img.size
                    new_size = (width/size, height/2)
                    img.thumbnail(new_size)
                    if size == 2:
                        img.save(f"{path_middle_img}\\{name_img}")
                    else:
                        img.save(f"{path_small_img}\\{name_img}")