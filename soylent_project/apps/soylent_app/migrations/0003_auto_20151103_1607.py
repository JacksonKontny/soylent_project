# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soylent_app', '0002_datasrc_derivcd_fdgroup_fooddes_foodprice_footnote_langual_langualfactorsdescription_nutdata_nutrdef'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='nDB_No',
        ),
        migrations.RemoveField(
            model_name='limitrequirement',
            name='nutr_No',
        ),
        migrations.RemoveField(
            model_name='ratiorequirement',
            name='denominator',
        ),
        migrations.RemoveField(
            model_name='ratiorequirement',
            name='numerator',
        ),
        migrations.RemoveField(
            model_name='ratiorequirement',
            name='nutr_No1',
        ),
        migrations.RemoveField(
            model_name='ratiorequirement',
            name='nutr_No2',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='ndb_no',
            field=models.ForeignKey(db_column=b'nDB_No', blank=True, to='soylent_app.FoodDes', null=True),
        ),
        migrations.AddField(
            model_name='limitrequirement',
            name='nutr',
            field=models.ForeignKey(db_column=b'nutr_ID', blank=True, to='soylent_app.NutData', null=True),
        ),
        migrations.AddField(
            model_name='ratiorequirement',
            name='nutrients',
            field=models.ManyToManyField(to='soylent_app.NutData', null=True, db_column=b'nutr_ID', blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='maximum',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='minimum',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
