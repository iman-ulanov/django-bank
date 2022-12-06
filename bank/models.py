from django.db import models
from datetime import date


class Client(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='ФИО')
    citizenship = models.CharField(max_length=20, null=False, blank=False, verbose_name='Гражданство')
    birth_year = models.DateField(null=False, blank=False, verbose_name='Год рождения')
    work_place = models.CharField(max_length=30, null=False, blank=False, verbose_name='Место работы')
    update_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


    def __str__(self):
        return f'{self.name}, Год рождения-{self.birth_year.year}'



class Account(models.Model):
    number = models.CharField(max_length=16, null=False, blank=False, unique=True, verbose_name='Номер аккаунта')
    account_type = models.IntegerField(default=1, null=False, verbose_name='тип аккаунта')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='accounts')


    class Meta:
        db_table = 'accounts'
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    def __str__(self):
        return f'Клиент {self.client.name}, аккаунт-{self.number}'



class Credit(models.Model):
    sum = models.IntegerField(null=False, blank=False, verbose_name='Сумма кредита')
    date = models.DateField(auto_now_add=True, verbose_name='Дата получения')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credits')


    class Meta:
        db_table = 'loans'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'


    def __str__(self):
        return f'{self.account.client.name}'

