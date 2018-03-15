我们使用Redis-Benchmark对各个数据库进行了测试，由于不同的数据库有不同的通讯方式，我们对SogouQDB，和LevelDB进行了接口封装。
![sogouqdb_dezhoukv](/testing/compare_sogouqdb_dezhoukv.png "1000000随机KEY下sogouqdb与dezhoukv性能对比")
![redis_leveldb](/testing/compare_redis_leveldb.png "1000000随机KEY下redis与leveldb性能对比")
dezhoukv下1-6个后端进程下，get的性能对比
![](/testing/compare_get_dezhoukv_1-6_backends.png "DezhouKV1-6后端进程get对比")
dezhoukv下1-6个后端进程下，set的性能对比
![](/testing/compare_set_dezhoukv_1-6_backends.png "DezhouKV1-6后端进程set对比")
图片说明：x轴表示请求的返回比，y轴表明返回比对应的耗时。
对于sogouqdb来说，测试时在HDD介质上进行的，因此性能最低，返回耗时在30-150之间，在四个db中排最后.对于dezhoukv来说，存储介质分布在DRAM+SSD上，取x=90%，观察对应的耗时，Set的耗时大约在37ms，范围在20-60，Get的耗时在39ms，范围在21-54，在所有KV中排第三。对于Redis来说，存储介质在DRAM上，耗时Set大约在2ms左右，范围在2-10之间，Get大约在2ms，在所有KV中是最快的。对于leveldb，存储介质在SSD上，取x=90%，Set返回耗时约4ms，范围在2-12之间，Get返回耗时约5ms，范围在2-40之间，在所有KV中排第二。
从普适性来看，dezhoukv可以利用DRAM+SSD+HDD的空间，因此存储总容量是所有KV中最大的。
对于dezhouv，不同的后端进程，后端进程数越大耗时越大，取x=90%观察，对于Get指令，可以看到1个后端时耗时最短，约30ms，5个后端进程时耗时约为70ms，对于Set指令，一个后端进程时耗时为20ms，6个后端进程时耗时为80ms。