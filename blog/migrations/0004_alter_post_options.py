# Generated by Django 4.0.1 on 2022-02-04 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish_date', '-id')},
        ),
    ]