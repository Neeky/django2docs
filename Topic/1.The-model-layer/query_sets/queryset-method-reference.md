# django2docs

主编&作者:**蒋乐兴**

wechat:**jianglegege**

email:**1721900707@qq.com**

homepage:**http://www.sqlpy.com**

---

- [序言](#序言)
- [属性](#属性)
- [filter](#filter)
- [exclude](#exclude)
- [annotate](#annotate)
- [order_by](#order_by)
- [reverse](#reverse)
- [distinct](#distinct)
- [values](#values)
- [values_list](#values_list)
- [dates](#dates)
- [datetimes](#datetimes)
- [none](#none)
- [all](#all)
- [union](#union)
- [intersection](#intersection)
- [difference](#difference)
- [select_related](#select_related)
- [prefetch_related](#prefetch_related)
- [defer](#defer)
- [only](#only)
- [using](#using)
- [select_for_update](#select_for_update)
- [get](#get)
- [create](#create)
- [get_or_create](#get_or_create)
- [update_or_create](#update_or_create)
- [bulk_create](#bulk_create)
- [count](#count)
- [in_bulk](#in_bulk)
- [iterator](#iterator)
- [latest](#latest)
- [earliest](#earliest)
- [first](#first)
- [last](#last)
- [exists](#exists)
- [update](#update)
- [delete](#delete)


---

## 序言
   **QuerySet method reference** 主要用于讲解QuerySet对象所拥有的“属性”和“方法” 

   ---

## 属性
   **1): orderd** 用于确定当前的QuerySet对象是否是一个有序的结果集
   ```python
   bs = Blog.objects.all()
   bs.ordered
   # False
   ```

   **2): db** 用于确定当前的QuerySet对象所对应的数据库名
   ```python
   bs = Blog.objects.all()
   bs.db
   #'default'
   # 可见QuerySet对象的db属性引用的是Django的配置文件中的配置
   ```
   ```python
   #以下是使用MySQL的配置
   DATABASES = {
       'default':{
           'ENGINE': 'django.db.backends.mysql', # 后台数据库的类型
           'HOST': '127.0.0.1',                  # 后台数据库所在主机的ip我这里用本机
           'PORT': 3306,                         # 后台数据库所监听的端口
           'USER': 'appuser',                    # 连接数据库的用户名
           'PASSWORD': '123456',                 # 连接数据库的密码
           'NAME': 'tempdb',                     # 数据库中的schema名字
       }
   }
   ```

   ---

## filter
   **filter(\*\*kwargs)** 根据给定的过虑条件返回新的QuerySet对象，各个过虑条件逻辑上是`and`关系，如果要表达其它逻辑关系可以用Q对象来完成
   ```python
   bs = Blog.objects.all()
   for b in bs:
       print(b.id)
       #5
       #6
    b = bs.filter(id=5)
    b
    # <QuerySet [<Blog: b>]>
   ```

   ---

## exclude
   **exclude(\*\*kwargs)** 返回由那些不满足条件的行组成的QuerySet
   ```python
   bs = Blog.objects.all()
   for b in bs:
       print(b.id)
       #5
       #6
   b = bs.exclude(id=5) # 得到id不是5的那些行
   b
   # <QuerySet [<Blog: x>]>
   ```

   ---

## annotate
   **annotate(\*args,\*\*kwargs)** 可以完成对对象的分组聚合,返回值的类型是QuerySet
   
   如：Blog对象中并没有定义有多少个Entry对象引用了它，但是我们可以通过annotate来办到
   ```python
   qs = Blog.objects.all().annotate(entrys=Count('entry'))
   for q in qs:
       print(q.entrys)
       # ... 
       # 1
       # 1
   ```
   对应的SQl语句如下
   ```sql
   SELECT 
    `blog_blog`.`id`, 
    `blog_blog`.`name`, 
    `blog_blog`.`tagline`, 
    COUNT(`blog_entry`.`id`) AS `entrys` 
   FROM `blog_blog` 
    LEFT OUTER JOIN 
    `blog_entry` 
    ON (`blog_blog`.`id` = `blog_entry`.`blog_id`) 
   GROUP BY `blog_blog`.`id` 
   ORDER BY NULL
   ```

   ---

## order_by
   **order_by(\*fields)** 默认情况下QuerySet结果集中的次序是由Meta中定义的，如果我们要用一种新的次序来给结果集排序的话，可以用QuerySet的order_by方法来完成
   ```python
   Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline') # 注意排序列是按位置参数的形式给出的
   ```
   1): 默认是升序

   2): 在列名间加上'-'表示降序排序

   ---

## reverse
   **reverse()** 调转一个QuerySet中所有行中的次序
   ```python
   my_queryset.reverse()
   ```
   ---

## distinct
   **distinct(\*fields)** 对结果集进行去重时会用到

   ---

## values
   **values(\*fields,\*\*expression)** 返回由字典组成的QuerySet对象，它的主要目的是限制结果集中列的数量
   ```python
   Blog.objects.all().values('name','tagline')
   #<QuerySet [{'name': 'MySQL权威指南', 'tagline': 'MySQL'}, {'name': 'Python3权威指南', 'tagline': 'Python'}]>
   
   Blog.objects.all()
   #<QuerySet [<Blog: MySQL权威指南>, <Blog: Python3权威指南>]>
   ```

   values的\*\*expression还支持向annotate一样支持自定义计算
   ```python
   from django.db.models.functions import Lower
   Blog.objects.all().values(lower_name=Lower(name))
   #<QuerySet [{'lower_name': 'mysql权威指南'}, {'lower_name': 'python3权威指南'}]>
   ```

   跨Model查询
   ```python
   Entry.objects.values()
   #<QuerySet [
       {'id': 3, 'blog_id': 7, 'headline': 'MySQL权威指南', 'body_text': '', 'pub_date': datetime.date(2018, 10, 6), 'mod_date': datetime.date(2018, 10, 6), 'n_comments': 0, 'n_pingbacks': 0, 'rating': 0}, 
       {'id': 4, 'blog_id': 8, 'headline': 'Python权威指南', 'body_text': '', 'pub_date': datetime.date(2018, 10, 6), 'mod_date': datetime.date(2018, 10, 6), 'n_comments': 0, 'n_pingbacks': 0, 'rating': 0}]>

   Blog.objects.values('name','entry__headline')
   #<QuerySet [
       {'name': 'MySQL权威指南', 'entry__headline': 'MySQL权威指南'}, 
       {'name': 'Python3权威指南', 'entry__headline': 'Python权威指南'}]>
   ```

   注意values对外键引用的处理方式，Entry的blog列应该是引用着Blog对象的，但是在使用values()方法的情况下已经不在有blog这个列了，而是通过blog_id来引用的；所以要特别注意什么时候返回的是Model的实例，什么时候返回的只是一个实例的id值

   ---

## values_list
   **values_list(\*fields, flat=False, named=False)** 相比直接返回Model对象来说values方法直接返回字典已经算是比较轻量级的了，但是在数据量比较大的情况下字典要消耗的内存也是非常可观的，这个时候我们要就用到更加轻量级的数据结构来节约内存；values_list返回内元组 组成的列表
   ```python
   Blog.objects.values_list('name','entry__headline')
   # <QuerySet [('MySQL权威指南', 'MySQL权威指南'), ('Python3权威指南', 'Python权威指南')]>
   ```

   flat可以针对只查询一列的情况进行更加“抠门”的优化
   ```python
   Blog.objects.values_list('name')
   # <QuerySet [('MySQL权威指南',), ('Python3权威指南',)]> #可以看到返回值是一个列表包元组的结构
   Blog.objects.values_list('name',flat=True)
   # <QuerySet ['MySQL权威指南', 'Python3权威指南']>        #当指定flat为True的情况下Python把内部的元组都省了
   ```

   named相比flat而言不会进行那么“抠门”的优化，它以会心命名元组的形式返回结果集
   ```python
   Blog.objects.values_list('name',named=True)
   # <QuerySet [Row(name='MySQL权威指南'), Row(name='Python3权威指南')]>
   ```

   ---

## dates
   **dates(field, kind, order='ASC')** 
   ```py
   Entry.objects.values('pub_date')
   # <QuerySet [{'pub_date': datetime.date(2018, 10, 6)}, {'pub_date': datetime.date(2018, 10, 6)}]>
   ```
   kind用于控制时间的精度 year精确到年 month精确到月 dya精确到日 ...
   ```python
   Entry.objects.dates('pub_date','year')
   # <QuerySet [datetime.date(2018, 1, 1)]>
   
   Entry.objects.dates('pub_date','month')
   # <QuerySet [datetime.date(2018, 10, 1)]>
   
   Entry.objects.dates('pub_date','day')
   # <QuerySet [datetime.date(2018, 10, 6)]>
   ```

## datetimes
   **与dates方法类似只是datetimes针对的是datetimes数据类型**

   ---

## none
   **none() 直接返回空的QuerySet对象**
   ```py
   Blog.objects.none()
   # <QuerySet []>

   from django.db.models.query import EmptyQuerySet
   isinstance(Entry.objects.none(), EmptyQuerySet)
   # True
   ```

## all
   **all()** 返回当前QuerySet的一个完整拷贝
   ```py
   qs1 = Blog.objects.all()
   qs2 = qs1.all()
   id(qs1),id(qs2)
   # (4375152568, 4375745648)
   ```
   ---

## union
   **union(\*other_qs, all=False)**和数据库中的union一样，用于合并多个结果集(默认去除重复行)
   ```sql
   select 1 as a union select 1 as a;
   +---+
   | a |
   +---+
   | 1 |
   +---+
   1 row in set (0.00 sec)
   ```

   ---

## intersection
   **intersection(\*other_qs)** 交集

   ---

## difference
   **difference(\*other_qs)** 差集

   ---

## select_related
   **select_related(\*fields) 跟随外键约束一次性查询出、父表中被关联到的行、它的主要目的是为了减少对数据库的查询次数；只适用一对多，一对一关系**
   ```python
   qs = Entry.objects.filter(id=3)
   qs[0].blog
   ```
   后台SQL
   ```sql
   SELECT 
    `blog_entry`.`id`, 
    `blog_entry`.`blog_id`, 
    `blog_entry`.`headline`, 
    `blog_entry`.`body_text`, 
    `blog_entry`.`pub_date`, 
    `blog_entry`.`mod_date`, 
    `blog_entry`.`n_comments`, 
    `blog_entry`.`n_pingbacks`, 
    `blog_entry`.`rating` 
   FROM `blog_entry` WHERE `blog_entry`.`id` = 3  LIMIT 1
   
   SELECT 
    `blog_blog`.`id`, 
    `blog_blog`.`name`, 
    `blog_blog`.`tagline` 
   FROM `blog_blog` WHERE `blog_blog`.`id` = 7
   ```
   可见后台分了两次查询来完成`qs[0].blog`

   ```python
   qs = Entry.objects.select_related('blog').filter(id=3)
   qs[0].blog
   ```
   后台SQL
   ```sql
   SELECT 
    `blog_entry`.`id`, 
    `blog_entry`.`blog_id`, 
    `blog_entry`.`headline`, 
    `blog_entry`.`body_text`, 
    `blog_entry`.`pub_date`, 
    `blog_entry`.`mod_date`, 
    `blog_entry`.`n_comments`, 
    `blog_entry`.`n_pingbacks`, 
    `blog_entry`.`rating`, 
    `blog_blog`.`id`, 
    `blog_blog`.`name`, 
    `blog_blog`.`tagline` 
   FROM `blog_entry` 
   INNER JOIN `blog_blog` 
    ON (`blog_entry`.`blog_id` = `blog_blog`.`id`) 
   WHERE `blog_entry`.`id` = 3  LIMIT 1
   ```

   **可见select_related方法要求传入的是一个外键、如果要一直外键下去可以用 __ 来连接各个外键**
   ```python
   from django.db import models
   
   class City(models.Model):
       # ...
       pass
   
   class Person(models.Model):
       # ...
       hometown = models.ForeignKey(
           City,
           on_delete=models.SET_NULL,
           blank=True,
           null=True,
       )
   
   class Book(models.Model):
       # ...
       author = models.ForeignKey(Person, on_delete=models.CASCADE)

   b = Book.objects.select_related('author__hometown').get(id=4)
   p = b.author         # Doesn't hit the database.
   c = p.hometown       # Doesn't hit the database.
   ```

   ---

## prefetch_related
   **prefetch_related(\*lookups) 与select_related的目标一样，都是要减少对数据库的查询次数；不同的是prefetch_related只适用于多对多关系**

   ---

## defer
   **defer(\*fields) 用于指定哪些列不必要返回**
   ```python
   b = Blog.objects.all()
   b
   ```
   默认是返回所有列的
   ```sql
   SELECT 
    `blog_blog`.`id`, 
    `blog_blog`.`name`, 
    `blog_blog`.`tagline` 
   FROM `blog_blog`  LIMIT 21
   ```

   defer可以告诉django那些列并不需要
   ```python
   b = Blog.objects.defer('tagline').all()
   b
   ```
   ```sql
   SELECT `blog_blog`.`id`, `blog_blog`.`name` FROM `blog_blog`  LIMIT 21
   ```

   ---

## only
   **only(\*fields) 与defer相反，给要需要的列**
   ```python
   b = Blog.objects.only('name').all()
   b
   ```
   后台SQL
   ```sql
   SELECT `blog_blog`.`id`, `blog_blog`.`name` FROM `blog_blog`  LIMIT 21
   ```

   ---

## using
   **using(alias) 指定查询使用的连接参数**
   ```python
   Entry.objects.all() # 不加的话就使用defaults
   ```
   ```python
   #以下是使用MySQL的配置
   DATABASES = {
       'default':{
           'ENGINE': 'django.db.backends.mysql', # 后台数据库的类型
           'HOST': '127.0.0.1',                  # 后台数据库所在主机的ip我这里用本机
           'PORT': 3306,                         # 后台数据库所监听的端口
           'USER': 'appuser',                    # 连接数据库的用户名
           'PASSWORD': '123456',                 # 连接数据库的密码
           'NAME': 'tempdb',                     # 数据库中的schema名字
       }
   }
   ```

   ---

## select_for_update
   **select_for_update(nowait=False, skip_locked=False, of=()) 锁定读**

   ---

## raw
   **raw(raw_query, params=None, translations=None) 用于执行SQL语句**
   ```python
   bs = Blog.objects.raw("select id, name,tagline from blog_blog;")
   for b in bs:
       print(b.name,b.tagline)
       #MySQL权威指南 MySQL
       #Python3权威指南 Python
   ```
   查询列一定要包含主键，不然会报错

   ---

## get
   **get(\*\*kwargs) 返回匹配过滤参数的对象**

   1): 如果返回了多行会报`MultipleObjectsReturned`
   
   2): 如果一行都没有返回报`DoesNotExist` **所以在使用get的时候要对这两种异常进行处理**

   ```python
   from django.core.exceptions import ObjectDoesNotExist
   try:
       b = Blog.objects.get(id=9)
   except ObjectDoesNotExist as e:
       print("this is in exception ")

   # 以下写法也成立
   try:
       b = Blog.objects.get(id=9)
   except Blog.DoesNotExist as e:
      print("this is in exception")
   ```

   ---

## create
   **create(\*\*kwargs) 相对先创建实例再save的两步走的方式来说create可以一步完成**
   ```python
   Blog.objects.create(name='C#',tagline='C#-hello world')
   # <Blog: C#>
   ```
   ---

## get_or_create
   **get_or_create(defaults=None, \*\*kwargs) 根据给出的条件查询一行，如果这一行不存在就创建它，返回值为一个无组(object,created) object是查询或创建出来的对象，created是一个标识，如果它为true说明对象是create出来的，而不是查询出来的**
   ```python
   try:
       obj = Person.objects.get(first_name='John', last_name='Lennon')
   except Person.DoesNotExist:
       obj = Person(first_name='John', last_name='Lennon', birthday=date(1940, 10, 9))
       obj.save()
   ```
   get_or_create的等价写法
   ```python
   obj, created = Person.objects.get_or_create(
       first_name='John',
       last_name='Lennon',
       defaults={'birthday': date(1940, 10, 9)},
   )
   ```
   get_or_create也可以写的特别复杂
   ```python
   from django.db.models import Q
   
   obj, created = Person.objects.filter(
       Q(first_name='Bob') | Q(first_name='Robert'),
   ).get_or_create(last_name='Marley', defaults={'first_name': 'Bob'})
   ```

   ---

## update_or_create
   **update_or_create(defaults=None, \*\*kwargs) 如果能查询到对应的行就更新它，如果不能就创建它**
   ```python
   defaults = {'first_name': 'Bob'}
   try:
       obj = Person.objects.get(first_name='John', last_name='Lennon')
       for key, value in defaults.items():
           setattr(obj, key, value)
       obj.save()
   except Person.DoesNotExist:
       new_values = {'first_name': 'John', 'last_name': 'Lennon'}
       new_values.update(defaults)
       obj = Person(**new_values)
       obj.save()
   ```
   对于update_or_create就可以这样写
   ```python
   obj, created = Person.objects.update_or_create(
       first_name='John', last_name='Lennon',
       defaults={'first_name': 'Bob'},
   )
   ```

   ---

## bulk_create
   **bulk_create(objs, batch_size=None) 批量创建对象**
   ```python
   Entry.objects.bulk_create([
       Entry(headline='This is a test'),
       Entry(headline='This is only a test'),
   ])
   ```
   关于batch_size
   ```python
   from itertools import islice
   
   batch_size = 100
   objs = (Entry(headline='Test %s' % i) for i in range(1000))
   while True:
       batch = list(islice(objs, batch_size))
       if not batch:
           break
       Entry.objects.bulk_create(batch, batch_size)
   ```

   ---

## count
   **count() 返回QuerySet匹配到的行数**
   ```python
   Entry.objects.filter(headline__contains='Lennon').count()
   ```

   ---

## in_bulk
   **in_bulk(id_list=None, field_name='pk') 根据主键的列表查询行**
   ```python
   Blog.objects.in_bulk([9,8])
   # {8: <Blog: Python3权威指南>, 9: <Blog: C#>}
   ```

   ---


## iterator
   **iterator(chunk_size=2000) 以游标的形式进行查询，以优化客户端的内存使用**
   ```python
   bq = Blog.objects.all().iterator()
   type(bq)
   # <class 'generator'> 因为iterator返回的是一个生成器，所以它的返回结果只能消费一轮

   bq = Blog.objects.all().iterator()
   for b in bq:
       print(type(b),b.name)
   
   <class 'blog.models.Blog'> MySQL权威指南
   <class 'blog.models.Blog'> Python3权威指南
   <class 'blog.models.Blog'> C#
   ```

   ---

## latest
   **latest(\*fields) 根据model中的时间列返回最新的行**
   ```python
   Entry.objects.latest('pub_date')
   ```

   ---

## earliest
   **earliest(*fields) 与latest相反，返回最老的行**

   ---

## first
   **first() 如果Queryset为空，返回None;如果不为空就返回给定次序的第一行**
   ```python
   p = Article.objects.order_by('title', 'pub_date').first()
   try:
       p = Article.objects.order_by('title', 'pub_date')[0]
   except IndexError:
       p = None
   ```

   ---

## last
   **与first相反**

   ---

## exists
   **exists() 如果QuerySet包含任意内容就返回True,如果什么都没有就返回Flase**

   ---

## update
   **update(\*\*kwargs) 更新QuerySet中的行到数据库、返回受影响的行数**
   ```python
   Entry.objects.filter(pub_date__year=2010).update(comments_on=False)
   # 1
   ```
   ---

## delete
   **delete() 删除QuerySet中的行,返回被删除的行数，和被删除的行组成的字典**
   ```python
   Entry.objects.filter(blog=b).delete()
   # (4, {'weblog.Entry': 2, 'weblog.Entry_authors': 2})
   ```
   ---
