class RandomizedSet(object):

    def __init__(self):
        self.val_list = []
        self.val_dict = {}        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_dict:
            
            return False
            
        else:
            self.val_list.append(val)
            self.val_dict[val] =  len(self.val_list) -1
            return True

        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_dict:
            return False
        else:
            idx = self.val_dict[val]
            last_val = self.val_list[-1]

            self.val_list[idx] = last_val
            self.val_dict[last_val] = idx

            self.val_list.pop()
            del self.val_dict[val]

            return True
        

        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.val_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()