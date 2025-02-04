from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    def add(self, item):
        self.item = item
        self.inventory.append(item)

        return item
    
    def remove(self, item):
        self.item = item
        
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        
    def get_by_id(self,id):
        
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self,other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        self.inventory.append(their_item)

        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]
        
        
        self.swap_items(other_vendor, my_item, their_item)

        return True
    
    def get_by_category(self, category):
      
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)
        return category_list

    def get_best_by_category(self, category):
        max_category = []
        
        if category not in self.inventory:
            return None
        
        
        for item in self.inventory:
            if item.get_category() == category:
                max_category.append(item)
            return max(max_category)
    
    
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if their_priority not in self.inventory and my_priority not in other_vendor.inventory:
            return False

        my_item = my_priority
        their_item = their_priority
        self.swap_items(other_vendor, my_item, their_item)

        return True