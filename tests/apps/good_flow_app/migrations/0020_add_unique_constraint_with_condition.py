# Generated by Django 3.1 on 2019-09-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0019_drop_unique_constraint'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='testtable',
            constraint=models.UniqueConstraint(
                condition=models.Q(test_field_int__isnull=False),
                fields=('test_field_int',),
                name='test_uniq_constraint',
            ),
        ),
    ]