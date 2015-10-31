# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RollNo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('rollno_text', models.CharField(max_length=9)),
                ('name_text', models.CharField(max_length=200)),
                ('current_branch', models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], max_length=50)),
                ('cpi', models.DecimalField(max_digits=4, decimal_places=2, verbose_name='CPI')),
                ('category', models.CharField(choices=[('1', 'General'), ('2', 'OBC'), ('3', 'SC'), ('4', 'ST'), ('5', 'General-PD'), ('6', 'OBC-PD'), ('7', 'SC-PD'), ('8', 'ST-PD')], max_length=50, verbose_name='CATEGORY')),
                ('choice_1', models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], max_length=50, verbose_name='Choice1')),
                ('choice_2', models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], max_length=50, verbose_name='Choice2')),
                ('choice_3', models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], max_length=50, verbose_name='Choice3')),
                ('choice_4', models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], max_length=50, verbose_name='Choice4')),
            ],
        ),
    ]
