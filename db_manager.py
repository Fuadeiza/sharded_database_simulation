from shard import Shard
from router import QueryRouter

class ShardedDatabase:
    def __init__(self, num_shards=4):
        self.shards = [Shard(i) for i in range(num_shards)]
        self.router = QueryRouter(self.shards)

    def insert_user(self, user_id, user_data):
        shard = self.router.route(user_id)
        shard.insert(user_id, user_data)

    def get_user(self, user_id):
        shard = self.router.route(user_id)
        user_data = shard.get(user_id)
        if user_data:
            print(f"[GET] User {user_id} found in Shard {shard.shard_id} : {user_data}")
        else:
            print(f"[GET] User {user_id} not found in Shard {shard.shard_id}")
        return user_data
    
    def print_shards(self):
        print("\n--- SHARD STATE ---")
        for shard in self.shards:
            print(shard)
        print("-------------\n")
    
    def print_shard_load(self):
        print("\n--- SHARD LOAD ---")
        for shard in self.shards:
            print(f"Shard {shard.shard_id} handled {shard.request_count} requests.")
        print("------------------\n")



        