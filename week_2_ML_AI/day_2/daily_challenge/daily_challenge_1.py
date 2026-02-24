# ==================================================
# Daily Challenge : Pagination
# ==================================================
#
# What You’ll Learn:
# - Classes and Objects
# - Constructors (__init__)
# - List slicing
# - Method chaining (return self)
# - Error handling
# - Type conversion
#
# --------------------------------------------------
# Step 1 : Create the Pagination class
# --------------------------------------------------
#
# Create a class called Pagination.
# This class will simulate a simple pagination system.
#
# It should optionally accept:
# - items (a list)
# - page_size (default = 10)
import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        
        if items is None:
            items = []

        self.items = items

        # convert to int
        self.page_size = int(page_size)

        self.current_idx = 0

        # calculate total pages
        self.total_pages = math.ceil(len(self.items) / self.page_size)
        
# --------------------------------------------------
# Step 2 : Implement the __init__ method
# --------------------------------------------------
#
# The constructor should:
#
# - Accept two optional parameters:
#       items (default = None)
#       page_size (default = 10)
#
# - If items is None:
#       initialize it as an empty list.
#
# - Store items inside the instance.
#
# - Store page_size inside the instance.
#       Make sure it is converted to int.
#
# - Create an attribute current_idx:
#       This represents the current page index.
#       Internally pages should start at 0.
#
# - Calculate the total number of pages.
#       Use math.ceil to round up.
#
#
# --------------------------------------------------
# Step 3 : Implement get_visible_items()
# --------------------------------------------------
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]
        
# This method should:
#
# - Return the list of items visible on the current page.
#
# - Use slicing.
#
# - Calculate:
#       start index
#       end index
#
#       start = current_idx * page_size
#       end = start + page_size
#
#
# --------------------------------------------------
# Step 4 : Implement Navigation Methods
# --------------------------------------------------
#

# ---------------------
# - page_num is 1-based (user input).
# - If page_num is out of range:
#       raise ValueError.
# - Otherwise:
#       update current_idx (remember internal index is 0-based).
#
#
    
# ------------
# - Set current_idx to the first page.
#

   
# -----------
# - Set current_idx to the last page.
#
#
# next_page()
# -----------
# - Move forward one page.
# - Do nothing if already on the last page.
#
#
# previous_page()
# ---------------
# - Move backward one page.
# - Do nothing if already on the first page.
#
#
# IMPORTANT:
# All navigation methods (except get_visible_items)
# should return self.
# This allows method chaining.
#
    def go_to_page(self, page_num):
        # page_num is 1-based
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError("Page number out of range")
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self
# --------------------------------------------------
# Bonus : Implement __str__()
# --------------------------------------------------
#
# This method should:
#
# - Return a string representation of the current page.
# - Each item should appear on a new line.
# - Use "\n".join(...)
#
#
# --------------------------------------------------
# Testing
# --------------------------------------------------
#
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
#
# Test:
print(p.get_visible_items())
print(p.next_page())
print(p.last_page())
#p.go_to_page(10)  # should raise ValueError
#p.go_to_page(0)   # should raise ValueError
#
#
# Bonus chaining test:
p.first_page()
print(p.next_page().next_page().next_page().get_visible_items())
#
# Expected output: ['m', 'n', 'o', 'p']
#
# ==================================================