# Generated by Django 5.0 on 2023-12-26 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag_about_rename_home_author_comment_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
    ]
