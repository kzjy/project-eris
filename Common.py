class Record: 

    def __init__(self):
        self.items = []

    def push(self, item):
        if self.get_queue_length() >= 20:
            self.pop()
        
        self.items.append(item)
        
    def pop(self):
        return self.items.pop(0)

    def get_most_recent_item(self):
        if self.get_queue_length() > 0:
            return self.items[-1]
        return None

    def get_queue_length(self):
        return len(self.items)
    
    def empty(self):
        self.items = []