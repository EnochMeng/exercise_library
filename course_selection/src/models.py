##定义各种类：学校，老师，课程，学生

import hashlib

class School:

    def __init__(self, name, site):
        self.name = name
        self.site = site
        # 用列表来保存老师，课程，班级
        self.school_teachers = []
        self.school_courses = []
        self.school_classes = []

    # 创建老师函数,返回一个老师对象
    def create_teacher(self, name, user_id, age, sex, salary):
        teacher_obj = Teacher(name, user_id, age, sex, salary)
        self.school_teachers.append(teacher_obj)
        return teacher_obj

    # 创建课程函数
    def create_course(self, name, price, period):
        course_obj = Course(name, price, period)
        self.school_courses.append(course_obj)
        return course_obj

    # 创建班级函数
    def create_class(self, name, course):
        class_obj = Class(name, course)
        self.school_classes.append(class_obj)
        return class_obj

    # 创建学生函数
    def create_student(self, name, user_id, age, sex):
        student_obj = Student(name, user_id, age, sex)
        return student_obj


class People:
    def __init__(self, name, user_id, age, sex, *args, **kwargs):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.sex = sex
        self.courses = []
        self.owner_class = []
        self.id = self.create_id()

    def tell_crouse(self):
        '''查看课程'''
        for obj in self.courses:
            obj.tell_crouse()

    def tell_class(self):
        """查看班级"""
        for obj in self.owner_class:
            obj.tell_crouse()

    def create_id(self):
        '''加密'''
        m = hashlib.md5()
        m.update(self.name.encode('utf-8'))
        m.update(str(self.user_id).encode('utf-8'))
        return m.hexdigest()


class Teacher(People):
    def __init__(self, name, user_id, age, sex, salary, *args, **kwargs):
        People.__init__(self, name, user_id, age, sex, *args, **kwargs)
        self.salary = salary

    def save(self):
        pass


class Class:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.teacher = []
        self.student = []

    # 查看班级信息
    def tell_class(self):
        print('''
        %s info
        course: %s
        teacher: %s
        student: %s
        ''' % (self.name, self.course, self.teacher, self.student))

    # 保存信息
    def save(self):
        pass


class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

    def tell_course(self):
        '''查看课程信息'''
        print('''
        --------%s info---------
        COURSE:%s
        PRICE:%s
        PERIOD:%s
        ''' % (self.name, self.name, self.price, self.period))

    def save(self):
        pass


class Student(People):
    def __init__(self, name, user_id, age, sex):
        People.__init__(self, name, user_id, age, sex)
        self.tuition = 0
        self.grade = 0

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
        ''' % (self.name, self.name, self.id, self.age, self.sex, self.owner_class,
               self.tuition, self.grade))

    def save(self):
        pass
