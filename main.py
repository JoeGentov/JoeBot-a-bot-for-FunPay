import os, FunPayAPI
from FunPayAPI import Account, Runner, types, enums

def firstset():
    def check_key():
        filename = "goldenkey.txt"
    
        if os.path.exists(filename):
            with open(filename, "r") as file:
                saved_key = file.read().strip()
                print("Ключ найден!Сохранённый ключ находится в файле info.txt\nУдачного использования!")
                global golden_key
                golden_key = saved_key            
        else:
        
            print("Файл не найден. Введите ключ, он будет сохранён:")
            user_key = input("> ")
            with open(filename, "w") as file:
                file.write(user_key)
            print("Ключ сохранён в файл.")
    check_key()
    def firstmessage():
        filename = "message.txt"
    
        if os.path.exists(filename):
            with open(filename, "r") as file:
                saved_message = file.read().strip()
                print("Приветственное сообщение установлено, оно хранится в message.txt")
                global FirstMessage
                FirstMessage = saved_message         
        else:
        
            print(f"{filename} не найден. Введите приветственное сообщение, оно будет сохранено:")
            user_message = input("> ")
            with open(filename, "w") as file:
                file.write(user_message)
            print("Приветственное сообщение сохранено в файл.")
            
    firstmessage()
    def accountname():
        filename = "accountname.txt"
    
        if os.path.exists(filename):
            with open(filename, "r") as file:
                saved_name = file.read().strip()
                print("Необходимое имя аккаунта для автовыдачи установлено, оно хранится в accountname.txt")
                global Accountname
                Accountname = saved_name       
        else:
        
            print(f"{filename} не найден. Введите необходимое имя аккаунта для автовыдачи, оно будет сохранено:")
            user_name = input("> ")
            with open(filename, "w") as file:
                file.write(user_name)
            print("Имя сохранено в файл.")
    accountname()
    def autogetmail():
        filename = "account1mail.txt"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                saved_mail = file.read().strip()
                print(f"Почта для автовыдачи установлена, она хранится в {filename}")
                global mail
                mail = saved_mail    
        else:
        
            print(f"{filename} не найден. Введите почту для автовыдачи, она будет сохранена:")
            user_mail = input("> ")
            with open(filename, "w") as file:
                file.write(user_mail)
            print(f"Имя сохранено в {filename}")
    autogetmail()
    def autogetpass():
        filename = "account1pass.txt"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                saved_pass = file.read().strip()
                print(f"Пароль для автовыдачи установлен, он хранится в {filename}")
                global password
                password = saved_pass    
        else:
        
            print(f"{filename} не найден. Введите пароль для автовыдачи, он будет сохранен:")
            user_pass = input("> ")
            with open(filename, "w") as file:
                file.write(user_pass)
            print(f"Имя сохранено в {filename}") 
    autogetpass()
firstset()
    
        
        


TOKEN = golden_key

def first_message():
    acc = Account(TOKEN).get()
    runner = Runner(acc)
    
    for event in runner.listen(requests_delay=4):
        if event.type is enums.EventTypes.NEW_MESSAGE:
            if event.message.text.lower() == any and event.message.author_id !=acc.id:
                acc.send_message(event.message.chat_id, f"{FirstMessage}")
    return
first_message()

def autogetmailpass():
    acc = Account(TOKEN).get()
    runner = Runner(acc)
    
    for event in runner.listen(requests_delay=4):
        if event.type is enums.EventTypes.NEW_ORDER:
            if f"{accountname}" in event.order.description:
                chat = acc.get_chat_by_name(event,order.buyer_username, True)
                acc.send_message(chat.id, f"Привет, {event.order.buyer_username}!\n"
                                      f"Вот твой аккаунт:\n"
                                      f"Почта: {mail}\n"
                                      f"Пароль: {password}")
    return
autoget()
                             
