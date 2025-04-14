from db_manager import ShardedDatabase


if __name__== "__main__":
    db = ShardedDatabase()

    # Simulating Hot shard
    print("\nInserting into HOT SHARD")
    for uid in range(1000, 1100):
        if uid % 4 == 0:
            db.insert_user(uid, {"name": f"HotUser{uid}"})
    
    # Normal shard distribution
    print("\nInserting normally distyributed users")
    for uid in range(200, 210):
        db.insert_user(uid, {"name": f"User{uid}"})

    db.print_shard_load()
    db.print_shards()