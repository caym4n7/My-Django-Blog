# Generated by Django 3.1 on 2021-04-07 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210405_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish')], default='draft', max_length=10),
        ),
    ]
