from django.db import models
import datetime

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Show title must be at least 2 characters"
        elif Show.objects.filter(title=postData['title']):
            errors['title'] = "Show title must be unique"
        if len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters"
        if len(postData['desc']) != 0 and len(postData['desc']) < 10:
            errors['desc'] = "Description must at least 10 characters"
        if len(postData['date']) < 10:
            errors['date'] = "Release date is required"
        elif datetime.datetime.strptime(postData['date'], "%Y-%m-%d") > datetime.datetime.now():
            errors['date'] = "Release date must be in the past"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()