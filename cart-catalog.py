# Catalog list of products and their prices are given below:
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Constants for discounts and fees
PACKAGE_CAPACITY = 10
PACKAGE_SHIPPING_FEE = 5
GIFT_WRAP_FEE = 1

# Initialize variables for discounts
cart_total = 0
total_quantity = 0
applicable_discounts = []
discounted_product_quantity = 0

# Get quantity and gift wrapping information  for each product from the user
products = []
for product_name, product_price in catalog.items():
    quantity = int(input(f"Enter the quantity of {product_name}: "))
    is_gift_wrapped = input(f"Is {product_name} wrapped as a gift? (yes/no): ").lower() == "yes"

    products.append((product_name, quantity, is_gift_wrapped)) # Add the product to the list of products
    cart_total += quantity * product_price
    total_quantity += quantity

# Apply discounts based on the rules
if cart_total > 200:
    discount_name = "flat_10_discount"
    discount_amount = 10
    applicable_discounts.append((discount_name, discount_amount)) # Add the discount to the list of applicable discounts

if total_quantity > 20:
    discount_name = "bulk_10_discount"
    discount_amount = 0.1 * cart_total
    applicable_discounts.append((discount_name, discount_amount)) # Add the discount to the list of applicable discounts

if total_quantity > 30:
    for product_name, quantity, is_gift_wrapped in products:
        if quantity > 15:
            discounted_product_quantity += quantity - 15
            discount_name = "tiered_50_discount"
            discount_amount = 0.5 * discounted_product_quantity * catalog[product_name] # Calculate the discount amount
            applicable_discounts.append((discount_name, discount_amount)) # Add the discount to the list of applicable discounts
            break
# Apply bulk discount for each product if the quantity is greater than 10
if any(quantity > 10 for _, quantity, _ in products):
    for product_name, quantity, is_gift_wrapped in products:
        if quantity > 10:
            discounted_product_quantity = quantity
            discount_name = "bulk_5_discount"
            discount_amount = 0.05 * quantity * catalog[product_name] # Calculate the discount amount
            applicable_discounts.append((discount_name, discount_amount)) # Add the discount to the list of applicable discounts
            break

# Select the most beneficial discount for the customer
max_discount_amount = 0
selected_discount = None
for discount_name, discount_amount in applicable_discounts: # Iterate through the list of applicable discounts
    if discount_amount > max_discount_amount:
        max_discount_amount = discount_amount
        selected_discount = (discount_name, discount_amount) # Select the discount with the highest discount amount

# Calculate total price of the order
subtotal = cart_total
if selected_discount: # If a discount is selected apply it to the subtotal
    discount_name, discount_amount = selected_discount
    subtotal -= discount_amount

# Calculate shipping fee
total = subtotal + (PACKAGE_SHIPPING_FEE * (total_quantity // PACKAGE_CAPACITY))
if total_quantity % PACKAGE_CAPACITY != 0:
    total += PACKAGE_SHIPPING_FEE
# Calculate gift wrapping fee
gift_wrap_fee = 0
for _, quantity, is_gift_wrapped in products:
    if is_gift_wrapped:
        gift_wrap_fee += GIFT_WRAP_FEE * quantity # Calculate the gift wrap fee for each product

# Output details of the order
print("Product Details:")
for product_name, quantity, _ in products:
    product_total = quantity * catalog[product_name] # Calculate the total price of the product
    print(f"{product_name}: Quantity: {quantity}, Total: ${product_total}")
print("\nSummary:")
print(f"Subtotal: ${subtotal}")

# Display applicable discounts and the selected discount
if applicable_discounts:
    print("\nAvailable Discounts:")
    for discount_name, discount_amount in applicable_discounts:
        print(f"  -  {discount_name}: Amount: ${discount_amount}")

# Display the selected discount
if selected_discount:
    discount_name, discount_amount = selected_discount
    print("\nDiscount Applied:")
    print(f" - {discount_name}: Amount: ${discount_amount}")
    print("Maximum discount applied!")

print(f"Shipping fee: ${PACKAGE_SHIPPING_FEE * (total_quantity // PACKAGE_CAPACITY)}")
print(f"Gift wrap fee: ${gift_wrap_fee}")
print(f"Total: ${total-discount_amount}")
