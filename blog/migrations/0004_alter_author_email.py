# Generated by Django 3.2.8 on 2022-06-21 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_publication_date_post_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
