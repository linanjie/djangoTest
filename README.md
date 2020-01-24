project和app的关系
一个项目一般包含多个应用，一个应用也可以用在多个项目中
生成的python migration文件是描述数据库结构变化的
这时候，数据库还没真正变化，只是生成了描述数据库变化的文件。

新建一个对象的方法

    1.Person.objects.create(name=name,age=age)
    
    2.p = Person(name="WZ", age=23)

      p.save()

    3.p = Person(name="TWZ")

      p.age = 23

      p.save()

    4.Person.objects.get_or_create(name="WZT", age=23)

    这种方法是防止重复很好的方法，但是速度要相对慢些，返回一个元组，第一个为Person对象，第二个为True或False, 新建时返回的是True, 已经存在时返回False.

获取对象方法：
    
    1.Person.objects.all()

    2.Person.objects.all()[:10] 切片操作，获取10个人，不支持负索引，切片可以节约内存

    3.Person.objects.get(name=name)
    
get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter

    4.Person.objects.filter(name="abc")  # 等于Person.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人

    5.Person.objects.filter(name__iexact="abc")  # 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件
    
    6.Person.objects.filter(name__contains="abc")  # 名称中包含 "abc"的人
    
    7.Person.objects.filter(name__icontains="abc")  #名称中包含 "abc"，且abc不区分大小写
    
    8.Person.objects.filter(name__regex="^abc")  # 正则表达式查询
    
    9.Person.objects.filter(name__iregex="^abc")  # 正则表达式不区分大小写
    
filter是找出满足条件的，当然也有排除符合某条件的
    
    10.Person.objects.exclude(name__contains="WZ")  # 排除包含 WZ 的Person对象
    
    11.Person.objects.filter(name__contains="abc").exclude(age=23)  # 找出名称含有abc, 但是排除年龄是23岁的

ps aux | grep python 来查看系统中运行的 python 进程
输出结果中 USER 后面的 PID 代表进程编号。
我们可以通过查看 /proc/PID/ 目录的文件信息来得到这个进程的一些信息（Linux中一切皆文件，进程信息也在文件中）
tu@linux /proc/4491 $ sudo ls -ahl

上面的信号是有顺序的，比如第1个是 HUP，第9个是 KILL，下面两种方式是等价的：
kill -1 PID 和 kill -HUP PID
kill -9 PID 和 kill -KILL PID

感兴趣的读者还可以自行学习，深入了解下uwsgi和nginx无损reload的机制。
CTRL-C 发送 SIGINT 信号给前台进程组中的所有进程，常用于终止正在运行的程序。
CTRL-Z 发送 SIGTSTP 信号给前台进程组中的所有进程，常用于挂起一个进程。

3. 查看进程打开了哪些文件
sudo lsof -p PID
如果是分析一个你不太了解的进程，这个命令比较有用。
可以使用 lsof -p PID | grep TCP 查看进程中的 TCP 连接信息。

4. 查看文件被哪个进程使用
使用这个命令查看一个文件被哪些进程正在使用 sudo lsof /path/to/file

Linux中我们可以使用 netstat 工具来进程网络分析
ps aux | grep nginx看下nginx进程是不是启动了

1. 查看全部端口占用情况
Linux中我们可以使用 netstat 工具来进程网络分析，netstat 命令有非常多选项

2. 查看具体端口占用情况
> sudo lsof -i :80 (注意端口80前面有个英文的冒号)

