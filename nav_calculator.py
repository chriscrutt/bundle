assets = 0

bitcoin = 27000
ethereum = 737
usdt = 1
xpr = 0.20
litecoin = 131

bitcoin_percent = 60
ethereum_percent = 20
usdt_percent = 10
xpr = 5
litecoin = 5

assets = 100

bitcoin_old = 7139.1382
bitcoin_new = 27919.27

# Total P+I (A):
# Principal (P):
# Compound (n):	Compounding (x/Yr)
# Time (t in years)

# r = n[(A / P) ^ (1 / nt) - 1]

rate = 1 * ((bitcoin_new / bitcoin_old) ** (1 / (1 * 1)) - 1)

print((bitcoin_new - bitcoin_old) / bitcoin_old)

print(rate)

print(bitcoin_old)
print(bitcoin_new)
print(bitcoin_old * rate)
print(bitcoin_old * (rate - 0.02))

print("\nseperator\n")

time_passed = 0.5
expense_ratio = 0.02
interest = 1000000 * time_passed * rate
before_fees = 1000000 + interest
money_made = before_fees * (expense_ratio * time_passed)
after_fees = before_fees - money_made

print("principle is:", 1000000)
print("rate yearly is:", rate)
print("expense ratio yearly is:", expense_ratio)
print("time passed is:", time_passed)
print("interest is:", interest)
print("before fees is:", before_fees)
print("after fees is:", after_fees)
print("we made:", money_made)