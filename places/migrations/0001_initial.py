# Generated by Django 4.1.4 on 2023-07-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='static')),
                ('desc', models.TextField()),
                ('amt', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
