# ==================================================
# 🌟 Exercise 1 : Student Grade Summary
# ==================================================
#
# Instructions:
# You are given a dictionary where:
# - Keys = student names
# - Values = list of grades for each student
#
# Your task is to:
# 1. Calculate the average grade for each student.
# 2. Assign a letter grade based on the average.
# 3. Calculate the class average.
# 4. Print a summary report.
#
# --------------------------------------------------
# Initial Data:
#
student_grades = {
     "Alice": [88, 92, 100],
     "Bob": [75, 78, 80],
     "Charlie": [92, 90, 85],
     "Dana": [83, 88, 92],
     "Eli": [78, 80, 72]
 }
#
# --------------------------------------------------
# Requirements:
#
# 1️⃣ Create a new dictionary called student_averages:
#    - Loop through student_grades
#    - For each student:
#        * Calculate the average using sum() and len()
#        * Store the result in student_averages
student_averages = {name:sum(value)/len(value) for name,value in student_grades.items() }
#
# 2️⃣ Create a dictionary called student_letter_grades:
#    - Assign letter grades using this scale:
#        A : 90 and above
#        B : 80 to 89
#        C : 70 to 79
#        D : 60 to 69
#        F : Below 60
student_letter_grades = {}
for key,value in student_averages.items():
    if value < 60:
        student_letter_grades[key] = 'F'
    if 60 <= value <= 69:
        student_letter_grades[key] = 'D'
    if 70 <= value <= 79:
        student_letter_grades[key] = 'C'
    if 80 <= value <= 89:
        student_letter_grades[key] = 'B'
    if value >= 90 :
        student_letter_grades[key] = 'A'

# 3️⃣ Calculate the class average:
#    - Average of all student averages
average_class = sum(student_averages.values())/len(student_averages)
#
# 4️⃣ Print:
#    - Student name
#    - Average grade
#    - Letter grade

for key,value in student_averages.items():
     print(f"{key} - Average: {value:.2f} - Grade: {student_letter_grades[key]}")
#
# --------------------------------------------------
# Hints:
# - Use loops to iterate through dictionaries
# - Initialize empty dictionaries before filling them
# - Use sum() and len() to compute averages
#
# ==================================================
# 🌟 Exercise 2 : Advanced Data Manipulation and Analysis
# ==================================================
#
# You are given a list of dictionaries representing sales transactions.
#
# Each dictionary contains:
# - customer_id
# - product
# - price
# - quantity
# - date
#
# --------------------------------------------------
sales_data = [
     {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
     {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
     {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
     {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
     {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
     {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
     {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]
# 
# --------------------------------------------------
# Tasks:
#
# 1️⃣ Total Sales Calculation:
#    - Calculate total revenue per product.
#    - Use a loop.
#    - Store results in a dictionary.
revenue_per_product_dic = {}
for dic in sales_data:
    if dic["product"] in revenue_per_product_dic.keys():
        revenue_per_product_dic[dic["product"]] += dic['price']*dic['quantity']
    else:
        revenue_per_product_dic["product"] = dic['price']*dic['quantity']

# 2️⃣ Customer Spending Profile:
#    - Calculate total amount spent by each customer.
#    - Use a dictionary to accumulate totals.
accumulate_totals_dic = {}
for dic in sales_data:
    if dic["customer_id"] in accumulate_totals_dic.keys():
        accumulate_totals_dic[dic["customer_id"]] += dic['price']*dic['quantity']
    else:
        accumulate_totals_dic[dic["customer_id"]] = dic['price']*dic['quantity']
#
# 3️⃣ Sales Data Enhancement:
#    - Add a new field "total_price" to each transaction:
#        total_price = price * quantity
#    - Modify the original sales_data list.
for dic in sales_data:
    dic['total_price'] = dic['price'] * dic['quantity']

# 4️⃣ High-Value Transactions:
#    - Use list comprehension.
#    - Select transactions where total_price > 500.
#    - Sort descending by total_price.
high_value_transactions = sorted(
    [dic for dic in sales_data if dic['total_price'] > 500],
    key=lambda x: x['total_price'],
    reverse=True
)

# 5️⃣ Customer Loyalty Identification:
#    - Count purchases per customer.
#    - Identify customers with more than one purchase.
actual_customer = 1
lst = []
while True:
    count = 0
    for dic in sales_data:
        if dic["customer_id"] == actual_customer:
            count+=1
    if count > 1:
        lst.append(actual_customer)
    actual_customer+=1
    if int(actual_customer)>len(sales_data):
        break
    print(lst)

    
# --------------------------------------------------
# Bonus: Insights and Analysis
#
# - Calculate average transaction value per product.
# - Identify the most popular product (based on quantity sold).
# - Provide insights about:
#     * Customer behavior
#     * Revenue trends
#     * Marketing strategies
#
# ==================================================
# End of Exercises
# ==================================================