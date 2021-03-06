# Generated by Django 3.1.12 on 2021-07-08 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emoji', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emojiterra',
            name='emoji',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='emojiterra',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='emojiterra',
            name='unicode_categories',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='emojiterra',
            name='unicode_codepoints',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='emojiterra',
            name='unicode_codes',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='emojiterra',
            name='unicode_keywords',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='emojiterra',
            name='unicode_shortname',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='emojiterra',
            name='unicode_version',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='emojiterra',
            name='url',
            field=models.CharField(max_length=1000),
        ),
    ]
