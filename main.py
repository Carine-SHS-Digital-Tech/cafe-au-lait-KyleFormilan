import csv

f = open('daily_summary.csv', 'r+')

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
change = 0
takeaway_dine_in = 0
count_tendered = 0
count_2 = 0
mode_of_order_count = 0
mode_of_operation = 0
daily_summary_continue = 0
new_order_count = 0
order_ID = 1
header = ["ORDER_ID", "TYPE", "Cappuccino", "EXGST_1", "Esspresso", "EXGST_2", "Latte",
                                  "EXGST_3", "Iced Coffee", "EXGST_4", "ORDER_CUPS", "ORDER_CHARGES",
                                  "ORDER_PRICE_EXC_GST", "ORDER_TOTAL"]

with open('daily_summary.csv', 'w', encoding='UTF8') as daily_summary:
    writer = csv.writer(daily_summary)
    writer.writerow(header)


while mode_of_order_count == 0:
    while new_order_count == 0:
        daily_summary_continue = 0
        print("\n**************** WELCOME TO CAFE AU LAIT ******************\n\n")

        mode_of_operation = input("Type 'New order' or 'Daily summary' for your choice of operation: ").upper()

        if mode_of_operation == "NEW ORDER":
            while takeaway_dine_in != 1:
                method_of_order = input("\nDine in or Takeaway: ").upper()
                if method_of_order == "TAKEAWAY":
                    GST += surcharge
                    takeaway_dine_in = 1
                elif method_of_order == "DINE IN":
                    GST = GST
                    takeaway_dine_in = 1
                else:
                    print("ERROR. INVALID INPUT")

            print("\nItems on the menu today are; Cappuccino($3.00), Espresso($2.25), Latte($2.50) and Iced Coffee($2.50)")
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
            ### ADD IN WYA TO VIEW DAILY SUMMARY
            print("You may view the Daily Summary in the daily_summary.csv file above.")
            daily_summary_continue = 1

        else:
            print("ERROR. Invalid Input")

        while daily_summary_continue != 1:
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

            print("\n\nYour receipt of your order is as follows,\n")
            print(f"You ordered {amount_order_items} items")
            print(f"Which consists of {item_1} Cappuccino{plural_1}, {item_2} Espresso{plural_2}, {item_3} Latte{plural_3} and "
                  f"{item_4} Iced Coffee{plural_4}")

            print(f"Your individual items cost excluding GST are ${item_1_cost} for the {item_1} Cappuccino{plural_1}, "
                  f"${item_2_cost} for the {item_2} Espresso{plural_2}, ${item_3_cost} for the {item_3} Latte{plural_3}, "
                  f"${item_4_cost} for the {item_4} Iced Coffee{plural_4}")
            print(f"Total price excluding Extra Charges is ${total_price_ex_GST:.2f}")
            print(f"Extra Charges cost is ${GST:.2f}")
            print(f"The Total Line Item cost is ${total_line_price:.2f}")

            count_tendered = 0
            total_line_price_new = total_line_price
            while count_tendered == 0:
                amount_tendered = float(input("\nEnter Amount Required: $"))
                if amount_tendered < total_line_price_new:
                    difference = total_line_price_new - amount_tendered
                    print(f"You owe ${difference.__round__(2)}")
                    total_line_price_new = total_line_price_new - amount_tendered
                elif amount_tendered == total_line_price_new:
                    print("Correct amount tendered\nHere are your coffees")
                    count_tendered = 1
                elif amount_tendered > total_line_price_new:
                    change = amount_tendered - total_line_price_new
                    print(f"Your change is ${change.__round__(2)}")
                    count_tendered = 1
                else:
                    print("ERROR")
            daily_summary_continue = 0
            count_2 = 0


            header = ["ORDER_ID", "TYPE", "Cappuccino", "EXGST_1", "Esspresso", "EXGST_2", "Latte",
                        "EXGST_3", "Iced Coffee", "EXGST_4", "ORDER_CUPS", "ORDER_CHARGES",
                        "ORDER_PRICE_EXC_GST", "ORDER_TOTAL"]
            row = [order_ID, mode_of_operation, item_1, item_1_cost, item_2, item_2_cost, item_3,
                    item_3_cost, item_4, item_4_cost, amount_order_items, GST.__round__(2), total_price_ex_GST.__round__(2),
                    total_line_price.__round__(2)]
            order_ID += 1
            with open('daily_summary.csv', 'a', encoding='UTF8') as daily_summary:
                writer = csv.writer(daily_summary)

                writer.writerow(row)

            while count_2 == 0:
                continue_order = input("Is it the end of the business day? ").upper()
                if continue_order == "YES":
                    mode_of_order_count = 1
                    new_order_count = 1
                    print("Business day has ended, Daily summary will be reset.")
                    count_2 = 1

                    view_summary = input("Do you wish to view daily summary? ").upper()
                    if view_summary == "YES":
                        ### ADD IN WYA TO VIEW DAILY SUMMARY
                        print("You may view Daily Summary above")
                        daily_summary_continue = 1
                        f.truncate(0)
                        f.close()
                    else:
                        f.truncate(0)
                        f.close()
                        daily_summary_continue = 1


                elif continue_order == "NO":
                    print("The business day is still on.")
                    count_2 = 1
                    daily_summary_continue = 1
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
                    count_tendered = 0
                    mode_of_order_count = 0
                    change = 0
                    amount_tendered = 0
                    difference = 0
                else:
                    print("Invalid Input. Try again.")
