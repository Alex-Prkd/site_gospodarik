import os


class RemoveImages:
    @staticmethod
    def remove(name_img,
               path_big_img,
               path_middle_img,
               path_small_img):

        if os.path.exists(os.path.join(path_big_img, name_img)):
            os.remove(os.path.join(path_big_img, name_img))

        if os.path.exists(os.path.join(path_middle_img, name_img)):
            os.remove(os.path.join(path_middle_img, name_img))

        if os.path.exists(os.path.join(path_small_img, name_img)):
            os.remove(os.path.join(path_small_img, name_img))

    @staticmethod
    def remove_avatar(path: str):
        old_avatar = os.listdir(path)
        if len(old_avatar) == 0:
            return
        old_avatar = old_avatar[0]
        if os.path.exists(os.path.join(path, old_avatar)):
            os.remove(os.path.join(path, old_avatar))
