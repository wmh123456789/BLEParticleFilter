# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 14:35:24 2014

@author: XiaolongShen
"""
from numpy import *
#from numpy.random import *
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from cal import *
import yaml
class particle(object):
    '''
    AD=Angel Deviation
    LD=Length Deviation
    n = particle number
    initpos = initialized start point
    map2 = map size
    '''
    def __init__(self,AD,LD,n,initpos,cal):
        #Send In
        self.AD=AD;
        self.LD=LD;
        self.number=n;
        self.cal = cal;

        #PreSet---Look into The config Yaml File
        #Load Yaml Config
        f = open('partConf.yaml')
        x = yaml.load(f)
        f.close();
        self.conf = x;



        #Init Part
        self.ResampleCount = 0;
        self.AngDif = 0;
        self.InitStack = 5;
        self.x=ones((n,2),float)*initpos;
        initsize=4;
        map2 = cal.dataZip['map'];
        print map2
        self.map2= map2;
        self.ref = random.randint(0,1,n);
        self.div = False;
        self.weight = ones(self.number)/self.number;
        #Init Spread
        # self.x+=random.uniform(-initsize,initsize,self.x.shape);
        # self.x=self.x.clip(zeros(2),array([map2[0],map2[1]])-2);
        # self.weight = ones(n)/n;
        print "Init Start"
        # self.InitSprad();
        print "Start End"
        #Read From Configuration
        self.AngCount = x['InitAngStack'];
        initang = float(x['InitAngle']);
        self.angel = random.uniform(-(initang/180.*pi),(initang/180.*pi),self.number);

        tt = list(self.ref)
        print "-1:%s,1:%s,0:%s" %(tt.count(-1),tt.count(1),tt.count(0))
        pass;
#    def resample(self,weights):
#        print "Resample"
#        n = len(weights)
#        indices = []
#        C = [0.] + [sum(weights[:i+1]) for i in range(n)]
#        u0, j = random.random(), 0
#        for u in [(u0+i)/n for i in range(n)]:
#            while u > C[j]:
#                j+=1
#            indices.append(j-1)
#        return indices
    # def InitSprad(self):
    #     self.x= random.uniform(0,max(self.map2[0],self.map2[1]),self.x.shape);
    #     self.x=self.x.clip(zeros(2),array([self.map2[0],self.map2[1]])-2);
    #     self.weight = ones(self.number)/self.number;
    #     for i in range(2):
    #         w = self.cal.updateMap(self.x,self.weight);
    #         ind = self.resample(w);
    #         self.weight = w[ind];
    #         self.weight = self.weight / sum(self.weight);
    #         self.x = self.x[ind];
    #     pass;
    def InitSprad(self):
        K = where(self.cal.refmap==255);
        xo=hstack((K[1][:,newaxis],K[0][:,newaxis]))
        #increase to number
        ind = random.randint(0,xo.shape[0],self.number);
        x0=xo[ind,:];
        self.x = random.normal(loc=x0,scale = 1, size = x0.shape);
        print self.x
        self.weight = ones(self.number)/self.number;
    def resample(self,weights):
        print "Resample"
        n = len(weights)
        indices = []
        C = cumsum(weights);
        u0, j = random.random(), 0
        Li=(u0+arange(n))*(1./n);
        for u in Li:
            while u > C[j]:
                j+=1
            indices.append(j-1)
        return indices



    def compare(self,l):
        ind = 1;
        st = l[0];
        for n in l:
            if n > st:
                ind = l.index(n)+1;
                st = n;
        return str(ind)

    def updateWifi(self,ang,dis,wifiinfo):
        if ang == False:
            print "Call Only Wifi"
            xx = self.update2(wifiinfo);
            ww = self.weight;
            ww = ww/sum(ww);
        else:
            print "Call INS Update"
            xx = self.update(ang,dis,wifiinfo);
            ww = self.weight;
            ww = ww/sum(ww);
        if self.div == True:
            G={}
            G["1"]=where(self.ref==0)[0]
            G["2"]=where(self.ref==-1)[0];
            G["3"]=where(self.ref==1)[0];
            G["4"]=where(self.ref==2)[0];
            swg1=sum(ww[G["1"]]);
            swg2=sum(ww[G["2"]])
            swg3=sum(ww[G["3"]])
            swg4=sum(ww[G["4"]])
            flag = self.compare([swg1,swg2,swg3,swg4]);
            print "G1:%s  ,  G2:%s  ,  G3:%s  ,  G4:%s\n Selection: %s" %(swg1,swg2,swg3,swg4,flag)
            xs = xx[G[flag],:];
            ws = ww[G[flag]];
            ws = ws/sum(ws);
            return (xs.T*ws).T.sum(0),xs 
        else:
            return (xx.T*ww).T.sum(0),xx

    def update2(self,wifiinfo):
        # stepsize=self.stepsize;
        # n=self.number;
        # f0=array([[255,255,255]]);
        # for iter_count in xrange(iter_round):
        #     x=array(self.x);
        map2 = self.map2
        x = self.x;
        stepsize = 2;
        n = self.number;
        x= random.normal(loc=x,scale=stepsize,size=x.shape);
        x= x.clip(zeros(2),array([map2[0],map2[1]])-2);
        w = self.weight;
        w=self.cal.updateweight(x,w,wifiinfo);
#         val=cal.costFunc(x,info)
#         w=1./(1. - val);
#         w=w**2;
# #           w/=sum(w);
#         w=w/(1.+(f0-im[int_(x[:,1]),int_(x[:,0]),0:3]).sum(axis=1));
#         # w/=sum(w);
# #           w=w**2;
#         w/=sum(w);
#         # w=w/(1.+pred.val(info,x)*1e+3);
#         # w/=sum(w);
        if 1./sum(w**2) < n/2. :
            ind =int_(self.resample(w))
            x=x[ind,:];
            w = w[ind];
#           print "Call Resample"
        self.x=array(x).clip(zeros(2),array([map2[0],map2[1]])-2);
        self.weight = array(w);
#           self.w=array(w);
        return self.x      
    
    def update(self,ang,dis,wifiinfo):
        x = self.x;
        pa =self.angel;
        w= self.weight;
        map2 = self.map2
#        angel = arctan2(nextpos[1]-x[:,1],nextpos[0]-x[:,0]);
        AngD = 0;

        if abs(ang)>pi/self.conf['LargeTurnThredDelim']:
            self.AngCount = self.conf['AngDifStack'];
            AngD = abs(ang)/pi/3;
            self.AngDif = AngD;
        elif self.AngCount>0:
            self.AngCount-=1;
            AngD = self.AngDif;

        # print "Angle: %s,%s" %(AngD,self.AD)
        upang = random.normal(loc=ang, scale = AngD+self.AD, size = self.number);
#        dis = sqrt((nextpos[1]-x[:,1])**2+(nextpos[0]-x[:,0])**2);
        updis = random.normal(loc=dis, scale = self.LD, size = self.number);
        pa += upang;
#         if abs(ang) > pi/3:
#             print " add divergence"
# #            print self.ref
#             self.div = True;
#             K=random.randint(-1,3,self.number);
#             self.ref = K;
#             pa = pa + K*(pi/2);#$random.normal(loc = random.randint(-1,2,self.number)*(pi/2), scale = 2./180.*pi, size = self.number);
        tpa = pa;
#        print ang
#        print tpa
        x[:,0] = x[:,0] + cos(tpa)*updis;
        x[:,1] = x[:,1] + sin(tpa)*updis;
        for i in range(1):
            w=self.cal.updateweight(x,w,wifiinfo);
            self.weight = w
            self.angel = pa
            if 1./sum(w**2) < self.number/2.:                     # If particle cloud degenerate:
                self.ResampleCount+=1;
                if self.ResampleCount == self.conf['ResampleGapRound'] or self.InitStack>0:
                    # print "Resample"
                    self.InitStack-=1;
                    ind = self.resample(w);
                    self.ref = self.ref[ind];
                    self.weight = w[ind];
                    self.weight = self.weight / sum(self.weight);
                    self.x = x[ind];
                    self.angel = pa[ind]
                    self.ResampleCount=0;
        #            self.ref = self.ref[ind];
            else:
                pass;
            self.x=self.x.clip(zeros(2),array([map2[0],map2[1]])-2);
        #self.angel = pa;
        return self.x
