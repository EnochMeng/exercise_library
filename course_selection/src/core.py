##程序运行的主要逻辑
import uuid
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
    while True:
        print('欢迎进入学生视图，请选择功能'.center(30,'*'))
        cmd = input('''
        1.注册信息
        2.登录
        3.返回上一级
        4.退出程序''').strip()
        if cmd == '1':
            while True:
                print('欢迎注册学生信息'.center(30, '-'))
                name = input('name: ').strip()
                # name_id = input('name_id: ').strip()  # 注册信息
                age = input('age: ').strip()
                gender = input('gender: ').strip()
                name_id = str(uuid.uuid1()) # 使用uuid生成绝对不一样的id用来标识每个人的身份
                if not name:
                    print('姓名必填')
                    continue
                break
            student_obj = models.Student(name, age, gender，name_id)
            student_obj.save()

        elif cmd == '2':
            while tag:
                print('请登录'.center(30, '-'))
                name = input('请输入用户名： ')
                name_id = input('请输入用户id： ')  # 登录，如果数据库中有这个人的文件，继续，否则打印用户不存在
                res = os.listdir(settings.STUDENTDB_PATH)
                for item in res:
                    file_path = r'%s\%s' % (settings.STUDENTDB_PATH, item)
                    with open(file_path, 'rb') as f:
                        student_obj = pickle.load(f)
                        if name == student_obj.name and name_id == student_obj.user_id:
                            while tag:
                                cmd = input('登录成功\n'
                                            '1.交学费\n'
                                            '2.选择班级\n'
                                            '3.返回上级\n'
                                            '4.退出程序\n'
                                            '请选择功能： ').strip()
                                if cmd == '1':  # 交学费
                                    money = int(input('请输入缴纳金额： '))
                                    student_obj.tuition += money
                                    print('缴纳成功，学费余额为%s' % student_obj.tuition)
                                    student_obj.save()
                                elif cmd == '2':  # 选择班级
                                    res = os.listdir(settings.CLASS_PATH)
                                    for item in res:
                                        file_path = r'%s\%s' % (settings.CLASS_PATH, item)
                                        with open(file_path, 'rb') as f:
                                            class_obj = pickle.load(f)
                                            print('班级名称：<%s> 班级所学课程<%s>' % (class_obj.name, class_obj.course))
                                    course_cmd = input('请选择班级：')
                                    res = os.listdir(settings.CLASS_PATH)
                                    for item in res:
                                        file_path = r'%s\%s' % (settings.CLASS_PATH, item)
                                        with open(file_path, 'rb') as f:
                                            class_obj = pickle.load(f)
                                        if course_cmd == class_obj.name:
                                            for i in class_obj.student:
                                                if student_obj.id == i.id:
                                                    print('班级已有此人')  # 如果班级里已有此人，则结束村换
                                                    tag = False
                                                else:
                                                    class_obj.student.append(student_obj)
                                                    student_obj.student_class.append(class_obj)
                                                    student_obj.save()
                                                    class_obj.save()
                                                    print('班级添加成功')
                                                    student_obj.tell_info()
                                elif cmd == '3':
                                    tag = False
                                elif cmd == '4':
                                    exit()
                                else:
                                    continue
                        else:
                            print('用户不存在')
                            tag = False



def admin_view():
    pass

def return_layer():
    pass

def logout():
    exit()



if __name__ == '__main__':
    main_func()





