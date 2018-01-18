# 类的整体说明介绍,类成员介绍

class Foo:

# 基本介绍    
    static_field = 'abc' # 静态字段：保存在类中，可以通过实例访问，也可以通过类直接访问
    __v = '123' # 静态私有字段，和下面的普通私有字段是一样的，就是一个是静态字段，一个是普通字段的区别。然后类的内部可以使用，外部不能使用私有字段，一模一样，不再做介绍


    def __init__(self): # 构造方法：创建实例时，会自动来执行这个方法
        self.name ='a' # 普通字段：保存在实例中，通过实例访问，不能通过类直接访问
        self.__age = 'b' # 成员修饰符：在前面加上两个下划线"__",就表示了这个是私有字段，外部不能直接访问，可以在内部写个函数简介访问，上面那个是共有字段，私有字段通过对象无法直接访问，也就是输入obj.__age时会报错
        # super(Foo，self).__init__() 这个是去找Foo的父类，并执行父类的__init__方法
        # 另外一种写法 父类名.__init__(self) 也可以执行父类的__init__方法，推荐使用上面的那种

    def show(self): # 通过这个方法，对象就可以在外部简介访问到这个__age了，输入obj.show().私有字段，类的内部可以使用，外部不能使用私有字段
        return self.__age # 静态私有字段，有可以写成Foo.__v来在内部使用

    def __fun(self): # 这个是私有方法，和上面的私有字段一样，加上两个下划线就好"__"，外部不能直接访问，可以在内部写个函数简介访问
        print('abc')

    def fun(self): #内部间接访问上面的私有方法，和上面的私有字段一样。
        self.__fun()
        return 123
    # 普通方法，静态方法，类方法，包括属性在内，只要加上"__"就可以来变为私有的，这就是成员修饰符
    # 注意子类也无法直接访问父类中的私有字段，私有方法，可以间接访问。
    
    def bar(self): # 普通方法
        # self是对象（实例）
        print('bar')

    @staticmethod # 静态方法：不用写self，可以传入参数，可以通过类直接访问，可以通过实例访问
    def stat(a1,a2):
        print(a1,a2)

    @classmethod # 类方法：默认传入类名作为第一个参数（cls是规范写法，其实可以不写），可以通过类直接访问，可以通过实例访问
    def classmd(cls):
        # cls 是类名
        print(cls)
        print('classmd')



        
# 属性介绍
    @property   # 属性（特性）：这样的函数可以后面不加括号，直接就运行，比如如下操作就可以直接运行此函数，通过实例调用，类不能直接调用
    def perr(self): # obj = Foo()  obj.perr   其实就是可以让这个函数像字段一样被调用。可以实现分页功能
        print('abc')    
        return 123

    # obj.perr = 123
    @perr.setter # 这个和property是一起的，当你在输入 obj.perr = 123 时，这个函数就会被调用，123 就会被作为 val 参数传入
    def perr(self, val): # 其实输入 obj.perr = 123 时，并没有真正进行赋值，仅仅是和这个函数对应，输入这句话就执行这个函数，你可以在这个函数里自己去写赋值，或者你想干嘛就干嘛
        print(val)      # 其实和反射很像

    # del obj.peer
    @perr.deleter # 这个和上面那个一样，也是和property是一起的，也是和这个函数对应的
    def perr(self): # 当你输入 del obj.perr时，就会执行这个函数,自己可以去试一下，仔细想想其实很多内置函数都是通过这些东西来实现的，列表啊什么的
        print(666)


    def f1(self): 
        return 123

    def f2(self,v):
        print(v)
        
    def f3(self):
        print('del')

    per = property(fget=f1,fset=f2,fdel=f3,doc='adfasdfasdfasdf')
    # 这个是属性的另一种表达方式，里面的 fget=f1(f1是上面的函数)其实就是和上面的@property的功能是一样的；fset=f2就是和上面的@perr.setter的功能是一样的；fdel=f3就是和上面的@perr.deleter的功能是一样的
# 比如输入obj.per就会去执行f1函数，obj.per=123就会去执行f2函数，del obj.per就会去执行f3函数，和上面是一样的，写法不一样
# doc就是说明，写这个property是用来干嘛的

# 类的特殊成员
# __init__：也是特殊成员,类后面加括号自动执行类中的__init__方法,Foo()
# __call__：对象后面加括号自动执行对象的类中的__call__方法，obj();Foo()()
# __int__: 当我们使用int转化为数字时，其实就是执行了数字对象中的__int__方法，python中一切皆对象，数字，字符都是对象；int(obj)时，其实就是去执行了obj那个类中的__int__方法
# __str__: 和上面的__int__一样，这个使用比较多。其实我们使用print(obj)时，python内部是执行print(str(obj)),因此其实就是去则行obj的类中的__str__方法，以后我们可以使用这个
# 特殊成员有很多
# __add__:其实python内部使用"+"时，比如r = obj1 + obj2时，就是去调用obj1类中的__add__方面，并且将第二个对象当做参数传输，return的值给r
# 加减乘除都是一样的，和上面的__add__一样
#__del__:


    
