# Cart-Catalog Python Program


This is a Python program that calculates the total cost and details of a shopping cart based on a catalog of products.

Catalog
The catalog dictionary contains the available products and their corresponding prices:

```
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
    }

```
## Constants
The program uses the following constants:
```
PACKAGE_CAPACITY = 10
PACKAGE_SHIPPING_FEE = 5
GIFT_WRAP_FEE = 1
```
PACKAGE_CAPACITY: Maximum number of products that can fit in a single package.

PACKAGE_SHIPPING_FEE: Shipping fee for each package.

GIFT_WRAP_FEE: Fee for gift wrapping each product.
## Program Flow
1). Initialize variables:

**cart_total:** Total cost of all products in the shopping cart.

**total_quantity:** Total quantity of products in the shopping cart.

**applicable_discounts:** List to store the discounts that apply to the shopping cart.

**discounted_product_quantity:** Quantity of products eligible for tiered discount.


## Example Usage
Here's an example usage of the program:


# Example input and output for demonstration purposes only

```
Enter the quantity of Product A: 11
Is Product A wrapped as a gift? (yes/no): yes
Enter the quantity of Product B: 12
Is Product B wrapped as a gift? (yes/no): no
Enter the quantity of Product C: 9
Is Product C wrapped as a gift? (yes/no): yes
Product Details:
Product A: Quantity: 11, Total: $220
Product B: Quantity: 12, Total: $480
Product C: Quantity: 9, Total: $450

Summary:
Subtotal: $1035.0

Available Discounts:
  -  flat_10_discount: Amount: $10
  -  bulk_10_discount: Amount: $115.0
  -  bulk_5_discount: Amount: $11.0

Discount Applied:
 - bulk_10_discount: Amount: $115.0
Maximum discount applied!
Shipping fee: $15
Gift wrap fee: $20
Total: $940.0

```

This example demonstrates a shopping cart with quantities and gift wrapping information for three products. The program calculates the subtotal, applies the most beneficial discounts, and calculates the total cost, including shipping and gift wrap fees.

