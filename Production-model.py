
# function to calculate via zero-level strategy
def calc_stock_quantity(stock_level: int, months: int, sales_qty: dict) -> None:
    prod_qties = []
    curr_stock_lvl = stock_level
    for j in range(1, months + 1):
        if sales_qty[f"month_{j}"] <= curr_stock_lvl:
            prod_qties.append(0)
            curr_stock_lvl -= sales_qty[f"month_{j}"]
            # print(sales_qty[f"month_{j}"], curr_stock_lvl, 0)
        else:
            to_prod = sales_qty[f"month_{j}"] - curr_stock_lvl
            prod_qties.append(to_prod)
            curr_stock_lvl += to_prod
            curr_stock_lvl -= sales_qty[f"month_{j}"]
            # print(sales_qty[f"month_{j}"], curr_stock_lvl, to_prod)

    for x in range(len(prod_qties)):
        print(f"Production quantity month {x + 1} - {prod_qties[x]}")


 # Ask user for inputs
initial_stk_lvl = int(input("Please enter an initial stock level :"))
number_of_months_to_plan = int(input("Please enter number of months to plan :"))
planned_month_sales_qty = {}
for i in range(1, number_of_months_to_plan + 1):
    sales_quantity = int(input(f"Please enter the planned sales quantity for month {i} : "))
    planned_month_sales_qty[f"month_{i}"] = sales_quantity

# Process user input
calc_stock_quantity(initial_stk_lvl, number_of_months_to_plan, planned_month_sales_qty)