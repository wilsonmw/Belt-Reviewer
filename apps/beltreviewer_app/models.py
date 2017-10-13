from __future__ import unicode_literals

from django.db import models

import re

import bcrypt

# Create your models here.

class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status':True, 'errors':[]}
        if not postData['first_name'] or len(postData['first_name']) < 2:
            results['status']=False
            results['errors'].append("First Name must be more than one character.")
        if not postData['last_name'] or len(postData['last_name']) < 2:
            results['status']=False
            results['errors'].append("Last Name must be more than one character.")
        if not postData['email'] or not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", postData['email']):
            results['status']=False
            results['errors'].append("Email address is not valid.")
        if not postData['password'] or len(postData['password']) < 8 or postData['password'] != postData['confirmpw']:
            results['status']=False
            results['errors'].append("Password must be at least 8 characters, and both password fields must match.")
        if results['status']==True:
            user = User.objects.filter(email=postData['email'].lower())
            if len(user)!=0:
                results['status']=False
                results['errors'].append('Registration failed. Please try again.')
                return results
            else:
                hashedpw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
                User.objects.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'].lower(), password=hashedpw)
                results['errors'].append("Registration successful. Please log in.")
                return results
        return results

    def loginVal(self, postData):
        results = {'status':True, 'errors':[], 'user':{}, 'id':""}
        if not postData['email'] or not postData['password']:
            results['status']=False
            results['errors'].append("Login failed. Please try again.")
            return results
        else:
            user = User.objects.filter(email=postData['email'].lower())
            print user
            if bcrypt.hashpw(postData['password'].encode(), user[0].password.encode()) != user[0].password:
                results['status']=False
                results['errors'].append("Login failed. Please try again.")
                return results
            else:
                results['user']=user
                results['id']=user[0].id             
                return results



class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = UserManager()
