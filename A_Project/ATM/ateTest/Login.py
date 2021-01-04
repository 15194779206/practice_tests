
class Login:
    def __init__(self):
        pass

    def login(self):
        f= open('name_info','r',encoding="utf-8")
        data = f.read()
        print(data)
        name = input("name:")
        passwd  = input("password:")




lo = Login()
lo.login()