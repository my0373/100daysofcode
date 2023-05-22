from decimal import Decimal
def loginBanner():
    print(f"Welcome to the tip calculator.")
def getTotalBill(bill):
    bill["total"] = Decimal(input("What was the total bill ? : "))

def getGuests(bill):
    bill["guests"] = int(input("How many people to split the bill ? :"))

def getTip(bill):
    bill['tip_percent'] = int(input("What percentage tip would you like to give ? 10, 12 or 15 ?"))
    bill['tip_amount'] = Decimal((bill["total"] / 100) * bill["tip_percent"])

def calculateBill(bill):
    bill["amount_to_pay"] = Decimal(bill["total"] + bill['tip_amount'])
    bill["amount_per_person"] = round(bill["amount_to_pay"] / bill["guests"], 2)
    bill["over_amount"] = (bill["amount_per_person"] * bill["guests"]) - bill["amount_to_pay"]

    if bill["over_amount"]:
        print(f"Unfortunately, {bill['amount_to_pay']} doesn't divide exactly by {bill['guests']}.")


def main():
    bill = {}
    loginBanner()
    getTotalBill(bill)
    getGuests(bill)
    getTip(bill)
    calculateBill(bill)


    print(bill)

if __name__ == '__main__':
    main()