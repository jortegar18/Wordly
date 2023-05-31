# Generated by Django 4.1.7 on 2023-05-31 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_remove_time_av_tutor_time_av_user_tutor_calification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='calification',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='cost',
        ),
        migrations.AddField(
            model_name='customuser',
            name='calification',
            field=models.CharField(default=11, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='cost',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
