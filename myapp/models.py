from django.db import models

# Create your models here.
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Topic(models.Model):
    name = models.CharField(max_length=200)
    length = models.IntegerField(default=12)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, related_name='courses',
                              on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return '{} by {}'.format(self.title, self.topic, self.for_everyone, self.description)


class Student(User):
    LVL_CHOICES = [
        ('HS', 'High School'),
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('ND', 'No Degree'),
    ]
    level = models.CharField(choices=LVL_CHOICES, max_length=2, default='HS')
    address = models.CharField(max_length=300)
    province = models.CharField(max_length=2, blank=True, default='ON')
    registered_courses = models.ManyToManyField(Course, blank=True)
    interested_in = models.ManyToManyField(Topic)


class Order(models.Model):
    ORDER_CHOICES = [
        (0, 'Cancelled'),
        (1, 'Confirmed'),
        (2, 'On Hold')
    ]
    order_status = models.IntegerField(choices=ORDER_CHOICES, max_length=2, default=1)
    courses = models.ManyToManyField(Course)
    Student = models.ForeignKey(Student, related_name='students',
                                on_delete=models.CASCADE)
    order_date = models.DateField(default=timezone.now())

    def __str__(self):
        return '{} by {}'.format(self.Student, self.courses.all())

    def total_cost(self):
        cost = 0
        for course in self.course.all():
            cost = cost + course.price
            return cost
