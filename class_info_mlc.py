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
# doc就是说明，用来写这个property是用来干嘛的

    def __getitem__(self,item):
        print(item,type(item))
        if type(item) == slice: # 当列表进行切片操作时，比如li[1:9:2]取1到9，步长为2。那传入的值就变为1:9:2，其实这是传入的1:9:2就是一个slice类型
            print(item.start,item.stop,item.step)# 可以打印出来，看看type(item)是什么，然后可以去看看slice类中的方法，其实slice.start就是1，slice.stop就是9，slice.step就是2
            print('进行切片处理')
        return item

    def __setitem__(self,key,item):
        print(key,item)

    def __delitem__(self,key,):
        print(key)    
# 上面这三个特殊方法比较重要，这个就类似于上面的property和列表。注意想想，其实你创建一个列表时，就是创建了一个列表的对象，li = list([1,2,3,4])
# 比如li = [1,2,3,4] ,li[0]就是对应去执行了__getitem__那个方法，li[0] = 99 这个重新赋值其实就是对应去执行__setitem__方法，del li[0] 其实就是去执行__delitem__方法


# 类的特殊成员
# __init__：也是特殊成员,类后面加括号自动执行类中的__init__方法,Foo()
# __call__：对象后面加括号自动执行对象的类中的__call__方法，obj();Foo()()
# __int__: 当我们使用int转化为数字时，其实就是执行了数字对象中的__int__方法，python中一切皆对象，数字，字符都是对象；int(obj)时，其实就是去执行了obj那个类中的__int__方法
# __str__: 和上面的__int__一样，这个使用比较多。其实我们使用print(obj)时，python内部是执行print(str(obj)),因此其实就是去则行obj的类中的__str__方法，以后我们可以使用这个
# 特殊成员有很多
# __add__:其实python内部使用"+"时，比如r = obj1 + obj2时，就是去调用obj1类中的__add__方面，并且将第二个对象当做参数传输，return的值给r
# 加减乘除都是一样的，和上面的__add__一样
#__del__: 析构方法：对象被销毁时，自动被触发
#__dict__: 将对象中封装的所有内容，通过字典返回，这个比较重要，用得会比较多，这个我们不需要自己去写一个__dict__方法，可以直接使用 obj.__dict__ 这样就把obj中封装的所有荣内作为一个字典返回
#__dict__也可以将类中的所有成员都显示出来，类中的成员很多，像注释等也算是类的成员，只是我们看不到

    def __iter__(self): # 如果类中有__iter__方法，那这个类的对象就是可迭代对象，可迭代对象并不能使用.next方法，迭代器才能，所以__iter__的返回值是个迭代器iter()
        return iter([11,22,33,44,55,66]) # 可迭代对象中的__iter__方法的返回值是一个迭代器
# 其实for i in li：print(i),在for循环中如果运到的事可迭代对象，就是可迭代对象的类中执行__iter__方法，并获取其返回值。然后执行返回值也就是一个迭代器的.next循环它
i = iter([1,2,3]) # i就是一个迭代器
i.__next__() # 也可以写成next(i)，一样的，两种写法
i.__next__()
i.__next__()
# i.__next__() # 报错了，因为没有值了

for item in i: # 其实for在这里就是帮我们执行了上面的操作，和上面是一样的，还帮我们自动处理了最后没有值得报错
    print(i)


# 所有的类都是由type创建的对象，type是个超级类，类的祖宗（元类）。也就是当类没有写__init__方法时，类会去调用type的__init__方法

class mytype(type): # 创建一个自己的元类
    def __init__(self,*args,**kwargs):
        super(mytype,self).__init__(self)
        print('123')

    def __call__(self,*args,**kwargs): # call不写的话，好像也可以直接执行的
        print('456')
        # 这里的self就是Bar
        obj = self.__new__(self,*args,**kwargs) # 表示一下流程
        self.__init__(obj)

class Bar(object,metaclass=mytype): # 使用我自己的设计的元类mytype，不使用type了，也就是会主动执行我mytype中的__init__方法.
    def __init__(self):
        print('abc')

    def __new__(cls,*args,**kwargs): # new不写好像也可以直接执行，表示一下流程
        return cls.__new__(cls,*args,**kwargs)

##    obj = Bar()
# 从上面我们可以看出来，当我们创建一个对象比如：obj = Bar()时，其实Bar也是个对象，所以，Bar()也就是执行了mytype中的__call__方法，之前讲过，对象加括号，就是调用__call__方法
# 执行了mytype中的__call__后，会再去执行Bar中__new__方法，__new__方法就返回了一个对象，然后对象obj再去执行Bar的__init__,我上面写的代码并不能完全模拟这个流程，只是表达了这么一个意思这个就是我们要创建的Bar的对象obj,自己去执行一下，obj = Bar（）看看结果
# 关于元类的一些流程还是不太对，我们需要记住，obj = Bar()并不是直接去执行Bar的__init__方法，其实是经过上面的方法后菜自行到Bar的__init__方法

# 反射为我们提供的方法，通过字符串来操作对象中成员，python中一切皆对象，因此这getattr，hasatter，setattr，delattr4个方法，同样可以去操作模块，类中的成员
# import s2 ; getattr(s2,'xxx')这样也是可以的，自己需要多扩展，根据定义。
obj = Foo()
r = getattr(obj,'name') # 去什么里面，拿出什么东西。这个就是去obj对象中，把name给拿出来,r就应该等于'a'
print(r)
func = getattr(obj,'show') # 也可以去obj对象的类中拿函数出来执行 func()就是执行了Foo中的show函数
func()

hasattr(obj,'name') # 判断obj对象的类中是否有‘name’这个东西，上的事get，这个是has一个道理。
setattr(obj,'k1','v1') # 设置一个东西，这个就是在obj对象中添加一个obj.k1 = 'v1'，就是一个赋值操作
print(obj.k1)
delattr(obj,'name') # 删除obj对象中的'name',与上面的一样

#单例，用于使用同一份实例，比如如下的类，就在内部添加了一个单例模式，如果要使用，可以直接去使用
class S1:
    __v = None
    
    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = S1()
            return cls.__v
        
s1 = S1.get_instance() # 如果想要用单例模式，就使用这样的方法去创建对象，不要使用S1()。
print(s1)
s2 = S1.get_instance()
print(s2)
# 执行上面可以发现s1和s2打印出来的内存地址是一样的，这就是单例模式
