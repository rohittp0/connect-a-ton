# Generated by Django 4.2.7 on 2023-11-04 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_useranswer_is_correct_alter_userconfig_college_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='skipped',
            field=models.BooleanField(default=False),
        ),
    ]
