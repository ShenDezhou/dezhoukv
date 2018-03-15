Today, Every enterprise has terabytes or even petabytes of data, and how to store these structured data tests the ability of architects. Traditional distributed KV databases, such as Redis, Memcached, MongoDB, Elasticsearch, focus only on scalability, high availability, and high performance. However, it is not suitable for universality. We analyzed several KV databases, Redis, LevelDB, RocksDB, SogouQDB, and found that the main performance constraint of these databases is additional synchronous communication logic to increase scalability. Based on our observation, we propose DezhouKV, a kind of KV database cluster with universality, extensibility, high performance and high availability. It also supports HDD/SSD hybrid deployment to solve the problem of universality without consuming computing performance. DezhouKV using
1) high-speed short hash algorithm to calculate the mapping
2) using Bloom Filter algorithm to reduce access to HDD/SSDs
3) using Maglev algorithm for load balancing of nodes 
4) Using multi-tier data storage files to sort the global KEY storage
5) use three layers of partitions to support heterogeneous server deployment to support complex production environments. 
The performance of KV database is better than that of other KV database clusters mentioned in this paper, and the performance of KV database is improved.
