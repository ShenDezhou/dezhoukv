We take GET in API as an example to describe the process in DezhouKV in detail.

MurmurHash3_128 maps KEY to the function space and obtain u, according to the u-calculation-formula,
searches for the existence of this KEY in the storage at all levels based on the Bloom Filter, and returns if it does not exist, 

The Bloom Filter displays the existence of calculates the Maglev node value according to the KEY, and determines the node's survival state if the node goes off, sends an internal instruction GET to the node, and the different versions are compatible and send the returned data to the customer, if step 3 returns to failure, then the utilization rate of DezhouKV cluster is counted according to HyperLogLog algorithm. For example, a certain level of the cache miss is needed.

Two salvage: repeat step 3.1,3.2, if the two salvage failed, the judgment can continue to degrade and return to three salvage: repeat step 3.1,3.2 and return to result.
