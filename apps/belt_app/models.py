from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register(self, postInfo):
        message = []
        if len(postInfo['first_name']) < 2 or len(postInfo['last_name']) < 2:
            message.append("Name must be longer than 2 characters")
        if not postInfo['first_name'].isalpha():
            message.append("Name must contain letters only")
        if not postInfo['last_name'].isalpha():
            message.append("Last Name is invalid, contains non alphabet characters.")
        if len(postInfo['password']) < 8:
            message.append('Password must be longer than 8 characters.')
        if not EMAIL_REGEX.match(postInfo['email']):
            message.append("Please enter a valid email")
        if postInfo['password'] != postInfo['confirm_password']:
            message.append("Passwords Must Match!")
        return message
    #Created an array of messages and append all error messages. Later on, these messages will be called in the views.py file. If the array is empty, the user information will be created inside the database by running the 'else' condition.

    def verify(self, email, password):
        message = []
        user_pass =  User.marvin.get(email=email)
        if not User.marvin.filter(email=email):
            message.append("Invalid Email!")
        else:
            if password != user_pass.password:
                message.append("Invalid Password!")
        return message


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    birthday = models.DateField(auto_now=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    marvin = UserManager()

class Quote(models.Model):
    message = models.TextField(max_length=1000)
    quoted_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    # the userManager is a User(the class/table) is a property of the UserManager class.
