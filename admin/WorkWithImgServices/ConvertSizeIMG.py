import io
import os
from PIL import Image
from werkzeug.datastructures import FileStorage


class CreateCopySmallSizeIMG:
    # Класс создаёт копии фото для других устр-в.
        def __init__(self):
            self.__sizes: list = [2, 5]    # Уменьшаем исходно изобр. в 2 и 5 раз

        def createMobileIMG(self, name_img: str,
                            path_big_img: str,
                            path_middle_img: str,
                            path_small_img: str) -> None:
            with Image.open(os.path.join(path_big_img, name_img)) as img:
                for size in self.__sizes:
                    width, height = img.size
                    new_size = (width/size, height/size)
                    img.thumbnail(new_size)
                    if size == 2:
                        img.save(f"{path_middle_img}\\{name_img}")
                    else:
                        img.save(f"{path_small_img}\\{name_img}")


        def convertSizeImgReview(self, img: FileStorage,
                                 path_big_size: str,
                                 path_middle_size: str,
                                 path_small_size: str):
            if isinstance(img, FileStorage):
                current_pos = img.tell()
                img.seek(0)
                convert_img = Image.open(io.BytesIO(img.read()))
                convert_img.thumbnail((1280, 1280))
                convert_img.save(f"{path_big_size}\\{img.filename}")
                img.seek(current_pos)
                self.createMobileIMG(name_img=img.filename,
                                     path_big_img=path_big_size,
                                     path_middle_img=path_middle_size,
                                     path_small_img=path_small_size
                                     )