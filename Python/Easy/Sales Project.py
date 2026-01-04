sales = [
    {"product": "Apple", "qty": 10, "price": 20},
    {"product": "Banana", "qty": 5, "price": 10},
    {"product": "Orange", "qty": 8, "price": 15},
    {"product": "Grapes", "qty": 3, "price": 50},
    {"product": "Mango", "qty": 6, "price": 40},
    {"product": "Watermelon", "qty": 2, "price": 60},
    {"product": "Pineapple", "qty": 4, "price": 30},
    {"product": "Papaya", "qty": 7, "price": 25},
    {"product": "Kiwi", "qty": 12, "price": 35},
    {"product": "Strawberry", "qty": 15, "price": 45}
]

'''
🔥 1. Calculate total sales (qty × price) for each product.
🔥 2. Print the total revenue generated from all products combined.
🔥 3. Find the product with the highest total sales amount.
🔥 4. Find the product with the lowest total sales amount.
🔥 5. Find which product has the highest quantity sold.
🔥 6. Find which product has the lowest quantity sold.
🔥 7. Add a new key "total_sale" in each dictionary (qty × price).
🔥 8. Count how many products have price greater than 30.
🔥 9. Create a list of all products that have qty > 5.
🔥 10. Calculate the average price of all products.
🔥 11. Calculate the average quantity of all products.
🔥 12. Create a function that returns the total revenue.
🔥 13. Create a function that takes a product name and returns its sales details.

Example:
Input: "Mango" → return qty, price, total sales.

🔥 14. Create a list of products sorted by price (ascending).
🔥 15. Create a list of products sorted by total sales (descending).
'''

for sale in sales:
    sale['Total Sale'] = sale['qty'] * sale['price']
    print(f'{sale['product']} = {sale["Total Sale"]}')