# Generated by Django 2.2.2 on 2019-06-15 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='artile_id',
            new_name='article_id',
        ),
    ]
