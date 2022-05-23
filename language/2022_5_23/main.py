def register():
        name = input('姓名>')
        age = input('年龄>')
        telephone = input('电话号码>')
        with open('./info.txt', 'a') as fp: 
            fp.write(name+'-'+age+'-'+telephone+'\n')
def login():
    pass 
def menu():
    print('欢迎使用学生管理系统')
    print('-----------------')
    print('1.登录\n2.注册\n3.退出')
    choice = input('选择>')
    if choice == '1':
        pass
    elif choice == '2':
        register()
    elif choice == '3':
        exit()
    else:
        print('非法输入')
# main
menu()
