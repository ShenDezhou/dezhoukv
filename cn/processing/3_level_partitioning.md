通过将数据分成(0-3.378%),(3.378%-10.09%)和(10.09%,100%)的方式，将系统的分成3层，系统的平均响应时间为![公式名](http://latex.codecogs.com/png.latex?%5cbar%7bV}=0.03378*V_1+0.06712*V_2+0.8991*V_3)，假设V<sub>1</sub>=1/135000,V<sub>2</sub>=1/17000,V<sub>3</sub>=1/3400(50%使用率的响应时间）,那么理论平均V=1/3722.5,即系统的理论平均IOPS为3722.5。    
通过3层等级的设计可以充分发挥异构（异构：不同节点设备有不同的DRAM、SSD空间以及HDD空间）节点的性能，同时保留了灵活性和效率。