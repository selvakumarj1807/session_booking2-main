# Generated by Django 3.0.5 on 2024-04-15 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_auto_20240414_1420'),
        ('user_panel', '0003_auto_20240415_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('booked_at', models.DateTimeField(auto_now_add=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.Session')),
            ],
            options={
                'db_table': 'booking',
            },
        ),
        migrations.DeleteModel(
            name='Session_book',
        ),
    ]
