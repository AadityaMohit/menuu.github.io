from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    pincode=models.IntegerField()
    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    feedback=models.TextField()
    def __str__(self):
        return self.feedback
    
    
class Cod(models.Model):
    cardnumber=models.IntegerField()
    expirationDate=models.DateField()
    cvv =models.IntegerField()
    cardHolderName=models.CharField(max_length=30)
    def __str__(self):
        return self.cardHolderName
    