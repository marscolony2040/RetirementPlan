import numpy as np
import pandas as pd

def pv(amount, rate, maturity):
    return (amount / rate) * (1 - pow(1 + rate, -maturity))

def pmt(amount, rate, maturity):
    return (amount * rate) / (pow(1 + rate, maturity) - 1)

def table(withdrawl=100000, save=5, withdraw=4, rate=0.03):
    present_value = pv(withdrawl, rate, withdraw)
    present_payment = pmt(present_value, rate, save)
    balance = 0
    ipmt = 0
    payment = 0
    hold = []
    hold.append([balance, ipmt, payment])
    for i in range(save):
        payment = present_payment
        ipmt = balance * rate
        balance = balance + ipmt + payment
        hold.append([balance, ipmt, payment])
    for i in range(withdraw):
        payment = withdrawl
        ipmt = balance * rate
        balance = balance + ipmt - payment
        hold.append([balance, ipmt, payment])
    return pd.DataFrame(data=hold, columns=['Balance','Interest','Pmt/Wth'])

print(table(withdrawl=500, save=10, withdraw=5, rate=0.09))
