# Generated by Django 5.0.6 on 2024-07-03 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0002_auto_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='auto',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Auto',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
