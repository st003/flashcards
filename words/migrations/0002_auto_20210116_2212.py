# Generated by Django 3.1.4 on 2021-01-16 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='category',
            field=models.IntegerField(blank=True, choices=[(1, 'Noun'), (2, 'Verb'), (3, 'Adjective'), (4, 'Adverb'), (5, 'Phrase')], null=True),
        ),
    ]
