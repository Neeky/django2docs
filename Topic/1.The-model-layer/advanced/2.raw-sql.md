# django2docs

主编&作者:**蒋乐兴**

wechat:**jianglegege**

email:**1721900707@qq.com**

homepage:**http://www.sqlpy.com**

---
- [简介](#简介)
- [raw方法](#raw方法)
- [给raw方法传参数](#给raw方法传参数)
- [直接执行SQL语句](#直接执行SQL语句)
---


## 简介
   **作为一个SQLServer开发出身的我，只能说Django的ORM已经非常优秀了，但是有一些问题写SQL可能会更加直接，特别是在一些复杂查询的场景下。好在Django并没有把我们直接执行查询的这条路给堵死；它更是提供了两个方便的路径来给我们执行SQL语句。**

   路径1：Manager.raw()

   路径2：connection.cursor()

   ---

## raw方法
   **Manager.raw(raw_query, params=None, translations=None)** 接收SQL语句返回RawQuerySet对象

   ```python
   class Person(models.Model):
       name = models.CharField(max_length=8)
       age = models.PositiveSmallIntegerField()
   
       def __str__(self):
           return "name = {0} age = {1}".format(self.name,self.age)
   ```
   ```python
   Person.objects.all()
   # <QuerySet [<Person: name = 法拉利 age = 16>, <Person: name = 牛顿 age = 66>, <Person: name = 开尔文 age = 88>]>

   # 试着用Raw方法来找出这些值
   # 可以看到要查哪个表就通过哪个表的Manager对象来、还有返回的对象是有类型的
   rs = Person.objects.raw("select id,name,age from blog_person;")
   type(rs)
   # <class 'django.db.models.query.RawQuerySet'>
   for i in rs:
       print(type(i),i.name,i.age)
   
   # <class 'blog.models.Person'> 法拉利 16
   # <class 'blog.models.Person'> 牛顿 66
   # <class 'blog.models.Person'> 开尔文 88
   ```
   可以看到返回的行直接被包装成了对应Model的实例，另一个要注意的地方是返回的列一定要包含主键不然会报错的；那么我们是否可以自己造一行出来呢？

   ```python
   rs = Person.objects.raw("select 100 as id,'蒋乐兴' as name,16 as age from blog_person;")
   print(type(rs[0]),rs[0].name,rs[0].age)
   # <class 'blog.models.Person'> 蒋乐兴 16
   ```

   ---

## 给raw方法传参数
   **raw方法的params参数可以给SQL语句传递参数，使用这种方式传递参数可以防止SQL注入攻击**
   ```python
   ps = Person.objects.raw("select id,name,age from blog_person where name =%s;",params=['牛顿'])
   p = ps[0]

   p.name
   # '牛顿'
   p.age
   # 66
   p.id
   # 2
   ```

   ---


## 直接执行SQL语句
   **直接执行SQL的方式也十分简单，直接调整驱动程序就可以了；**
   ```python
   from django.db import connection

   with connection.cursor() as cursor:
       cursor.execute("select name,age from blog_person where name=%s;",params=['牛顿'])
       p = cursor.fetchone()

   p
   # 真的是省内存呀，直接返回的元组
   # ('牛顿', 66)
    
   ```
   ---



