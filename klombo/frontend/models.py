# frontend/models.py
from django.db import models
from django.urls import reverse

# Create your models here.    
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username   = models.CharField(max_length=64, unique=True,null=False)
    password   = models.CharField(max_length=512,null=False)
    contact   = models.CharField(max_length=512,null=False)
    firstname   = models.CharField(max_length=512,null=False)
    lastname   = models.CharField(max_length=512,null=False)
    time   = models.DateTimeField(auto_now=True)



class Group(models.Model):
    id = models.AutoField(primary_key=True)
    userid   = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title   = models.CharField(max_length=512,default='NULL')
    description   = models.CharField(max_length=512,default='NULL')
    privacy   = models.CharField(max_length=512,default='NULL')
    time   = models.DateTimeField(auto_now=True)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    userid   = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    groupid   = models.CharField(max_length=512,default='',null=True)
    eventid   = models.CharField(max_length=120,default='',null=True)
    privacy   = models.CharField(max_length=120,default='0')
    text   = models.CharField(max_length=512,default='NULL')
    image   = models.CharField(max_length=512,default='',null=True)
    time   = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    userid   = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    postid   = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    text   = models.CharField(max_length=512,default='NULL')
    time   = models.DateTimeField(auto_now=True)

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    userid   = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    commentid   = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
    )
    time   = models.DateTimeField(auto_now=True)

class UsersInGroup(models.Model):
    id = models.AutoField(primary_key=True)
    userid   = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    groupid   = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    time   = models.DateTimeField(auto_now=True)

class Login(models.Model):
    id = models.AutoField(primary_key=True)
    userid   = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    type   = models.CharField(max_length=120,default='NULL')
    time   = models.DateTimeField(auto_now=True)

class Friend(models.Model):
    id = models.AutoField(primary_key=True)
    userid   = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    userid2   = models.CharField(max_length=512,default='NULL')
    type   = models.CharField(max_length=120,default='NULL')
    time   = models.DateTimeField(auto_now=True)

class FriendRequest(models.Model):
    id = models.AutoField(primary_key=True)
    userid   = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    userid2   = models.CharField(max_length=512,default='NULL')
    time   = models.DateTimeField(auto_now=True)

class GroupRequest(models.Model):
    id = models.AutoField(primary_key=True)
    userid   = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    userid2   = models.CharField(max_length=512,default='NULL')
    time   = models.DateTimeField(auto_now=True)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    userid   = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title   = models.CharField(max_length=512,default='NULL')
    description   = models.CharField(max_length=512,default='NULL')
    privacy   = models.CharField(max_length=512,default='NULL')
    time   = models.DateTimeField(auto_now=True)

class LoginCookie(models.Model):
    id = models.AutoField(primary_key=True)
    data   = models.CharField(max_length=512, unique=True,null=False)
    username   = models.CharField(max_length=512,null=False)
    time   = models.DateTimeField(auto_now=True)