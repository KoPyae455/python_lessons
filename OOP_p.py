from bank_acc import *

KoPyae = BankAccount(1000, "KoPyae")
Aye = BankAccount(2000, "Deepblue")

KoPyae.getBalance()
Aye.getBalance()

Aye.deposit(500)

KoPyae.withdraw(10000)
KoPyae.withdraw(999)

KoPyae.transfer(10000, Aye)
KoPyae.transfer(1, Aye)

Zaw = SavingsAcct(10000, "Zaw")

Zaw.getBalance()

Zaw.deposit(100)

# Zaw.getBalance()
#
# Zaw.withdraw(20000)
# Zaw.transfer(20000, Aye)
# Zaw.transfer(1000, Aye)
# Zaw.withdraw(1000)

# Aye.transfer(1000, KoPyae)
