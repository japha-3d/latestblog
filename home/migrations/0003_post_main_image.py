# Generated by Django 3.0.4 on 2021-09-05 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_time_to_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='main_image',
            field=models.ImageField(default=1, upload_to='media/blogs'),
            preserve_default=False,
        ),
    ]