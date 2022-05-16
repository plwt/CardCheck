from datetime import datetime, date

def card_number():
    card_no=input("Enter your payment card number: ")
    def digits_of(card_no):
        return [int(d) for d in str(card_no)]
    digits = digits_of(card_no)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    if checksum % 10 == 0:
        print("Card number is valid")
    else:
        print("Card number is invalid")
    
card_number()


def card_date():
    
    now = datetime.now()
    now = date(year=now.year, month=now.month, day=1)

    card_expiry = input("Enter your payment card expiry date (MM/YY): ")
    expiry = datetime.strptime(card_expiry, "%m/%y")
    expiry = date(year=expiry.year, month=expiry.month, day=1)

    if now == expiry:
        print("Card is about to expire.")
    elif now > expiry:
        print("Card has expired.")
    elif now < expiry:
        print("Card has not expired.")
    
card_date()
