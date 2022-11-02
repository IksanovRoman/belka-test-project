# Generated by Django 4.1.3 on 2022-11-02 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concentrate', '0006_remove_month_name_month_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='month',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FRESHMAN', max_length=2),
        ),
    ]