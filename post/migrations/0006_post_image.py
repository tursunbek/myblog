# Generated by Django 3.1 on 2020-08-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/%Y/%m/%d/'),
        ),
    ]
