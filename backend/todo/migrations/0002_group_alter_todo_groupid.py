# Generated by Django 4.2 on 2023-05-02 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='groupId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.group'),
        ),
    ]
