# Generated by Django 4.1.7 on 2023-06-04 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_customuser_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='calification',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]