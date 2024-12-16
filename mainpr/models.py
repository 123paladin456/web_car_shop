from django.db import models

# Create your models here.
class Brend(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Model(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Car(models.Model):
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    fuel = models.CharField(max_length=10, choices=[("benzin","бензин"),("gaz", "газ"),("dizil","дизель"), ("electro","електричество")])
    date = models.DateField()
    trasmission = models.CharField(max_length=20, choices=[("mehanic","механика"),("automat","автомат"),("robot","робот")])
    image = models.ImageField()
    def __str__(self):
        return f"{self.model}"