# Generated by Django 3.1.7 on 2021-05-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel_1', '0013_blog_blog_descriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cat_priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
