# Generated by Django 2.2.5 on 2019-09-27 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_auto_20190928_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='logtable',
            name='opt',
            field=models.IntegerField(default=12, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='logtable',
            name='email',
            field=models.TextField(max_length=20),
        ),
    ]
