from django.db import models

class Dish(models.Model):
    code = models.CharField(max_length=5, null=False, primary_key=True)
    name = models.CharField(max_length=200)
    rating = models.IntegerField()
    kkal = models.IntegerField()
    price = models.FloatField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Dish"

class Calls(models.Model):
    code_call = models.CharField(max_length=5, null=False, primary_key=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Calls"

class Call(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Call"