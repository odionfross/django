from django.db import models
import datetime, re, bcrypt

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        # validate birthday and it must be in the past
        if len(postData['dob']) < 10:
            errors['dob'] = "Birthday is required"
        elif datetime.datetime.strptime(postData['dob'], "%Y-%m-%d") > datetime.datetime.now():
            errors['dob'] = "Birthday must be in the past"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be valid format!!"
        # registered email is unique
        elif User.objects.filter(email=postData['email']):
            errors['email'] = "Show email must be unique"
        if len(postData['pwd']) < 8:
            errors['pwd'] = "Password must be at least 8 characters!!"
        if postData['pwd'] != postData['confirm_pwd']:
            errors['confirm_pwd'] = "Password and confirm password do not match!!"
        return errors

    def login_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be valid format!!"
        # show error if email trying to log in does not exist
        elif not User.objects.filter(email=postData['email']):
            errors['email'] = "Email does not exist"
        # the password does not exist OR the form password is not the same as the password in the database
        elif not bcrypt.checkpw(postData['pwd'].encode(), User.objects.filter(email=postData['email'])[0].password.encode()):
            # User.objects.filter(email=postData['email'])[0].password != postData['pwd']:
            errors['pwd'] = "Password do not match our record!!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()