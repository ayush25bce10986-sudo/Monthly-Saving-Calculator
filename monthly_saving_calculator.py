print("MONTHLY SAVINGS CALCULATOR")

monthly_income = float(input("Enter your monthly income: "))

print("\nEnter your monthly expenses:")
rent = float(input("Rent:"))
food = float(input("Groceries:"))
transportation = float(input("Transportation:"))
house_bills= float(input("Bills:"))
other = float(input("Other expenses:"))

total_expenses = rent + food + transportation + house_bills + other

monthly_savings = monthly_income - total_expenses


print("SAVINGS")
print(f"Monthly Income:{monthly_income:,.2f}")
print(f"Total Expenses:{total_expenses:,.2f}")
print(f"Monthly Savings:{monthly_savings:,.2f}")
print(f"Savings Rate:{(monthly_savings/monthly_income)*100:.1f}%")
print()

if monthly_savings > 0:
    print("Great job!")
    
    print("SAVINGS GOAL CALCULATOR")
    
    goal_name = input("\nWhat are you saving for? (e.g., vacation, car, emergency fund): ")
    goal_price = float(input(f"How much do you need for your {goal_name}? $"))
    
    months_needed = goal_price / monthly_savings
    years = int(months_needed // 12)
    remaining_months = int(months_needed % 12)
    
    print(f"\nGoal:{goal_name}")
    print(f"Target Amount:{goal_price:,.2f}")
    print(f"Monthly Savings:{monthly_savings:,.2f}")
    print(f"Time to reach goal:{int(months_needed)} months")
    
    if years > 0:
        print(f"({years} year(s) and {remaining_months} month(s))")
    
    print(f"\nKeep saving {monthly_savings:,.2f} every month to reach your goal!")
    
elif monthly_savings == 0:
    print("You're breaking even. Try to reduce expenses to start saving!")
else:
    print("Warning: You're spending more than you earn!")
    print(f"You need to reduce expenses by {abs(monthly_savings):,.2f} to break even.")

print("Thank you for using!")
