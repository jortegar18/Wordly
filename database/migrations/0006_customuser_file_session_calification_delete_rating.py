# Generated by Django 4.1.7 on 2023-06-04 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_remove_customuser_calification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/', verbose_name='File'),
        ),
        migrations.AddField(
            model_name='session',
            name='calification',
            field=models.CharField(default=11, max_length=5),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]