# Generated by Django 3.2.9 on 2021-11-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_slider_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('', 'Not active')], max_length=100),
        ),
    ]
