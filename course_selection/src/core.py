##程序运行的主要逻辑
from src import models

school1 = School('北京大学'，'北京')
school2 = School('上海大学'，'上海')

course1 = school1.create_course('python', 29800, '6mons')
course2 = school1.create_course('linux', 9800, '4mons')
course3 = school2.create_course('go', 19800, '4mons')


##程序主要逻辑，主登录界面
def main_func():
    func_dic = {
        '1': student_view,
        '2': teacher_view,
        '3': admin_view,
        '4': return_layer,
        '5': logout
    }
    while True:
        print('欢迎进入选课系统：'.center(30, '*'),
              "\n1.北京大学\n"
              "2.上海大学\n"
              "3.退出")
        res = input('请选择学校：').strip()
        if res == '1':
            school = school1

        elif res == '2':
            school = school2

        elif res == '3':
            exit()
        else:
            print("不存在选项！")
            continue

        while True:
            print('请选择视图'.center(30, '*'))
            cmd = input('1.学生视图\n'
                        '2.老师视图\n'
                        '3.管理员视图\n'
                        '4.返回上一级\n'
                        '5.退出选课系统: ').strip()
            if cmd in func_dic:
                func_dic[cmd]()
            else:
                print('不存在选项！')


def teacher_view():
    pass

def student_view():
    pass

def admin_view():
    pass

def return_layer():
    pass

def logout():
    exit()



if __name__ == '__main__':
    main_func()





