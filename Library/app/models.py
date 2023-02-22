from django.db import models

class Topping(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Crust(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Size(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Sauce(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Cheese(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE, default='Regular')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, default='Medium')
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE, default='Tomato')
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE, default='Mozzarella')

    def __str__(self):
        return f'A {self.cheese} Cheese Pizza with {self.sauce} Sauce, {self.crust} Crust and {self.size} in Size.'


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
   
    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    paid = models.BooleanField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        if self.paid:
            return f'{self.pizza} // Ordered by {self.customer} // Paid'
        else:
            return f'{self.pizza} // Ordered by {self.customer} // Not Paid'
