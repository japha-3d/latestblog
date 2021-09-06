# Generated by Django 3.0.4 on 2021-09-05 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210905_1950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='paragraph_1',
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph1',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph2',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph3',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph4',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph_2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph_3',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='paragraph_4',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]