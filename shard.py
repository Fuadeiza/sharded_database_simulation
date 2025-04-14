class Shard:
    def __init__(self, shard_id):
        self.shard_id = shard_id
        self.data = {}
        self.request_count = 0

    def insert(self, key, value):
        self.data[key] = value
        self.request_count +=1
        print(f"[Shard {self.shard_id} ] Inserted: {key} --> {value}")

    def get(self, key):
        self.request_count +=1
        return self.data.get(key)
    
    def __str__(self):
        return f"Shard {self.shard_id} (requests : {self.request_count}) : {self.data}"