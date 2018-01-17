#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/7/4


from src import models
from conf import settings
import pickle
import os

s1 = models.School('北京校区', '中国北京')
s2 = models.School('上海校区', '中国上海')
python = s1.create_course('Python', 19800, '6mons')
linux = s1.create_course('Linux', 17800, '4mons')
go = s2.create_course('Go', 9000, '4mons')
school_obj = None

def func():
    while True:
        print('欢迎进入老男孩选课系统'.center(30, '*'),
              '\n1.北京校区\n'
              '2.上海校区\n'
              '3.退出程序')
        res = input('请选择学校： ').strip()
        global school_obj
        if res == '1':
            school_obj = s1
        elif res == '2':
            school_obj = s2
        elif res == '3':
            break
        else:
            print('输入错误')
            continue

        while True:
            print('请选择视图'.center(30, '*'))
            cmd = input('1.学生视图\n'
                        '2.老师视图\n'
                        '3.管理员视图\n'
                        '4.返回上一级\n'
                        '5.退出选课系统: ').strip()
            if cmd == '1':
                student_view()
            elif cmd == '2':
                teacher_view()
            elif cmd == '3':
                admin_viwe()
            elif cmd == '4':
                break
            elif cmd == '5':
                exit()
            else:
                print('输入错误，请重新输入！')
                continue
    return school_obj


def student_view():
    '''学生视图'''
    while True:
        tag = True
        print('欢迎进入学生视图，请选择功能'.center(30, '*'))
        cmd = input('1.注册信息\n'
                    '2.登录\n'  # 循环选择功能
                    '3.返回上级\n'
                    '4.退出程序： ').strip()
        if cmd == '1':
            while True:
                print('欢迎注册学生信息'.center(30, '-'))
                name = input('name: ').strip()
                name_id = input('name_id: ').strip()  # 注册信息
                age = input('age: ').strip()
                sex = input('sex: ').strip()
                if not name:
                    print('姓名必填')
                    continue
                break
            student_obj = models.Student(name, name_id, age, sex)
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
        elif cmd == '3':
            return
        elif cmd == '4':
            exit()
        else:
            continue


def teacher_view():
    '''讲师视图'''
    tag = True  # 添加一个标志位
    while tag:
        print('请登录'.center(30, '-'))
        name = input('请输入用户名： ').strip()
        name_id = input('请输入用户id： ').strip()
        res = os.listdir(settings.TEACHERDB_PATH)
        for item in res:
            file_path = r'%s\%s' % (settings.TEACHERDB_PATH, item)
            with open(file_path, 'rb') as f:
                teacher_obj = pickle.load(f)
                if name == teacher_obj.name and name_id == teacher_obj.user_id:
                    while tag:
                        print('欢迎进入讲师视图'.center(30, '*'))
                        cmd = input('1.管理班级\n'
                                    '2.选择上课班级\n'
                                    '3.查看班级学员列表\n'
                                    '4.修改学员成绩\n'
                                    '5.返回上一级\n'
                                    '6.退出选课系统\n'
                                    '请选择功能： ').strip()
                        if cmd == '1':
                            for i in teacher_obj.teacher_class:
                                i.tell_info()
                        elif cmd == '2':
                            res = os.listdir(settings.CLASS_PATH)
                            for item in res:
                                file_path = r'%s\%s' % (settings.CLASS_PATH, item)
                                with open(file_path, 'rb') as f:
                                    class_obj = pickle.load(f)
                                    print('班级名称：<%s> 班级所学课程<%s>' % (class_obj.name, class_obj.course))
                            class_cmd = input('请选择班级：')
                            res = os.listdir(settings.CLASS_PATH)
                            for item in res:
                                file_path = r'%s\%s' % (settings.CLASS_PATH, item)
                                with open(file_path, 'rb') as f:
                                    class_obj = pickle.load(f)
                                if class_obj.name == class_cmd:
                                    class_obj.teacher.append(teacher_obj)
                                    teacher_obj.teacher_class.append(class_obj)
                                    teacher_obj.save()
                                    class_obj.save()
                                    teacher_obj.tell_info()
                        elif cmd == '3':
                            for i in teacher_obj.teacher_class:
                                for j in i.student:
                                    j.tell_info()
                        elif cmd == '4':
                            name = input('请输入想要修改的学生姓名：').strip()
                            name_id = input('请输入学生id： ').strip()
                            num = int(input('请输入要修改的成绩： ').strip())
                            res = os.listdir(settings.STUDENTDB_PATH)
                            for item in res:
                                file_path = r'%s\%s' % (settings.STUDENTDB_PATH, item)
                                with open(file_path, 'rb') as f:
                                    student_obj = pickle.load(f)
                                    if name == student_obj.name and name_id == student_obj.user_id:
                                        student_obj.grade += num
                                        print('%s 的成绩已修改为 %s' % (student_obj.name, num))
                                        student_obj.save()
                        elif cmd == '5':
                            tag = False
                        elif cmd == '6':
                            exit()
                        else:
                            continue


def admin_viwe():
    '''管理员视图'''
    print('请用管理员的身份登录，用户名：sam，密码：666'.center(30, '*'))  # 管理员有固定的用户名密码
    name = input('请输入用户名： ')
    password = input('请输入密码： ')
    if name == 'sam' and password == '666':
        while True:
            print('欢迎进入管理员视图'.center(30, '-'))
            cmd = input('1.创建讲师\n'
                        '2.创建班级\n'
                        '3.创建课程\n'
                        '4.返回\n'
                        '5.退出选课系统\n'
                        '请选择功能: ')
            if cmd == '1':
                name = input('请输入讲师姓名： ').strip()
                user_id = input('请输入讲师id： ').strip()
                age = input('请输入讲师年纪： ').strip()
                sex = input('请输入讲师性别： ').strip()
                salary = input('请输入讲师薪资： ').strip()
                if not name:
                    print('名字不能为空')
                    continue
                teacher = school_obj.create_teacher(name, user_id, age, sex, salary)
                teacher.save()
                school_obj.save()
                print('%s 老师的信息创建成功' % teacher.name)
                teacher.tell_info()
            elif cmd == '2':
                name = input('请输入班级名： ').strip()
                course = input('请输入班级课程： ').strip()
                if not name or not course:
                    print('输入错误')
                    continue
                class_obj = school_obj.create_class(name, course)
                class_obj.save()
                school_obj.save()
                print('%s 班级创建成功' % class_obj.name)
                class_obj.tell_info()
            elif cmd == '3':
                course = input('请输入课程名字： ').strip()
                price = input('请输入课程价钱： ').strip()
                period = input('请输入课程周期： ').strip()
                if not course or not price or not period:
                    print('输入错误')
                    continue
                course_obj = school_obj.create_course(course, price, period)
                course_obj.save()
                school_obj.save()
                print('%s 课程创建成功' % course_obj.course)
                course_obj.tell_course()
            elif cmd == '4':
                return
            elif cmd == '5':
                exit()
            else:
                continue
    else:
        print('用户名密码错误')


if __name__ == '__main__':
    func()
