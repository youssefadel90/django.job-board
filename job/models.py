from email.policy import default
from pydoc import describe
from unicodedata import name
from django.db import models



# Create your models here.
JOB_TYPE = (
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
)
 

class job (models.Model): #table
    title = models.CharField(max_length=100)  #column
    # location
    job_type = models.CharField(max_length=15, choices= JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacance = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    exeperince = models.IntegerField(default=1)
    category = models.ForeignKey('category', on_delete = models.CASCADE ,)




    def __str__(self):
        return self.title




class category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name