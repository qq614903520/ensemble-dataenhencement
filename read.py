#coding=utf-8
#write by jiangjie666
import os
import caffe
import numpy as np
root='/home/caffe/caffe/'
deploy=root+'/home/caffe/caffe-rc/models/bvlc_googlenet/deploy.prototxt'
caffe_model=root+''
fm=open(r'read1.txt')
tt=fm.readlines()
print tt[0]
for line in tt:
    print line 
def TEST(img):
    net=caffe.Net(deploy,caffe_model,caffe.TEST)
    transformer=caffe.io.Transformer({'data':net.blobs['data'].data.shape})
    transformer.set_transpose('data', (2,0,1))
     #transformer.set_mean('data', np.load(mean_file).mean(1).mean(1)) 
    transformer.set_raw_scale('data', 255)
    transformer.set_channel_swap('data', (2,1,0))
    im=caffe.io.load_image(img)
    net.blobs['data'].data[...] = transformer.preprocess('data',im)
    out = net.forward()
    labels = np.loadtxt(labels_filename, str, delimiter='\t')
    prob= net.blobs['prob'].data[0].flatten()
    print prob
    order=prob.argsort()[4] 
    print 'the class is:',labels[order] 
    f=file("/home/caffe/cooo/LA.txt","a+")
    f.writelines(img+' '+labels[order]+'\n')
    labels_filename = root +'/home/caffe/cooo/numii.txt' 
TEST(img)
