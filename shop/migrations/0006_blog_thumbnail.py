# Generated by Django 4.0.6 on 2022-07-31 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_blog_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
