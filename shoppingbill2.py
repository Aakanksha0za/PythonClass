# -*- coding: utf-8 -*-
# Product details
product_price = 499           # int
gst = 18.5                    # float
product_name = "Headphones"   # string

print("Product:", product_name)
print("Price:", product_price)
print("GST:", gst)

# Type casting
price_float = float(product_price)
gst_int = int(gst)
total = price_float + gst

print("\nPrice as float:", price_float)
print("GST as int:", gst_int)
print("Total Amount:", total)

