import requests
from cieloApi3 import *
import json
'''
url = 'https://apisandbox.cieloecommerce.cielo.com.br/1/sales'

data = {
   "MerchantOrderId":"2014111703",
   "Customer":{
      "Name":"Comprador crédito simples"
   },
   "Payment":{
     "Type":"CreditCard",
     "Amount":15700,
     "Installments":1,
     "SoftDescriptor":"123456789ABCD",
     "CreditCard":{
         "CardNumber":"1234123412341231",
         "Holder":"Teste Holder",
         "ExpirationDate":"12/2030",
         "SecurityCode":"123",
         "Brand":"Visa"
     }
   }
}

response = requests.post(url, data=data)

print(response)
'''

environment = Environment(sandbox=True)

merchant = Merchant('e491b4d2-607d-4850-973a-595c47fd20c7', 'WJJJHFTLBDTHBKWLEQBUYQQSUOLXEVMERSDJLXVM')

sale = Sale('123')

sale.customer = Customer('Jessica')

credit_card = CreditCard('123', 'Visa')
credit_card.expiration_date = '12/2018'
credit_card.card_number = '0000000000000001'
credit_card.holder = 'Jessica'

sale.payment = Payment(15700)
sale.payment.credit_card = credit_card

cielo_ecommerce = CieloEcommerce(merchant, environment)


response_create_sale = cielo_ecommerce.create_sale(sale)
print('----------------------response_create_sale----------------------')
print(json.dumps(response_create_sale, indent=2))
print('----------------------response_create_sale----------------------')

# Com a venda criada na Cielo, já temos o ID do pagamento, TID e demais
# dados retornados pela Cielo
payment_id = sale.payment.payment_id

# Com o ID do pagamento, podemos fazer sua captura,
# se ela não tiver sido capturada ainda
response_capture_sale = cielo_ecommerce.capture_sale(payment_id, 15700, 0)
print('----------------------response_capture_sale----------------------')
print(json.dumps(response_capture_sale, indent=2))
print('----------------------response_capture_sale----------------------')

# E também podemos fazer seu cancelamento, se for o caso
response_cancel_sale = cielo_ecommerce.cancel_sale(payment_id, 15700)
print('---------------------response_cancel_sale---------------------')
print(json.dumps(response_cancel_sale, indent=2))
print('---------------------response_cancel_sale---------------------')

