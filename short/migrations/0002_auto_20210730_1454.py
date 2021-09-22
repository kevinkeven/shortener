# Generated by Django 3.2.4 on 2021-07-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('short', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='hash',
            field=models.CharField(default='tjP0X9o', editable=False, max_length=8, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='url_path',
            field=models.URLField(blank=True, max_length=120),
        ),
    ]
