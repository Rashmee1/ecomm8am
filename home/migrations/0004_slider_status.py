# Generated by Django 3.2.9 on 2021-11-24 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('', 'Not active')], max_length=100),
        ),
    ]
