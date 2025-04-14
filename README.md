# 🔄 Sharded Database Simulation in Python

A simple, modular Python simulation of a sharded database system. Supports:

- Query routing via hash-based partitioning
- Insert/get operations across multiple shards
- Hot shard simulation (uneven load)
- Monitoring per-shard traffic
- Mock rebalancing recommendations

---

## 📦 Project Structure

├── README.md # you are here!
├── __init__.py
├── db_manager.py
├── main.py # run the simulation
├── router.py
└── shard.py

Concepts Covered
Sharding
Partitioning strategies
Load balancing
Hotspot detection
Query routing