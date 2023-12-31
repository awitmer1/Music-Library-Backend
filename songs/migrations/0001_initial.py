# Generated by Django 4.2.2 on 2023-06-16 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('album', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
    ]
