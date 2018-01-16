##定义各种类：学校，老师，课程，学生


class School:

    def __init__(self, name, site):
        self.name = name
        self.site = site


        ##用列表来保存老师，课程，班级
        self.school_teachers = []
        self.school_courses = []
        self.school_classes = []

    ##创建老师函数,返回一个老师对象
    def create_teacher(self, name, age, gender, salary):
        teacher_obj = Teacher(name, age, gender, salary)
        self.school_teachers.append(teacher_obj)
        return teacher_obj

    ##创建课程函数
    def create_course(self, name, price, period):
        course_obj = Course(name, price, period)

        self.school_courses.append(course_obj)
        return course_obj


    ##创建班级函数
    def create_class(self, name):
        class_obj = Class(name)
        self.school_classes.append(class_obj)
        return class_obj

    ##创建学生函数
    def create_student(self, name, age, gender):
        student_obj = Student(name, age, gender)
        
        return student_obj

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

class Teacher:
    def __init__(self,name,age,gender,salary):
        self.name = name
        self.age = age
        self.gender = gender
        self.salary = salary

class Class:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.teacher = []
        self.student = []

    ##查看班级信息
    def tell_class(self):
        print('''
        %s info
        course name: %s
        teacher name: %s
        student amount: %s
        '''%(self.name, self.course, self.teacher, self.student))

    ##保存信息
    def save(self):
        pass




class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

class Student:
    def __init__(self, name, age, gender, name_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.name_id = name_id

    def save(self):
        with open(r'%s\%s' % (settings.STUDENT_PATH, self.name_id), 'wb') as f:
            pickle.dump(self, f)



