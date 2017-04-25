from __future__ import unicode_literals
from django.db import models
import re,bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration(self,first_name,last_name,email,password,conpassword):
        if (first_name and len(first_name)>=2 and first_name.isalpha()):
            if (last_name and len(last_name)>=2 and last_name.isalpha()):
                if ( email and EMAIL_REGEX.match(email)):
                    if (password and len(password) >=8 and password == conpassword):
                        mypassword = password.encode()
                        hashed = bcrypt.hashpw(mypassword,bcrypt.gensalt())
                        list =[hashed]
                        return list
        else:
            return None
    def login(self,userPassword,password):
        dabasePassword = userPassword.encode()
        print dabasePassword
        mypassword = password.encode()
        print mypassword
        print bcrypt.hashpw(mypassword,dabasePassword)
        if(bcrypt.hashpw(mypassword,dabasePassword)==dabasePassword):
            print "hello"
            return True
        else:
            print "wrong"
            return False


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # userIntance.secrets_liked.all()

class Secret(models.Model):
    secret_message = models.CharField(max_length=45)
    user = models.ForeignKey(User, related_name="secrets")
    list_of_users_liked=models.ManyToManyField(User,related_name='list_of_secrets_liked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # secretInstance.likes.all()
