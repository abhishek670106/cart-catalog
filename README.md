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
Initialize variables:

**cart_total:** Total cost of all products in the shopping cart.
**total_quantity:** Total quantity of products in the shopping cart.
**applicable_discounts:** List to store the discounts that apply to the shopping cart.
**discounted_product_quantity:** Quantity of products eligible for tiered discount.
Get quantity and gift wrapping information for each product:

Iterate over each product in the catalog.
Prompt the user to enter the quantity and whether the product is gift-wrapped.
Calculate the product's cost and update cart_total and total_quantity.
Store the product details in the products list.
Apply discounts:

Check if the cart_total exceeds $200. If true, add a flat 10% discount.
Check if the total_quantity exceeds 20. If true, add a 10% bulk discount based on the cart_total.
Check if the total_quantity exceeds 30. If true, calculate the quantity eligible for the tiered discount.
Iterate over the products in the products list.
If a product's quantity exceeds 15, calculate the discount amount based on 50% of the excess quantity and product price.
Add the tiered discount to applicable_discounts and break from the loop.
Check if any product quantity exceeds 10. If true, calculate a 5% bulk discount for the first product exceeding 10.
Iterate over the products in the products list.
If a product's quantity exceeds 10, calculate the discount amount based on 5% of the product's price multiplied by the exceeding quantity.
Add the bulk discount to applicable_discounts and break from the loop.
Select the most beneficial discount:

Iterate over the applicable_discounts list and find the discount with the highest amount.
Store the selected discount in selected_discount.
Calculate the subtotal:

Set subtotal as the cart_total.
If a selected_discount is available, subtract the discount amount from the subtotal.
Calculate the total cost:

Calculate the shipping fee based on the number of packages required to accommodate all products.
Add the shipping fee to the subtotal.
Calculate the gift wrap fee based on the quantity of gift-wrapped products.
Calculate the total cost by adding the subtotal, shipping fee, and gift wrap fee.
Output details:

Print the details of each product in the shopping cart, including quantity and total cost.
Print the subtotal.
If there are applicable discounts, print the available discounts with their amounts.
If a discount was selected, print the applied discount with its amount.
Print the shipping fee, gift wrap fee, and total cost.
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
Total: $1055.0

```

This example demonstrates a shopping cart with quantities and gift wrapping information for three products. The program calculates the subtotal, applies the most beneficial discounts, and calculates the total cost, including shipping and gift wrap fees.

Please note that the example input and output above are for demonstration purposes only and may not reflect the actual program behavior or expected outputs for different inputs.

Feel free to modify the program or adapt it to suit your specific requirements.
