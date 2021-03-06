# Generated by Django 3.0.3 on 2020-03-11 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='QuoteType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('ins', 'Inspiring'), ('fun', 'Funny'), ('mot', 'Motivational'), ('dem', 'Demotivational'), ('tru', 'Truthful')], help_text='Quote category', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('user', models.CharField(max_length=100, null=True)),
                ('created_date', models.DateField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quote.Author')),
                ('quotetype', models.ManyToManyField(help_text='Please select a quote type:', to='quote.QuoteType')),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]
