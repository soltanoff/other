#!/usr/bin/env python
import vk_api
import time

login = 'login@login'
password = 'password'
target_chat_id = 83 
target_chat_title = 'Zi'


def main():
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    vk = vk_session.get_api()
    
    print("Starting work...")

    try:
        while True:
            current_chat_title = vk.messages.getChat(chat_id=target_chat_id)['title']
            if current_chat_title != target_chat_title:
                print('Changed:', current_chat_title, 'to', target_chat_title)
                vk.messages.editChat(chat_id=target_chat_id, title=target_chat_title)
            time.sleep(2)
    except vk_api.ApiError as error_msg:
        print('[ApiError]', error_msg)
        return
    except vk_api.ApiHttpError as error_msg:
        print('[ApiHttpError]', error_msg)
        return
    except Exception as error_msg:
        print('[Any exception]', error_msg)
        return


if __name__ == '__main__':
    main()