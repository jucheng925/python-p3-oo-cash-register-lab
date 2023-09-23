#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0, items=None, last_item=None):
    self.discount = discount 
    self.total = total
    self.last_item = last_item
    if items is None:
      items = []
      self.items = items

  def add_item(self, title, price, quantity=1):
    self.total += quantity * price
    self.items += ([title] * quantity)
    self.last_item = [title, price, quantity]


  def apply_discount(self):
    if self.discount > 0:
      self.total = self.total * (1 - (self.discount/100))
      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total -= self.last_item[1] * self.last_item[2]