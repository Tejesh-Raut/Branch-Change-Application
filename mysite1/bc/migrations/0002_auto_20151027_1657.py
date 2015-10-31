# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import bc.models


class Migration(migrations.Migration):

    dependencies = [
        ('bc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rollno',
            name='choice_10',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice10', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_11',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice11', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_12',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice12', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_13',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice13', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_14',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice14', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_15',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice15', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_16',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice16', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_17',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice17', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_5',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice5', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_6',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice6', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_7',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice7', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_8',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice8', max_length=50, default=''),
        ),
        migrations.AddField(
            model_name='rollno',
            name='choice_9',
            field=models.CharField(choices=[('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM B.Tech', 'MM B.Tech'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('ME B.Tech', 'ME B.Tech'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('EP B.Tech', 'EP B.Tech'), ('EN Dual Deg', 'EN Dual Deg'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE B.Tech', 'EE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('CL Dual Deg', 'CL Dual Deg'), ('CL B.Tech', 'CL B.Tech'), ('CH', 'CH'), ('CE B.Tech', 'CE B.Tech'), ('AE B.Tech', 'AE B.Tech')], verbose_name='Choice9', max_length=50, default=''),
        ),
        migrations.AlterField(
            model_name='rollno',
            name='cpi',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='CPI', validators=[bc.models.validate_rollno]),
        ),
        migrations.AlterField(
            model_name='rollno',
            name='rollno_text',
            field=models.IntegerField(validators=[bc.models.validate_rollno]),
        ),
    ]
