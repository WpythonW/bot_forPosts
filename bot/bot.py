import vk_api
import requests


def main():
    session = requests.Session()
    print("Authorization VK")
    login = input("Input phone(or login): ")
    password = input("Password: ")
    vk_session = vk_api.VkApi(login, password)
    
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    print("Authorization successful")
    msg = input("Text for post: ")
    ph = input("Photo for post(leave empty, if post is text only): ")
    #ret = vk.photos.getUploadServer(album_id = 220847175_000)
    #print(ret)
    
    #result = vk.photos.save(album_id = 220847175_000, photos_list = ["123.png"], server = vk.photos.getUploadServer())
    #print(result)
    
    with open('groups.txt', 'r', encoding='utf-8') as groups:
        for line in groups:
            post = vk.wall.post(owner_id = int(line), message = msg, attachments = ph)
            print(post)
    
    input()
    
main()