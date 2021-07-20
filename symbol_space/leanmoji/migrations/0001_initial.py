# Generated by Django 3.1.12 on 2021-07-20 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kaomoji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, null=True)),
                ('kaomoji', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('keywords', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]