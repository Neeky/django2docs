from django.db import models
from django.utils import timezone

# Create your models here.


#class Person(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#
#    #每一个类的属性都会被映射成表中的列
#


#class Musician(models.Model):
#    first_name = models.CharField(max_length=50)
#    last_name = models.CharField(max_length=50)
#    instrument = models.CharField(max_length=100)
#
#class Album(models.Model):
#    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
#    name = models.CharField(max_length=100)
#    release_date = models.DateField()
#    num_stars = models.IntegerField()


#class Person(models.Model):
#    SHIRT_SIZES = (
#        ('S', 'Small'),
#        ('M', 'Medium'),
#        ('L', 'Large'),
#    )
#    name = models.CharField(max_length=60)
#    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

#class Person(models.Model):
#    SHIRT_SIZES = (
#        ('S', 'Small'),
#        ('M', 'Medium'),
#        ('L', 'Large'),
#    )
#    name = models.CharField(max_length=60)
#    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
#    birth_day = models.DateTimeField(default=timezone.now) # 给person 加了一个默认的生日，这个生日是动计算的

#class Person(models.Model):
#    SHIRT_SIZES = (
#        ('S', 'Small'),
#        ('M', 'Medium'),
#        ('L', 'Large'),
#    )
#    name = models.CharField(max_length=60)
#    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
#    birth_day = models.DateTimeField(default=timezone.now) 


#class Fruit(models.Model):
#    name = models.CharField(max_length=100, primary_key=True)

#class Manufacturer(models.Model):
#    pass
#
#class Car(models.Model):
#    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
#


#class Topping(models.Model):
#    # ...
#    pass
#
#class Pizza(models.Model):
#    # ...
#    toppings = models.ManyToManyField(Topping)
#

#class Person(models.Model):
#    name = models.CharField(max_length=128)
#
#    def __str__(self):
#        return self.name
#
#class Group(models.Model):
#    name = models.CharField(max_length=128)
#    members = models.ManyToManyField(Person, through='Membership')
#
#    def __str__(self):
#        return self.name
#
#class Membership(models.Model):
#    person = models.ForeignKey(Person, on_delete=models.CASCADE)
#    group = models.ForeignKey(Group, on_delete=models.CASCADE)
#    date_joined = models.DateField()
#    invite_reason = models.CharField(max_length=64)

#class Place(models.Model):
#    name = models.CharField(max_length=50)
#    address = models.CharField(max_length=80)
#
#    def __str__(self):
#        return "%s the place" % self.name
#
#class Restaurant(models.Model):
#    place = models.OneToOneField(
#        Place,
#        on_delete=models.CASCADE,
#        primary_key=True,
#    )
#    serves_hot_dogs = models.BooleanField(default=False)
#    serves_pizza = models.BooleanField(default=False)
#
#    def __str__(self):
#        return "%s the restaurant" % self.place.name
#
#class Waiter(models.Model):
#    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#    name = models.CharField(max_length=50)
#
#    def __str__(self):
#        return "%s the waiter at %s" % (self.name, self.restaurant)

#class Person(models.Model):
#    first_name = models.CharField(max_length=50)
#    last_name = models.CharField(max_length=50)
#    birth_date = models.DateField()
#
#    def baby_boomer_status(self):
#        "Returns the person's baby-boomer status."
#        import datetime
#        if self.birth_date < datetime.date(1945, 8, 1):
#            return "Pre-boomer"
#        elif self.birth_date < datetime.date(1965, 1, 1):
#            return "Baby boomer"
#        else:
#            return "Post-boomer"
#
#    @property
#    def full_name(self):
#        "Returns the person's full name."
#        return '%s %s' % (self.first_name, self.last_name)
#
#
#class Blog(models.Model):
#    name = models.CharField(max_length=100)
#    tagline = models.TextField()
#
#    def save(self, *args, **kwargs):
#        if self.name == "Yoko Ono's blog":
#            return # Yoko shall never have her own blog!
#        else:
#            super().save(*args, **kwargs)  # Call the "real" save() method.


#class CommonInfo(models.Model):
#    name = models.CharField(max_length=30)
#
#class Person(CommonInfo):
#    age = models.IntegerField()

#class CommonInfo(models.Model):
#    name = models.CharField(max_length=100)
#    age = models.PositiveIntegerField()
#
#    class Meta:
#        abstract = True
#
#class Student(CommonInfo):
#    home_group = models.CharField(max_length=5)
#

#class Person(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#
#class MyPerson(Person):
#    class Meta:
#        proxy = True
#
#    def get_full_name(self):
#        # ...
#        return self.first_name + self.last_name
#

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)

class BookReview(Book, Article):
    pass
    
