# Generated by Django 3.2.4 on 2021-07-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SHORTURL',
            fields=[
                ('hash', models.CharField(default='AMGwXWq', editable=False, max_length=8, primary_key=True, serialize=False)),
                ('url_path', models.URLField(max_length=120)),
                ('orignalurl', models.CharField(max_length=600)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expires', models.DateTimeField()),
            ],
        ),
    ]
