# Generated by Django 4.0.1 on 2022-01-31 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0009_alter_post_eventid_alter_post_groupid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='eventid',
            field=models.CharField(default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='groupid',
            field=models.CharField(default='', max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.CharField(default='', max_length=512, null=True),
        ),
    ]
