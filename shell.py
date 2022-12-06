from bank.models import Client, Account, Credit
from random import randint


client_1 = Client.objects.create(name='Бердиев Н.Д.', birth_year='1994-01-04', citizenship='гражданин КР', work_place='Codify')
client_2 = Client.objects.create(name='Актилек', birth_year='2005-12-22', citizenship='Кыргызстан', work_place='Ramada')

account_1 = client_1.accounts.create(number=randint(1000000000000000, 9999999999999999), account_type=3)
account_2 = client_1.accounts.create(number=randint(1000000000000000, 9999999999999999), account_type=2)
account_3 = client_2.accounts.create(number=randint(1000000000000000, 9999999999999999), account_type=8)
account_4 = client_2.accounts.create(number=randint(1000000000000000, 9999999999999999))

credit_1 = account_1.credits.create(sum=25000)
credit_2 = account_2.credits.create(sum=19000)
credit_3 = account_3.credits.create(sum=550000)
credit_4 = account_4.credits.create(sum=36000)
