class QueryRouter:
    def __init__(self, shards, strategy="hash_mod"):
        self.shards = shards
        self.strategy = strategy
        
    def route(self, key):
        if self.strategy == "hash_mod":
            shard_index = key % len(self.shards)
            return self.shards[shard_index]
        else:
            raise NotImplementedError(f"Strategy {self.strategy} not implemented")
        