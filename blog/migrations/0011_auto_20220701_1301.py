# Generated by Django 3.2.8 on 2022-07-01 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20220701_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100, verbose_name='Subject Name')),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.feedbacksubject'),
        ),
    ]