# Generated by Django 2.2.3 on 2019-08-09 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_user', '0006_auto_20190809_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='restaurant_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
