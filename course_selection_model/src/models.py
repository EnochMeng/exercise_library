#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Sam"
# Date: 2017/7/4
from conf import settings
import pickle
import hashlib

class School:
    """学校类"""

    def __init__(self, school_name, school_site):
        self.school_name = school_name
        self.school_site = school_site
        self.school_courses = []  # 为学校所有的课程创建一个空列表
        self.school_terchers = []  # 创建一个空列表存放老师
        self.school_class = []  # 创建一个空列表存放班级

    def create_class(self, name, course):
        '''创建班级'''
        class_obj = Class(name, course)
        self.school_class.append(class_obj)
        return class_obj

    def create_course(self, course, price, period):
        '''创建课程'''
        course_obj = Course(course, price, period)
        self.school_courses.append(course_obj)
        return course_obj

    def create_teacher(self, name, user_id, age, sex, salary):
        '''创建老师'''
        teacher_obj = Teacher(name, user_id, age, sex, salary)
        self.school_terchers.append(teacher_obj)
        return teacher_obj

    def create_student(self, name, user_id, age, sex, classroom):
        '''创建学生'''
        student_obj = Student(name, user_id, age, sex)
        classroom.student.append(student_obj)
        return student_obj

    def save(self):
        '''保存信息'''
        with open(r'%s\%s' % (settings.SCHOOL_PATH, self.school_name), 'wb') as f:
            pickle.dump(self, f)


class Class:
    '''班级类'''

    def __init__(self, name, course):
        self.name = name
        self.teacher = []
        self.course = course
        self.student = []

    def tell_info(self):
        '''查看班级信息'''
        print('''
        -------%s info---------
        name:%s
        teacher:%s
        course:%s
        student:%s
        ''' % (self.name, self.name, self.teacher, self.course, self.student))

    def save(self):
        '''保存班级信息'''
        with open(r'%s\%s' % (settings.CLASS_PATH, self.name), 'wb') as f:
            pickle.dump(self, f)


class Course:
    '''课程类'''

    def __init__(self, course, price, period):
        self.course = course
        self.price = price
        self.period = period

    def tell_course(self):
        '''查看课程信息'''
        print('''
        --------%s info---------
        COURSE:%s
        PRICE:%s
        PERIOD:%s
        ''' % (self.course, self.course, self.price, self.period))

    def save(self):
        '''保存课程信息'''
        with open(r'%s\%s' % (settings.COURSE_PATH, self.course), 'wb') as f:
            pickle.dump(self, f)


class People:
    def __init__(self, name, user_id, age, sex):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sex = sex
        self.courses = []
        self.id = self.create_id()

    def tell_crouse(self):
        '''查看课程'''
        for obj in self.courses:
            obj.tell_crouse()

    def create_id(self):
        '''加密'''
        m = hashlib.md5()
        m.update(self.name.encode('utf-8'))
        m.update(str(self.user_id).encode('utf-8'))
        return m.hexdigest()


class Teacher(People):
    def __init__(self, name, user_id, age, sex, salary):
        People.__init__(self, name, user_id, age, sex)
        self.salary = salary
        self.teacher_class = []

    def tell_info(self):
        '''查看老师信息'''
        print('''
        --------%s info---------
        NAME:%s
        ID:%s
        AGE:%s
        SEX:%s
        SAL:%s
        CLASS:%s
        ''' % (self.name, self.name, self.user_id, self.age, self.sex, self.salary, self.teacher_class))

    def save(self):
        '''保存老师信息'''
        with open(r'%s\%s' % (settings.TEACHERDB_PATH, self.id), 'wb') as f:
            pickle.dump(self, f)


class Student(People):
    def __init__(self, name, user_id, age, sex):
        People.__init__(self, name, user_id, age, sex)
        self.student_class = []
        self.tuition = 0
        self.grade = 0

    def __str__(self):
        return self.name

    def tell_info(self):
        '''查看学生信息'''
        print('''
        ---------%s info----------
        NAME:%s
        ID:%s
        AGE:%s
        SEX:%s
        CLASS:%s
        TUITION:%s
        GRADE:%s
        ''' % (self.name, self.name, self.id, self.age, self.sex, self.student_class,
               self.tuition, self.grade))

    def save(self):
        '''保存学生信息'''
        with open(r'%s\%s' % (settings.STUDENTDB_PATH, self.id), 'wb') as f:
            pickle.dump(self, f)
