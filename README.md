# video_analysis
## 2022.7.11
1.当出现不在小白块里面的新目标的时候。怎么办呢?如何去修复异常情况。  
2.如何优雅的解决一下关键点黏连问题。  
3.如何将物体的目标大小和目标检测算法的大小联系起来，用一个合适的估计量或者是什么。  
## 2022.7.18
与李老师开完会之后确定第三点可以不用做了  
1.凝练文章的中心思想，与infocom等文章的论述做对比，定下论文题目。  
2.针对文章的中心思想做进一步完善。  
3.在两个数据集上有稳定结果，往移动端部署。  
目前来看先解决两个问题：  
（1）出现不在小白块的新目标怎么办。完全没有思路==  
（2）触发完目标检测之后的冷启动，调整卡尔曼滤波的权值看看。  
