# Generated by Django 5.0 on 2023-12-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_claimquerymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='claimquerymodel',
            name='service_Garage_Output',
            field=models.CharField(default='Pending', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='claimquerymodel',
            name='service_ML_Output',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='claimquerymodel',
            name='service_username',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
