# Generated by Django 3.0.3 on 2020-03-23 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quotetype',
            field=models.ManyToManyField(to='quote.QuoteType'),
        ),
    ]