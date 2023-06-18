#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    
    self.total = 0

    self.last_transaction = 0

    self.items = []

  def add_item(self, title, price, quantity = 1):
    self.title = title
    self.price = price
    self.quantity = quantity
    self.last_transaction = price*quantity
    self.total += self.last_transaction
    for _ in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if self.discount > 0:
      discount_percentage = float(self.discount)/100
      self.total = int(self.total * (1 - discount_percentage))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
    
  def void_last_transaction(self):
    self.total = self.total - self.last_transaction