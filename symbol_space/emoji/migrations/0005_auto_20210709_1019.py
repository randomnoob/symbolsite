# Generated by Django 3.1.12 on 2021-07-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emoji', '0004_auto_20210709_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emojiterra',
            name='unicode_codes',
            field=models.TextField(),
        ),
    ]