# Generated by Django 3.2.8 on 2021-11-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vetoffice', '0002_auto_20211104_1213'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['owner']},
        ),
        migrations.AlterField(
            model_name='breed',
            name='animal',
            field=models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Reptile', 'Reptile'), ('Rabbit', 'Rabbit'), ('Fish', 'Fish'), ('Unknown', 'Unkown')], default='Unknown', max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='animal_type',
            field=models.CharField(choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Reptile', 'Reptile'), ('Rabbit', 'Rabbit'), ('Fish', 'Fish'), ('Unknown', 'Unkown')], default='Unkown', max_length=50),
        ),
    ]
