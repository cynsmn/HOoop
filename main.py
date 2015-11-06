# mini script que se ejecuta poniendo:
# $ipython -i main.py

from atm_machine import Account
cuenta1=Account(123,'cynthia') #empieza con balance cero
cuenta2=Account(555,'pepe',100)

# 1) probamos la funcion deposito
cuenta1.deposit(20)
#print cuenta1.balance

# 2) probamos la extraccion
cuenta2.withdraw(200)
#print cuenta2.balance
cuenta2.withdraw(50)
#print cuenta2.balance

# 3) probamos el balance -con los () 
cuenta1.check_balance()
cuenta2.check_balance()

# 4) probamos la transferencia de cuenta2 a cuenta1
cuenta2.transfer_money(10,cuenta1)

