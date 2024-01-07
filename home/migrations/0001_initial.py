# Generated by Django 4.2.5 on 2023-11-04 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskTitle', models.CharField(max_length=255)),
                ('TaskDesc', models.TextField(max_length=255)),
                ('Curr_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
