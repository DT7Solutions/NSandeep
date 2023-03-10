# Generated by Django 4.1.5 on 2023-01-04 10:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sandeepapp', '0002_about_brandslider_ourclientreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='heading', max_length=30)),
                ('Created', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(default='title', max_length=225)),
                ('Image1', models.ImageField(upload_to='uploads/')),
                ('Image2', models.ImageField(upload_to='uploads/')),
                ('Description1', models.CharField(max_length=2000)),
                ('Description2', models.CharField(max_length=2000)),
                ('Tags', models.CharField(max_length=100)),
                ('CreatedName', models.CharField(max_length=100)),
                ('Create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='sandeepapp.category')),
            ],
        ),
    ]
