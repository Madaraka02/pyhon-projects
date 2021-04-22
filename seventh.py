def computepay(h , r):
    grosspay = h * r

    if(h <= 40):
        pay = (h * r)
    elif(h > 40):
        pay = (40 * r + (h-40) * 1.5 * r)

    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter the Rate:")
r = float(rate)
pay = computepay(h , r)
print("pay" computepay(h , r))
