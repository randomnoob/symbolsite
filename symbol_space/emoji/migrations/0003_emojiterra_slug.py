# Generated by Django 3.1.12 on 2021-07-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emoji', '0002_auto_20210708_0752'),
    ]

    operations = [
        migrations.AddField(
            model_name='emojiterra',
            name='slug',
            field=models.CharField(default=None, max_length=1000),
            preserve_default=False,
        ),
    ]