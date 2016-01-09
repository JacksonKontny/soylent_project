# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('soylent_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSrc',
            fields=[
                ('datasrc_id', models.CharField(max_length=6, serialize=False, primary_key=True, db_column=b'dataSrc_ID')),
                ('authors', models.CharField(max_length=255, null=True, blank=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('year', models.CharField(max_length=4, null=True, blank=True)),
                ('journal', models.CharField(max_length=135, null=True, blank=True)),
                ('vol_city', models.CharField(max_length=16, null=True, db_column=b'vol_City', blank=True)),
                ('issue_state', models.CharField(max_length=5, null=True, db_column=b'issue_State', blank=True)),
                ('start_page', models.CharField(max_length=5, null=True, db_column=b'start_Page', blank=True)),
                ('end_page', models.CharField(max_length=5, null=True, db_column=b'end_Page', blank=True)),
            ],
            options={
                'db_table': 'data_src',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DerivCd',
            fields=[
                ('deriv_cd', models.CharField(max_length=4, serialize=False, primary_key=True, db_column=b'deriv_Cd')),
                ('deriv_desc', models.CharField(max_length=120, db_column=b'deriv_Desc')),
            ],
            options={
                'db_table': 'deriv_cd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FdGroup',
            fields=[
                ('fdgrp_cd', models.CharField(max_length=4, serialize=False, primary_key=True, db_column=b'fdGrp_Cd')),
                ('fdgrp_desc', models.CharField(max_length=60, db_column=b'fdGrp_Desc')),
            ],
            options={
                'db_table': 'fd_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FoodDes',
            fields=[
                ('ndb_no', models.CharField(max_length=5, serialize=False, primary_key=True, db_column=b'nDB_No')),
                ('long_desc', models.CharField(max_length=200, db_column=b'long_Desc')),
                ('shrt_desc', models.CharField(max_length=60, db_column=b'shrt_Desc')),
                ('comname', models.CharField(max_length=100, null=True, db_column=b'comName', blank=True)),
                ('manufacname', models.CharField(max_length=65, null=True, db_column=b'manufacName', blank=True)),
                ('survey', models.NullBooleanField()),
                ('ref_desc', models.CharField(max_length=135, null=True, blank=True)),
                ('refuse', models.IntegerField(null=True, blank=True)),
                ('sciname', models.CharField(max_length=65, null=True, db_column=b'sciName', blank=True)),
                ('n_factor', models.DecimalField(null=True, decimal_places=2, max_digits=4, db_column=b'n_Factor', blank=True)),
                ('pro_factor', models.DecimalField(null=True, decimal_places=2, max_digits=4, db_column=b'pro_Factor', blank=True)),
                ('fat_factor', models.DecimalField(null=True, decimal_places=2, max_digits=4, db_column=b'fat_Factor', blank=True)),
                ('cho_factor', models.DecimalField(null=True, decimal_places=2, max_digits=4, db_column=b'cHO_Factor', blank=True)),
            ],
            options={
                'db_table': 'food_des',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FoodPrice',
            fields=[
                ('price_id', models.AutoField(serialize=False, primary_key=True)),
                ('cents', models.IntegerField(null=True, blank=True)),
                ('unit_name', models.CharField(max_length=10, null=True, blank=True)),
                ('units', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'food_price',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Footnote',
            fields=[
                ('footnote_id', models.AutoField(serialize=False, primary_key=True)),
                ('footnt_no', models.CharField(max_length=4, db_column=b'footnt_No')),
                ('footnt_typ', models.CharField(max_length=1, db_column=b'footnt_Typ')),
                ('nutr_no', models.CharField(max_length=3, null=True, db_column=b'nutr_No', blank=True)),
                ('footnt_txt', models.CharField(max_length=200, db_column=b'footnt_Txt')),
            ],
            options={
                'db_table': 'footnote',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Langual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'langual',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LanguaLFactorsDescription',
            fields=[
                ('factor_code', models.CharField(max_length=5, serialize=False, primary_key=True, db_column=b'factor_Code')),
                ('description', models.CharField(max_length=140)),
            ],
            options={
                'db_table': 'langdesc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NutData',
            fields=[
                ('nutr_id', models.AutoField(serialize=False, primary_key=True, db_column=b'nutr_ID')),
                ('nutr_val', models.DecimalField(decimal_places=3, max_digits=10, db_column=b'nutr_Val')),
                ('num_data_pts', models.DecimalField(decimal_places=0, max_digits=5, db_column=b'num_Data_Pts')),
                ('std_error', models.DecimalField(null=True, decimal_places=3, max_digits=8, db_column=b'std_Error', blank=True)),
                ('ref_ndb_no', models.CharField(max_length=5, null=True, db_column=b'ref_NDB_No', blank=True)),
                ('add_nutr_mark', models.NullBooleanField(db_column=b'add_Nutr_Mark')),
                ('num_studies', models.IntegerField(null=True, db_column=b'num_Studies', blank=True)),
                ('minval', models.DecimalField(null=True, decimal_places=3, max_digits=10, db_column=b'minVal', blank=True)),
                ('maxval', models.DecimalField(null=True, decimal_places=3, max_digits=10, db_column=b'maxVal', blank=True)),
                ('df', models.IntegerField(null=True, db_column=b'dF', blank=True)),
                ('low_eb', models.DecimalField(null=True, decimal_places=3, max_digits=10, db_column=b'low_EB', blank=True)),
                ('up_eb', models.DecimalField(null=True, decimal_places=3, max_digits=10, db_column=b'up_EB', blank=True)),
                ('stat_cmt', models.CharField(max_length=10, null=True, blank=True)),
                ('addmod_date', models.CharField(max_length=10, null=True, db_column=b'addMod_Date', blank=True)),
                ('cc', models.CharField(max_length=1, null=True, db_column=b'cC', blank=True)),
            ],
            options={
                'db_table': 'nut_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NutrDef',
            fields=[
                ('nutr_no', models.CharField(max_length=3, serialize=False, primary_key=True, db_column=b'nutr_No')),
                ('units', models.CharField(max_length=7)),
                ('tagname', models.CharField(max_length=20, null=True, blank=True)),
                ('nutrdesc', models.CharField(max_length=60, db_column=b'nutrDesc')),
                ('num_dec', models.CharField(max_length=1, db_column=b'num_Dec')),
                ('sr_order', models.IntegerField(db_column=b'sR_Order')),
            ],
            options={
                'db_table': 'nutr_def',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SrcCd',
            fields=[
                ('src_cd', models.CharField(max_length=2, serialize=False, primary_key=True, db_column=b'src_Cd')),
                ('srccd_desc', models.CharField(max_length=60, db_column=b'srcCd_Desc')),
            ],
            options={
                'db_table': 'src_cd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('weight_id', models.AutoField(serialize=False, primary_key=True, db_column=b'weight_ID')),
                ('seq', models.CharField(max_length=2, null=True, blank=True)),
                ('amount', models.DecimalField(max_digits=5, decimal_places=3)),
                ('msre_desc', models.CharField(max_length=84, db_column=b'msre_Desc')),
                ('gm_wgt', models.DecimalField(decimal_places=1, max_digits=7, db_column=b'gm_Wgt')),
                ('num_data_pts', models.IntegerField(null=True, db_column=b'num_Data_Pts', blank=True)),
                ('std_dev', models.DecimalField(null=True, decimal_places=3, max_digits=7, db_column=b'std_Dev', blank=True)),
            ],
            options={
                'db_table': 'weight',
                'managed': False,
            },
        ),
    ]
