# Generated by Django 2.0.4 on 2018-04-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.DateField()),
                ('To', models.DateField()),
                ('Type', models.TextField(max_length=8)),
                ('requirements', models.TextField(max_length=10)),
                ('adults', models.CharField(max_length=3)),
                ('children', models.CharField(max_length=3)),
                ('name', models.TextField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
