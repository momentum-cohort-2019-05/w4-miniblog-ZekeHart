# Generated by Django 2.2.2 on 2019-06-21 17:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='TimeOfPosting'),
            preserve_default=False,
        ),
    ]
