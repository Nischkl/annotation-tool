# Generated by Django 2.0.5 on 2018-06-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotpreferred', '0002_task_desc_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='desc_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='task_images'),
        ),
    ]
