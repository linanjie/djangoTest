from django.db import models

# Create your models here.
# 我们新建了一个Person类，继承自models.Model, 一个人有姓名和年龄
# class Person(models.Model):
#     # name 和 age 等字段中不能有 __（双下划线 在Django QuerySet API中有特殊含义
#     # （用于关系，包含，不区分大小写，以什么开头或结尾，日期的大于小于，正则等）
#     # 也不能有Python中的关键字，name 是合法的，student_name 也合法，
#     # 但是student__name不合法。try, class, continue 也不合法，
#     # 因为它是Python的关键字( import keyword; print(keyword.kwlist)
#     # 可以打出所有的关键字)
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name


# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
#
# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     n_comments = models.IntegerField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     def __str__(self):
#         return self.headline

# 总之，一共有四种方法
# # 方法 1
# Author.objects.create(name="WeizhongTu", email="tuweizhong@163.com")
#
# # 方法 2
# twz = Author(name="WeizhongTu", email="tuweizhong@163.com")
# twz.save()
#
# # 方法 3
# twz = Author()
# twz.name="WeizhongTu"
# twz.email="tuweizhong@163.com"
# twz.save()
#
# # 方法 4，首先尝试获取，不存在就创建，可以防止重复
# Author.objects.get_or_create(name="WeizhongTu", email="tuweizhong@163.com")
# # 返回值(object, True/False)

# 获取对象的方法
# Person.objects.all()  # 查询所有
# Person.objects.all()[:10]
# 切片操作，获取10个人，不支持负索引，切片可以节约内存，不支持负索引，后面有相应解决办法，第7条
# Person.objects.get(name="WeizhongTu")  # 名称为 WeizhongTu 的一条，多条会报错
#
# get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter
# Person.objects.filter(name="abc")  # 等于Person.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人
# Person.objects.filter(name__iexact="abc")  # 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件
#
# Person.objects.filter(name__contains="abc")  # 名称中包含 "abc"的人
# Person.objects.filter(name__icontains="abc")  # 名称中包含 "abc"，且abc不区分大小写
#
# Person.objects.filter(name__regex="^abc")  # 正则表达式查询
# Person.objects.filter(name__iregex="^abc")  # 正则表达式不区分大小写
#
# # filter是找出满足条件的，当然也有排除符合某条件的
# Person.objects.exclude(name__contains="WZ")  # 排除包含 WZ 的Person对象
# Person.objects.filter(name__contains="abc").exclude(age=23)  # 找出名称含有abc, 但是排除年龄是23岁的

# 删除符合条件的结果
# Person.objects.filter(name__contains="abc").delete()  # 删除 名称中包含 "abc"的人
#
# 如果写成
# people = Person.objects.filter(name__contains="abc")
# people.delete()
# 效果也是一样的，Django实际只执行一条
# SQL
# 语句。

# 4. 更新某个内容
#
# (1) 批量更新，适用于 .all()  .filter()  .exclude() 等后面 (危险操作，正式场合操作务必谨慎)
# Person.objects.filter(name__contains="abc").update(name='xxx') # 名称中包含 "abc"的人 都改成 xxx
# Person.objects.all().delete() # 删除所有 Person 记录
# (2) 单个 object 更新，适合于 .get(), get_or_create(), update_or_create() 等得到的 obj，和新建很类似。
# twz = Author.objects.get(name="WeizhongTu")
# twz.name="WeizhongTu"
# twz.email="tuweizhong@163.com"
# twz.save()  # 最后不要忘了保存

# 5. QuerySet 是可迭代的
# es = Entry.objects.all()
# for e in es:
#     print(e.headline)

# Entry.objects.all() 或者 es 就是 QuerySet 是查询所有的 Entry 条目。
#
# 注意事项：
#
# (1). 如果只是检查 Entry 中是否有对象，应该用 Entry.objects.all().exists()
#
# (2). QuerySet 支持切片 Entry.objects.all()[:10] 取出10条，可以节省内存
#
# (3). 用 len(es) 可以得到Entry的数量，但是推荐用 Entry.objects.count()来查询数量，后者用的是SQL：SELECT COUNT(*)
#
# (4). list(es) 可以强行将 QuerySet 变成 列表

# 6. QuerySet 是可以用pickle序列化到硬盘再读取出来的
# 7. QuerySet 查询结果排序
# Author.objects.all().order_by('name')
# Author.objects.all().order_by('-name') # 在 column name 前加一个负号，可以实现倒序

# 8. QuerySet 支持链式查询
# 支持类似stream流的链式设计查询

# 9. QuerySet 不支持负索引
# Person.objects.all()[:10]
# 切片操作，前10条
# Person.objects.all()[-10:]
# 会报错！！！
#
# # 1. 使用 reverse() 解决
# Person.objects.all().reverse()[:2]  # 最后两条
# Person.objects.all().reverse()[0]  # 最后一条
#
# # 2. 使用 order_by，在栏目名（column name）前加一个负号
# Author.objects.order_by('-id')[:20]  # id最大的20条

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# 创建Django数据后台
@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')

    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    # 所以推荐定义 Model 的时候 写一个 __unicode__ 函数(或 __str__函数)
    def __str__(self):  # python用__str__代替 __unicode__
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def my_property(self):
        return self.first_name + ' ' + self.last_name

    my_property.short_description = "Full name of the person"

    full_name = property(my_property)
