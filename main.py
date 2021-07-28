amount_order_items = 0
order_items_count = 0

GST = 0.1
surcharge = 0.05
order_price = 0

item_1 = 0
item_2 = 0
item_3 = 0
item_4 = 0

plural_1 = 0
plural_2 = 0
plural_3 = 0
plural_4 = 0

total_line_price = 0
total_price_ex_GST = 0

takeaway_dine_in = 0
mode_of_operation = input("Select a mode of operation: ").upper()

if mode_of_operation == "NEW ORDER":
    while takeaway_dine_in != 1:
        method_of_order = input("Dine in or Takeaway: ").upper()
        if method_of_order == "TAKEAWAY":
            GST += surcharge
            takeaway_dine_in = 1
        elif method_of_order == "DINE IN":
            GST = GST
            takeaway_dine_in = 1
        else:
            print("ERROR. INVALID INPUT")

    print("Items on the menu today are; Cappuccino($3.00), Espresso($2.25), Latte($2.50) and Iced Coffee($2.50)")
    amount_order_items = int(input("How many items are you ordering? "))
    while order_items_count < amount_order_items:
        order_item = input("Menu Choice: ").upper()
        if order_item == "CAPPUCCINO":
            order_price += 3.00
            order_items_count += 1
            item_1 += 1
        elif order_item == "ESPRESSO":
            order_price += 2.25
            order_items_count += 1
            item_2 += 1
        elif order_item == "LATTE":
            order_price += 2.50
            order_items_count += 1
            item_3 += 1
        elif order_item == "ICED COFFEE":
            order_price += 2.50
            order_items_count += 1
            item_4 += 1
        else:
            print("We don't serve that on our menu")

elif mode_of_operation == "DAILY SUMMARY":
    print("")

else:
    print("ERROR. Invalid Input")


if item_1 != 1:
    plural_1 = "s"
else:
    plural_1 = ""
if item_2 != 1:
    plural_2 = "s"
else:
    plural_2 = ""
if item_3 != 1:
    plural_3 = "s"
else:
    plural_3 = ""
if item_4 != 1:
    plural_4 = "s"
else:
    plural_4 = ""


item_1_GST = 3.00 * GST * item_1
item_2_GST = 2.25 * GST * item_2
item_3_GST = 2.50 * GST * item_3
item_4_GST = 2.50 * GST * item_4

item_1_cost = item_1 * 3.00
item_2_cost = item_2 * 2.25
item_3_cost = item_3 * 2.50
item_4_cost = item_4 * 2.50

total_price_ex_GST = item_1_cost + item_2_cost + item_3_cost + item_4_cost
GST = item_1_GST + item_2_GST + item_3_GST + item_4_GST
total_line_price = GST + total_price_ex_GST


print(f"You ordered {amount_order_items} items")
print(f"Which consists of {item_1} Cappuccino{plural_1}, {item_2} Espresso{plural_2}, {item_3} Latte{plural_3} and "
      f"{item_4} Iced Coffee{plural_4}")

print(f"Your individual items cost excluding GST are ${item_1_cost} for the {item_1} Cappuccino{plural_1}, "
      f"${item_2_cost} for the {item_2} Espresso{plural_2}, ${item_3_cost} for the {item_3} Latte{plural_3}, "
      f"${item_4_cost} for the {item_4} Iced Coffee{plural_4}")
print(f"Total price excluding GST is ${total_price_ex_GST}")
print(f"GST price is ${GST}")
print(f"The Total Line Item cost is ${total_line_price}")

