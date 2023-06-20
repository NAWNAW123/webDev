from django.db import models
# Create your models here.
       
# class Customer(models.Model):
#     Customer_ID =models.AutoField(primary_key=True)
#     Customer_name= models.CharField(max_length=100)
#     Customer_address=models.CharField(max_length=100)
#     Customer_phone=models.IntegerField()
#     def _str_(Self):
#         return Self.Customer

class Phone(models.Model):
    Phone_name =models.CharField(max_length=100)
    Phone_price =models.IntegerField()
    Phone_buy =models.CharField(max_length)
    def _str_(Self):
        return Self.Phone






        


        
