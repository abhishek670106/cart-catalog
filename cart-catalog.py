# Catalog
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Constants
PACKAGE_CAPACITY = 10
PACKAGE_SHIPPING_FEE = 5
GIFT_WRAP_FEE = 1

# Initialize variables
cart_total = 0
total_quantity = 0
applicable_discounts = []
discounted_product_quantity = 0

# Get quantity and gift wrapping information for each product
products = []
for product_name, product_price in catalog.items():
    quantity = int(input(f"Enter the quantity of {product_name}: "))
    is_gift_wrapped = input(f"Is {product_name} wrapped as a gift? (yes/no): ").lower() == "yes"

    products.append((product_name, quantity, is_gift_wrapped))
    cart_total += quantity * product_price
    total_quantity += quantity

# Apply discounts
if cart_total > 200:
    discount_name = "flat_10_discount"
    discount_amount = 10
    applicable_discounts.append((discount_name, discount_amount))

if total_quantity > 20:
    discount_name = "bulk_10_discount"
    discount_amount = 0.1 * cart_total
    applicable_discounts.append((discount_name, discount_amount))

if total_quantity > 30:
    for product_name, quantity, is_gift_wrapped in products:
        if quantity > 15:
            discounted_product_quantity += quantity - 15
            discount_name = "tiered_50_discount"
            discount_amount = 0.5 * discounted_product_quantity * catalog[product_name]
            applicable_discounts.append((discount_name, discount_amount))
            break

if any(quantity > 10 for _, quantity, _ in products):
    for product_name, quantity, is_gift_wrapped in products:
        if quantity > 10:
            discounted_product_quantity = quantity
            discount_name = "bulk_5_discount"
            discount_amount = 0.05 * quantity * catalog[product_name]
            applicable_discounts.append((discount_name, discount_amount))
            break

# Select the most beneficial discount
max_discount_amount = 0
selected_discount = None
for discount_name, discount_amount in applicable_discounts:
    if discount_amount > max_discount_amount:
        max_discount_amount = discount_amount
        selected_discount = (discount_name, discount_amount)

# Calculate total
subtotal = cart_total
if selected_discount:
    discount_name, discount_amount = selected_discount
    subtotal -= discount_amount

total = subtotal + (PACKAGE_SHIPPING_FEE * (total_quantity // PACKAGE_CAPACITY))
if total_quantity % PACKAGE_CAPACITY != 0:
    total += PACKAGE_SHIPPING_FEE

gift_wrap_fee = 0
for _, quantity, is_gift_wrapped in products:
    if is_gift_wrapped:
        gift_wrap_fee += GIFT_WRAP_FEE * quantity

# Output details
print("Product Details:")
for product_name, quantity, _ in products:
    product_total = quantity * catalog[product_name]
    print(f"{product_name}: Quantity: {quantity}, Total: ${product_total}")
print("\nSummary:")
print(f"Subtotal: ${subtotal}")

# Display applicable discounts
if applicable_discounts:
    print("\nAvailable Discounts:")
    for discount_name, discount_amount in applicable_discounts:
        print(f"  -  {discount_name}: Amount: ${discount_amount}")

if selected_discount:
    discount_name, discount_amount = selected_discount
    print("\nDiscount Applied:")
    print(f" - {discount_name}: Amount: ${discount_amount}")
    print("Maximum discount applied!")

print(f"Shipping fee: ${PACKAGE_SHIPPING_FEE * (total_quantity // PACKAGE_CAPACITY)}")
print(f"Gift wrap fee: ${gift_wrap_fee}")
print(f"Total: ${total}")
