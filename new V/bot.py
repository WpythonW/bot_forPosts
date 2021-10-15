import vk_api
import requests
import os
import PyQt5
from PyQt5 import QtWidgets, uic
import sys


def gui():
    #app = QtWidgets.QApplication([])
    win = uic.loadUi("mydesign.ui") # расположение вашего файла .ui
    win.show()
    sys.exit(app.exec())  
    



class Auth():
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.win = uic.loadUi("auth_dual.ui") # расположение вашего файла .ui
        self.win.show()
 
    def auth_handler(self):
        # Код двухфакторной аутентификации
        self.win.close()
        self.win_dual = uic.loadUi("twofact.ui")
        self.win_dual.show()
        key = input("Enter authentication code: ")
        # Если: True - сохранить, False - не сохранять.
        remember_device = False  #потом изменить
        return key, remember_device
            
            
    def authorization(self):
        vk_session = vk_api.VkApi(self.win.login.text(), self.win.password.text(), auth_handler=self.auth_handler)
        try:
            vk_session.auth(token_only=True)
        except (vk_api.exceptions.LoginRequired, vk_api.exceptions.BadPassword):
            self.win.message.setText("неверный логин или пароль")
            return 0
        vk = vk_session.get_api()
        return vk
    
    def gui_authorization(self):
        vk = self.win.enter.clicked.connect(self.authorization)
        sys.exit(self.app.exec())  
    
    

def main():
    obj_auth = Auth()
    obj_auth.gui_authorization()
    
    #ret = vk.photos.getUploadServer(album_id = 220847175_000)
    #print(ret)
    
    #result = vk.photos.save(album_id = 220847175_000, photos_list = ["123.png"], server = vk.photos.getUploadServer())
    #print(result)
    status = "1"
    with open(os.path.join('groups.txt'), 'r', encoding='utf-8') as groups:
        while(status == "1"):
            msg = input("Text for post: ")
            ph = input("Photo for post(leave empty, if post is text only): ").split()
            for line in groups:
                post = vk.wall.post(owner_id = int(line), message = ph, attachments = ph)
                print(post)
            print("==========================")
            input("next post - 1, stop program - 0: ")
    
    input()
    
main()
#gui()