# Generated by Django 2.2.16 on 2022-03-16 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220317_0035'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='genretitle',
            name='unique_title_genre',
        ),
        migrations.RenameField(
            model_name='genretitle',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='genretitle',
            old_name='title_id',
            new_name='title',
        ),
        migrations.AddConstraint(
            model_name='genretitle',
            constraint=models.UniqueConstraint(fields=('title', 'genre'), name='unique_title_genre'),
        ),
    ]
