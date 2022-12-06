# Generated by Django 3.2 on 2022-12-06 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Аккаунт', 'verbose_name_plural': 'Аккаунты'},
        ),
        migrations.AlterModelOptions(
            name='credit',
            options={'verbose_name': 'Кредит', 'verbose_name_plural': 'Кредиты'},
        ),
        migrations.AlterField(
            model_name='account',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='bank.client'),
        ),
        migrations.AlterField(
            model_name='client',
            name='birth_year',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='bank.account'),
        ),
        migrations.AlterModelTable(
            name='credit',
            table='credits',
        ),
    ]