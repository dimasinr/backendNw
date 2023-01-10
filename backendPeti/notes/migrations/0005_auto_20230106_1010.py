# Generated by Django 3.2.16 on 2023-01-06 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_employeecuti'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noteshrd',
            old_name='end_date',
            new_name='date_note',
        ),
        migrations.RemoveField(
            model_name='noteshrd',
            name='data_cuti',
        ),
        migrations.RemoveField(
            model_name='noteshrd',
            name='jatah_cuti',
        ),
        migrations.RemoveField(
            model_name='noteshrd',
            name='sisa_cuti',
        ),
        migrations.RemoveField(
            model_name='noteshrd',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='noteshrd',
            name='tanggal_cuti',
        ),
        migrations.AddField(
            model_name='noteshrd',
            name='notes',
            field=models.TextField(max_length=120, null=True),
        ),
    ]
