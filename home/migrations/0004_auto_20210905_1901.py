# Generated by Django 3.0.4 on 2021-09-05 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='first_slide',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='second_slide',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='third_slide',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(upload_to='blogs'),
        ),
    ]
