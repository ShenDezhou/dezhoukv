通过将数据分成(0-3.378%),(3.378%-10.09%)和(10.09%,100%)的方式，将系统的分成3层，系统的平均响应时间为![公式名](http://latex.codecogs.com/png.latex?%5cbar%7bV}=0.03378*V_1+0.06712*V_2+0.8991*V_3)，假设V<sub>1</sub>=50,V<sub>2</sub>=500,V<sub>3</sub>=7000,那么理论平均V=6328.949。    
但由于域空间三种介质的Key比例为4：10：1，因此有4/15可能出现n（1-2)次回捞，有2/3的数据可能发生1次回捞，所以系统的介质请求次数![公式名](http://latex.codecogs.com/png.latex?%5cbar%7bN}=0.2667*2+0.6667*1.5+0.06667*1)=1.6001次。    
通过3层等级的设计可以充分发挥异构节点的性能，同时保留了灵活性和效率。