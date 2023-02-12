from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Pizza(models.Model):
   id = models.AutoField(primary_key=True)
   toppings = models.ManyToManyField(Topping, blank=True)
   
   # Crust
   Normal = 'Normal'
   Thin = 'Thin'
   Thick = 'Thick'
   
   Crust_Choices = [
        (Normal, 'Normal'),
        (Thin, 'Thin'),
        (Thick, 'Thick'),
    ]

   crust = models.CharField(
        max_length=15,
        choices=Crust_Choices,
        default=None,
    )

   # Size
   Small = 'Small'
   Medium = 'Medium'
   Large = 'Large'
   
   Size_Choices = [
        (Small, 'Small'),
        (Medium, 'Medium'),
        (Large, 'Large'),
    ]

   size = models.CharField(
        max_length=15,
        choices=Size_Choices,
        default=None,
    )
    
   #Sauce
   Tomato = 'Tomato'
   Barb = 'BBQ'
   Chilli = 'Chilli'
   
   Sauce_Choices = [
        (Tomato, 'Tomato'),
        (Barb, 'BBQ'),
        (Chilli, 'Chilli'),
    ]

   sauce = models.CharField(
        max_length=15,
        choices=Sauce_Choices,
        default=None,
    )

   # Cheese
   Mozzarella = 'Mozzarella'
   Cheddar = 'Cheddar'
   Gorgonzola = 'Gorgonzola'
   Provolone = 'Provolone'
   
   Cheese_Choices = [
        (Mozzarella, 'Mozzarella'),
        (Cheddar, 'Cheddar'),
        (Gorgonzola, 'Gorgonzola'),
        (Provolone, 'Provolone'),
    ]

   cheese = models.CharField(
        max_length=15,
        choices=Cheese_Choices,
        default=None,
    )

   def __str__(self):
       return f'Pizza with {self.crust} crust, {self.sauce} sauce, and {self.cheese} cheese. Toppings: {", ".join([topping.name for topping in self.toppings.all()])}'
