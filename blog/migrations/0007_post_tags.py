# Generated by Django 4.0.1 on 2022-02-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='blog.Tag'),
        ),
    ]
