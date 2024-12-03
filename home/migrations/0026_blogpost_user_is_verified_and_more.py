# Generated by Django 4.2.14 on 2024-12-03 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_merge_20241116_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('page_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, help_text='Designates whether the user has verified their account.', verbose_name='verified'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='feedback_type',
            field=models.CharField(choices=[('general', 'General Inquiry'), ('bug', 'Bug Report'), ('improvement', 'Improvement Suggestion'), ('feature', 'Request for a Feature')], max_length=20),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(choices=[('AppAttack', 'AppAttack'), ('Malware', 'Malware'), ('PT-GUI', 'PT-GUI'), ('Smishing_Detection', 'Smishing Detection'), ('Deakin_CyberSafe_VR', 'Deakin CyberSafe VR'), ('Deakin_Threat_Mirror', 'Deakin Threat Mirror'), ('Company_Website_Development', 'Company Website Development')], max_length=150, verbose_name='project title'),
        ),
    ]
