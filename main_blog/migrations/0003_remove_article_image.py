# Generated by Django 4.1.4 on 2023-02-15 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0002_article_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
    ]
