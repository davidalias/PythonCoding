Hash Function Rules:
- It must be DETERMINISTIC (same input always has the same output)
- FIXED LENGTH output (for all possible inputs)
- IRREVERSIBLE output (cannot reverse engineer the output to find the input)

Hash collision happens when two or more inputs (keys) in a hash function result in the same output (hash).
- A good hash function tries to minimize collisions
- A perfect hash function has no collisions
- Lot of hash collisions? Still a hash function but not a good one

Known hash functions -> MD5, SHA-256, BCrypt, Argon2
