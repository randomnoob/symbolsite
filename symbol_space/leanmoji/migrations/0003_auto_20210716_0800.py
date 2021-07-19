# Generated by Django 3.1.12 on 2021-07-16 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emoji', '0012_emojiwiki_intro_html'),
        ('codetoemoji', '0002_codepoints_emoji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codepoints',
            name='emoji',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='emoji.emojiterra'),
        ),
    ]
