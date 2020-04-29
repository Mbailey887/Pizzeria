from django.db import models

# Create your models here.
class PizzaName(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
        
class Topping(models.Model):
    pizzaname = models.ForeignKey(PizzaName, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        return f"{self.name[:50]}..."