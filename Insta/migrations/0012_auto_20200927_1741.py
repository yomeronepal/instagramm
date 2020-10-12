# Generated by Django 3.1.1 on 2020-09-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0011_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, upload_to='profile_pics'),
        ),
    ]