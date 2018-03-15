DezhouKV使用了MurmurHash3算法，将KEY映射到值域，当存储使用率超过3.378%后算法1退化，使用KEY_PUT_WHERE+Bloom Filter进行KEY查询，即先使用KEY_PUT_WHERE计算。
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
假设值域为n，布隆过滤器大小为m，哈希个数k公式![公式名](http://latex.codecogs.com/png.latex?k=ln2*({m/n})),则误报率R公式![公式名](http://latex.codecogs.com/png.latex?R=2^{-k}),可以算出，m/n为10时，k=6.9，R=0.8%。
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
    
    function keysCount（key，k）
    	num_buckets = 2 ^ k
    	max_zeroes = [0] * num_buckets
    	h = hash(key)
    	bucket_id = h & (num_buckets -1)
    	bucket_hash = h >> k
     	max_zeroes[bucket_id] = max(maxzeroes[bucket_id], trailing_zeroes(bucket_hash))
     	return 2 ^ (float(sum(max_zeroes)) / num_buckets) * num_buckets * 0.79402
    end function
___
