# Generated by Django 3.0.5 on 2020-05-22 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_post_course_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='', max_length=1200),
        ),
    ]