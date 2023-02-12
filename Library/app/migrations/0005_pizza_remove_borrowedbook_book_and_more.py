# Generated by Django 4.1.5 on 2023-02-08 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_borrowedbook_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.PositiveIntegerField(default=2023)),
                ('crust', models.CharField(max_length=250)),
                ('sauce', models.PositiveIntegerField(default=1)),
                ('cheese', models.CharField(max_length=250)),
                ('toppings', models.CharField(choices=[('Pepperoni', 'Pepperoni'), ('Pineapple', 'Pineapple'), ('Peppers', 'Peppers'), ('Mushrooms', 'Mushrooms'), ('Onions', 'Onions'), ('Margherita', 'Margherita')], default=None, max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='borrowedbook',
            name='book',
        ),
        migrations.RemoveField(
            model_name='borrowedbook',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BorrowedBook',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]