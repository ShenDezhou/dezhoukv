一个结构化数据根据MurmurHash3_128映射成128bit, 将高位64bit与低位64bit异或得到64bit的三维空间体积值，归一化后得到-10<sup>10</sup>~5\*10<sup>9</sup>区间的一个值，（归一化公式：![归一化](http://latex.codecogs.com/png.latex?f(x%29=xmod({1.5*{10^{10}}}%29-{7.5*{10^{9}}})），再根据速算公式求得向量u的值。   
（速算公式：![速算](http://latex.codecogs.com/png.latex?u=%5Cbegin{cases}i%26(-10%5E%7B10%7D%2C0%5D\\j%26%280%2C10%5E9%5D\\k%26%2810%5E9%2C5*10%5E9%5D%5Cend{cases})）。
