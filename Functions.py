def student_discount():
    currentprice = int(input("Enter Price:"))
    customer = "student"
    if customer == "student":
        currentprice = currentprice*0.9
        print(currentprice)


def regular_customer():
    price=int(input("Enter today Price:"))
    customers= "Regular"
    if customers == "Regular":
        price = price*0.85
        print(price)

student_discount()
regular_customer()





