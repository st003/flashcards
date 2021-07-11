# Generated by Django 3.1.13 on 2021-07-11 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_auto_20210711_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='category',
            field=models.IntegerField(blank=True, choices=[(1, 'Noun'), (2, 'Verb'), (3, 'Adjective'), (4, 'Adverb'), (5, 'Phrase'), (6, 'Counter')], db_index=True, null=True),
        ),
    ]
