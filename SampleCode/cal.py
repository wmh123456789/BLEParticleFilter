# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 10:59:15 2014

@author: XiaolongShen
"""
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imresize
import time
class calculation:
	def __init__(self,loadfile):
		try:
		#            self.map = plt.imread(mapfile);
		#            tmap = self.map[:,:,0]*255;
		#            self.refmap = imresize(tmap,(int_(tmap.shape[0]/10),int_(tmap.shape[1]/10)));
		#            print "Image Loaded In"
			self.dataZip=load(loadfile);
			print self.dataZip.keys()
			self.SignalStrength=self.dataZip['para'][:,1];
			self.Alpha = self.dataZip['para'][:,0];
			self.Position = self.dataZip['pos'];
			self.Wlist = array(self.dataZip['wlist']).tolist();
			# print self.Wlist
			self.refmap = self.dataZip['rtmap'];
			print self.refmap.shape
		except:
			print "No File Found"    


	def inner(self,WIFI,WIFIVALUE,D):
		if WIFI in D:
			D[WIFI].append(int(WIFIVALUE));
		else:
			D[WIFI]=[];
			D[WIFI].append(int(WIFIVALUE));
		return D
	def EXTTESTWIFIVALUE(self,warray,TestF):
		f=TestF.split('\n');
		D={};
		for l in f:
			ls=l.split('\t');
			if (len(ls)==5):
				D=self.inner(ls[1],ls[3],D);
			elif(len(ls)==4):
				D=self.inner(ls[0],ls[3],D);
		return D

	def EXTTESTWIFIVALUE2(self,warray,TestF):
		f=TestF.split('\n');
		D={};
		l_old='abasdfasdfasdf';
		for l in f:
			if len(l)<8:
				continue;
			if l[6:]==l_old[6:]:
				continue;
			l_old=str(l);
			ls=l.split(' ');
			for i in range(1,len(ls)-1,2):
				D=self.inner(ls[i],ls[i+1],D);
		return D

	def calInfoInput(self,info):
		D=self.EXTTESTWIFIVALUE2(self.Wlist,info);print D;
		return D    

	def calInfoInputFile(self,filename):
		# print self.Wlist;
		# print filename
		D=self.EXTTESTWIFIVALUE(self.Wlist,filename);print D;
		return D
	def costFunc(self,x,TEST):
		tSST=0;
		d0=1.6;
		S=0;
#		cv=ctypes.c_double;
		for n in TEST.keys():
			if n in self.Wlist:
				ind=self.Wlist.index(n);
				POS=self.Position[ind,:];
				alpha=self.Alpha[ind];
				SS=self.SignalStrength[ind];
				if alpha<=0.5 or SS<-80:
					continue;
				st=time.time();
				D=sqrt((POS[0]-x[:,0])**2+(POS[1]-x[:,1])**2);
				# print D
				R=20*log10(D/d0);
				for i in TEST[n]:
					tSST=tSST+(SS-alpha*R-i)**2;
				ed=time.time();
				S=S+ed-st;
		return -tSST;
	def updateweight(self,x,w,wifiinfo):
		D = self.calInfoInputFile(wifiinfo);
		# print D
		val = self.costFunc(x,D);
		# print "VAL MAX:%s, MIN:%s" %(val.max(),val.min())
		# val = val/sum(val);
		# print val
		val = 1./(1.-val);
		# val = sqrt(sqrt(val**2));


		####This is a crazy experiment, delete these code as soon as possible. Otherwise the world will be destroyed.
		if not(type(val) == type(1) or type(val) == type(1.1)):
			val = val**2;
			# val = val/(val.max()-val.min());
			# val = power(val,0.1)
			valscale = 10;
			val = val*valscale;



		###
		w = w*val;
		# w = array(w)/(1.- val);
		# w = w**2;
		# w = w/sum(w);
		f0 = 255.;
		try:
			ref = f0 - self.refmap[int_(x[:,1]),int_(x[:,0])];
		except:
			s0 = int_(self.refmap.shape[0]);
			s1 = int_(self.refmap.shape[1]);
			xx = x.clip(zeros(2),array([s1,s0])-2)
			ref = f0 - self.refmap[int_(xx[:,1]),int_(xx[:,0])]
		#        print ref
		val = w/(1.+ref*100)**10;
		val = val/sum(val);
		#        print val
		return val
	def updateMap(self,x,w):
		f0 = 255.;
		try:
			ref = f0 - self.refmap[int_(x[:,1]),int_(x[:,0])];
		except:
			s0 = int_(self.refmap.shape[0]);
			s1 = int_(self.refmap.shape[1]);
			xx = x.clip(zeros(2),array([s1,s0])-2)
			ref = f0 - self.refmap[int_(xx[:,1]),int_(xx[:,0])]
		#        print ref
		val = w/(1.+ref)**5;
		val = val/sum(val);
		#        print val
		return val		
#
#cal=calculation('2F.png');
#plt.imshow(cal.map[:,:,0]);
#plt.show()
#cal=calculation('data_New.npz','2F.png');
