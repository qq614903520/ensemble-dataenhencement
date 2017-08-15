#coding=utf-8
#write by jiangjie666
import os
llll=open('score.txt','r')
tt=llll.readlines()
nnnn=open('score1.txt','r')
rrr=nnnn.readlines()
print len(tt),len(rrr)
aaa=len(tt)
bbb=len(rrr)
ttfloat=float(str(aaa))
rrrfloat=float(str(bbb))
accurity=rrrfloat/ttfloat
print '准确率'+str(accurity)
