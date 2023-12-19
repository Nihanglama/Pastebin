from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=300,null=True,blank=False)
    email=models.CharField(max_length=100,null=True,blank=False)
    picture=models.ImageField(default='noprofile.jpg')

    def __str__(self):
        return self.name


def create(sender,instance,created,*args, **kwargs):
    if created:
        Customer.objects.create(user=instance,name=instance.username,email=instance.email)
post_save.connect(create,sender=User)


class Pasteitem(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=300,null=True,blank=False)
    pasteitems=models.TextField(null=True,blank=False)
    added_time=models.DateField(auto_now_add=True,null=True)
    langauge=(
        ('py','python'),
        ('C++','Cplusplus'),
        ('C','Cprogramming'),
        ('java','Java'),
        ('txt','Text'),
    )
    visibility=(
        ('public','Public'),
        ('private','Private'),
    )
    languages=models.CharField(choices=langauge,null=True,max_length=100,blank=False,default='python')
    visible=models.CharField(choices=visibility,null=True,max_length=100,blank=False,default='Public')


    def __str__(self):
        return self.title

