# Generated by Django 3.0.4 on 2021-09-05 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210905_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fourth_image',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='third_image',
            field=models.ImageField(blank=True, null=True, upload_to='blogs'),
        ),
    ]
