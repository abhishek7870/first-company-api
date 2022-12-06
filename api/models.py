from django.db import models

# Create your models here.
# create company modal


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('It', 'It'),
                                                     ('Non it', 'Non it'),
                                                     ('Mobile Phone',
                                                      'Mobile Phone')
                                                     ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    mobile_number = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=100, choices=(('Manager', 'Manager'),
                                                         ('Software Enginer', 'SD'),
                                                         ('Project Leader', 'PL')))
    company=models.ForeignKey(Company, on_delete=models.CASCADE)