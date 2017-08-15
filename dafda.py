#coding=utf-8
#write by jiangjie666
import os
from collections import Counter
fm=open(r'/home/caffe/cooo/max.txt')
tt=fm.readlines()
print tt[0]
for line in tt:
    #print line
    ress=line.split(',') 
    print ress
    #label=range(0,431)
    #print label
    #print len(label)
    #print Counter(ress)
    #print Counter(ress).most_common(2)
    pred=Counter(ress).most_common(3)
    print pred
    #print len(pred)
    print pred[0][0],pred[1][0],pred[0][1],pred[1][1]
    #print ress[18]
    if pred[0][1]>pred[1][1]:
        out=pred[0][0]
        #kaishi
    elif pred[0][1]==pred[1][1]:
        print [i for i, x in enumerate(ress) if x == pred[0][0]]
        xiab1=[i for i, x in enumerate(ress) if x == pred[0][0]]
        #print [i for i, x in enumerate(ress) if x == pred[1][0]]
        xiab2=[i for i, x in enumerate(ress) if x == pred[1][0]]
        topcaf1=0
        topvg1=0
        topgo1=0
        for xia1 in xiab1:
            #print xia1
            if xia1 in [0,1,2,3,4,5]:
                topcaf1 +=1
            elif xia1 in [6,7,8,9,10,11]:
                topvg1 +=1
            elif xia1 in [12,13,14,15,16,17]:
                topgo1 +=1
        print topcaf1,topvg1,topgo1
        print topcaf1*1.3+topvg1*1.2+topgo1*1.1
        fenshu1=topcaf1*1.3+topvg1*1.2+topgo1*1.1
        print 'fenshu1'+str(fenshu1)
        topcaf2=0
        topvg2=0
        topgo2=0
        for xia2 in xiab2:
            print xia2
            if xia2 in [0,1,2,3,4,5]:
                topcaf2 +=1
            elif xia2 in [6,7,8,9,10,11]:
                topvg2 +=1
            elif xia2 in [12,13,14,15,16,17]:
                topgo2 +=1
        print topcaf2,topvg2,topgo2
        print topcaf2*1.3+topvg2*1.2+topgo2*1.1
        fenshu2=topcaf2*1.3+topvg2*1.2+topgo2*1.1
        print 'fenshu2'+str(fenshu2)
        print 'dadqaf'
        if fenshu1>fenshu2:
            out=pred[0][0]
        else:
            out=pred[1][0]
        print 'out wei '+out
    score=0
    real=ress[18].rstrip()
    print real+'jdaida'
    if str(out)==str(real):
        print ress[18]+'666'
        score+=1
        print str(score)+'sss'
        print 'sada'
        #dadij
        uiui=open('score.txt','a')
        uiui.write(str(score)+'\n')
        uiui.close
  
        


    
    
    
    
    
    

