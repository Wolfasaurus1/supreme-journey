from django.db import models

'''
The following tables replace the LAR excel sheet(s)
'''
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class IR(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class LAR(models.Model):
    name = models.CharField(max_length=100)

class PersonIR(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    ir = models.ForeignKey(IR, on_delete=models.CASCADE)
    addition_date = models.DateField()

class IRLAR(models.Model):
    ir = models.ForeignKey(IR, on_delete=models.CASCADE)
    lar = models.ForeignKey(LAR, on_delete=models.CASCADE)



class Request(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    ir = models.ForeignKey(IR, on_delete=models.CASCADE)
    justification = models.TextField()
    status = models.CharField(max_length=300)