DezhouKV uses the MurmurHash3 algorithm to map the KEY to the range. When the storage usage exceeds 3.378%, the algorithm 1 degenerates. KEY_PUT_WHERE Bloom Filter is used for the KEY query, that is, KEY_PUT_WHERE calculation is used first.
___
#####Algorithm 1 U_Calculator
___
    function KEY_PUT_WHERE（KEY）
    	u=0
    	sum=MurmurHash3（KEY）    
    	determinant=sum%(1.5*10^10)-10^10
    	if determinant < 0 then
    		u=1
    	end if
    	if determinant > 0 and determinant < 10^9 then
    		u=2
    	end if
    	if determinant > 10^9 and determinant < 5*10^9 then
    		u=3
    	end if
    	return u
    end function
___
Suppose the size of the Bloom Filter is m, the range is n, the number of hashes is k, and false alarm rate is R, we can figure out that m/n is 10, k=6.9, R=0.8%.
![公式名](http://latex.codecogs.com/png.latex?k=ln2*({m/n}))
![公式名](http://latex.codecogs.com/png.latex?R=2^{-k})
___
#####Algorithm 2 BloomFilter_Get_K
___
    function SelectBloomK（m_n）
	    k=0.69*m_n
    	
    	if k < 1 then
    		k=1
    	end if
    	if k > 30 then
    		k=30
    	end if
    	return k
    end function
___
___
#####Algorithm 3 BloomFilter_Add
___
    function BloomAdd（KEY，bloom）
    	hashValue = BloomHash（KEY）
    	m = k * n
    	delta=hashValue >> 17 | hashValue << 15
    	for i in k do
    		pos = hashValue % m
    		bloom[pos/8] |= (1 << (pos % 8))
    		hashValue += delta
    	end for
    end function
___
___
#####Algorithm 4 BloomFilter_Get
___
    function BloomGet（KEY，bloom）
    	hashValue = BloomHash（KEY）
    	m = k * n
    	delta=hashValue >> 17 | hashValue << 15
    	for i in k do
    		pos = hashValue % m
    		if ((array[pos/8] & (1 << (pos % 8))) == 0) then
    			return false
    		end if
    		hashValue += delta
    	end for
    	return true
    end function
___
___
#####Algorithm 5 HyperLogLog_Count
___
    function trailing_zeroes（hashnum）
    	if hashnum == 0 then
    		return 32
    	end if
    	p = 0
    	while (hashnum) >> p & 1 == 0 then
    		p += 1
    	end while
    	return p
    end function
    
    function keysCount（KEY，k）
    	num_buckets = 2 ^ k
    	max_zeroes = [0] * num_buckets
    	h = hash(KEY)
    	bucket_id = h & (num_buckets -1)
    	bucket_hash = h >> k
     	max_zeroes[bucket_id] = max(maxzeroes[bucket_id], trailing_zeroes(bucket_hash))
     	return 2 ^ (float(sum(max_zeroes)) / num_buckets) * num_buckets * 0.79402
    end function
___
