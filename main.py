import csv
import os

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
viewing_summary = 0
difference = 0
amount_tendered = 0

frequency_dine_in = 0
frequency_takeaway = 0
frequency_total_orders = 0
frequency_cups_coffee = 0
frequency_income = 0
frequency_GST = 0
method_of_order = 0
mode_of_operation_count = 0

header = ["ORDER_ID", "TYPE", "Cappuccino", "EX_GST_1", "Espresso", "EX_GST_2", "Latte",
          "EX_GST_3", "Iced Coffee", "EX_GST_4", "ORDER_CUPS", "ORDER_CHARGES",
          "ORDER_PRICE_EXC_GST", "ORDER_TOTAL"]

# Opens and writes to daily_summary csv file, sets the header each time the code is reset
with open('daily_summary.csv', 'w', encoding='UTF8') as daily_summary:
    writer = csv.writer(daily_summary)
    writer.writerow(header)

# While loop for looping through code whilst the business day is still on
while mode_of_order_count == 0:
    while new_order_count == 0:
        daily_summary_continue = 0
        print("\n**************** WELCOME TO CAFE AU LAIT ******************\n\n")
        while mode_of_operation_count == 0:
            mode_of_operation = input("Type 'New order' or 'Daily summary' for your choice of operation: ").upper()

            # Checks whether user wants a new order or to view the daily summary
            if mode_of_operation == "NEW ORDER":
                mode_of_operation_count = 1
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

                # Gives user the option to choose their order
                print("\nItems on the menu today are; Cappuccino($3.00), Espresso($2.25), Latte($2.50) and "
                      "Iced Coffee($2.50)")
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

            # Opens up the daily summary in excel if user wishes to view daily summary
            elif mode_of_operation == "DAILY SUMMARY":
                mode_of_operation_count = 1
                os.system("start EXCEL.EXE daily_summary.csv")
                print("You may view the Daily Summary in the daily_summary.csv file above.")
                daily_summary_continue = 1

            else:
                print("ERROR. Invalid Input")

        # Sets the output to either plural or singular
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

            # Sets and calculates all the costs
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

            # Prints out the required information to the user
            print("\n\nYour receipt of your order is as follows,\n")
            print(f"You ordered {amount_order_items} items")
            print(f"Which consists of {item_1} Cappuccino{plural_1}, {item_2} Espresso{plural_2}, {item_3} "
                  f"Latte{plural_3} and {item_4} Iced Coffee{plural_4}")

            print(f"Your individual items cost excluding GST are ${item_1_cost} for the {item_1} Cappuccino{plural_1}, "
                  f"${item_2_cost} for the {item_2} Espresso{plural_2}, ${item_3_cost} for the {item_3} "
                  f"Latte{plural_3}, ${item_4_cost} for the {item_4} Iced Coffee{plural_4}")
            print(f"Total price excluding Extra Charges is ${total_price_ex_GST:.2f}")
            print(f"Extra Charges cost is ${GST:.2f}")
            print(f"The Total Line Item cost is ${total_line_price.__round__(2):.2f}")

            # Works out the amount required to be paid and ensures that the user gets the appropriate change
            count_tendered = 0
            total_line_price_new = total_line_price.__round__(2)
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

            # Updates csv file with every new order entered
            header = ["ORDER_ID", "TYPE", "Cappuccino", "EX_GST_1", "Espresso", "EX_GST_2", "Latte",
                      "EX_GST_3", "Iced Coffee", "EX_GST_4", "ORDER_CUPS", "ORDER_CHARGES",
                      "ORDER_PRICE_EXC_GST", "ORDER_TOTAL"]
            row = [order_ID, method_of_order, item_1, item_1_cost.__round__(2), item_2, item_2_cost.__round__(2),
                   item_3, item_3_cost.__round__(2), item_4, item_4_cost.__round__(2), amount_order_items,
                   GST.__round__(2), total_price_ex_GST.__round__(2), total_line_price.__round__(2)]
            order_ID += 1
            with open('daily_summary.csv', 'a', encoding='UTF8') as daily_summary:
                writer = csv.writer(daily_summary)

                writer.writerow(row)
            if method_of_order == "DINE IN":
                frequency_dine_in += 1
            else:
                frequency_takeaway += 1
            frequency_total_orders = frequency_total_orders + frequency_takeaway + frequency_dine_in
            frequency_cups_coffee = frequency_cups_coffee + item_1 + item_2 + item_3 + item_4
            frequency_GST = frequency_GST + GST
            frequency_income = frequency_income + total_line_price

            info_heading = ["ORDERS_COUNT", "DINE-IN", "TAKE-AWAY", "CUPS_COUNT", "GST_COLLECTED", "DAILY_INCOME"]
            info_body = [order_ID - 1, frequency_dine_in, frequency_takeaway, frequency_cups_coffee,
                         frequency_GST.__round__(2), frequency_income.__round__(2)]

            # Checks whether it is the end of the business day or not and if it is the end of the business day it displays the daily summary
            while count_2 == 0:
                continue_order = input("Is it the end of the business day? ").upper()
                if continue_order == "YES":
                    mode_of_order_count = 1
                    new_order_count = 1
                    print("Business day has ended, Daily summary will be reset.")

                    with open('daily_summary.csv', 'a', encoding='UTF8') as daily_summary:
                        writer = csv.writer(daily_summary)

                        writer.writerow(info_heading)
                        writer.writerow(info_body)

                    count_2 = 1

                    # Opens updated csv file in excel
                    os.system("start EXCEL.EXE daily_summary.csv")
                    while viewing_summary == 0:
                        view_summary = input("Are you finished viewing daily summary? ").upper()
                        if view_summary == "YES":
                            # Resets csv file
                            daily_summary_continue = 1
                            f.truncate(0)
                            f.close()
                            viewing_summary = 1
                        else:
                            daily_summary_continue = 1
                # Resets all the variables for the user to input a new order
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
                    mode_of_operation_count = 0
                else:
                    print("Invalid Input. Try again.")
