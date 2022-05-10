from datetime import date


#Works
def getnumber():
    card_number=input("What is your card number?")
        
    return card_number

#Works
def luhn_checksum():
    card_no=getnumber()
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
    
luhn_checksum()


def getcarddate():
    
    date_entry = input('Enter the expiry date of the  in DD-MM-YYYY format: ')
    year, month, day = map(int, date_entry.split('-'))
    carddate = datetime.date(day, month, year)
    return getcarddate

def check_date():
    
        carddate=getcarddate()
        """Checks current date against the credit card's date. If it is valid, returns True; else False."""
        carddate = datetime.datetime.strptime(self.card_date, "%d/%m/%Y").date()
        if datetime.date.today() < carddate:
            print("This card has not expired")
        else:
            print("This card has expired")

check_date()