from django.db import models
from users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from django.conf import settings


#Income model (stores user earnings)
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.source


#Expense model (stores user spending)
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category
    

#Advisory model (financial tips linked to users)
class Advisory(models.Model):
    #links each tip to a student
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="advisories")
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.category}"


#Automated saving model (stores calculated savings per income)
class AutomatedSaving(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    income_source = models.CharField(max_length=100) 
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_calculated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Saved {self.saved_amount}"

#Signal: automatically creates savings when new income is added
@receiver(post_save, sender=Income)
def create_automated_saving(sender, instance, created, **kwargs):
    if created:
         #Calculate 15% saving from income
        saving_value = instance.amount * Decimal('0.15')
        
        #Create AutomatedSaving record
        AutomatedSaving.objects.create(
            user=instance.user,
            income_source=instance.source,
            saved_amount=saving_value
        )