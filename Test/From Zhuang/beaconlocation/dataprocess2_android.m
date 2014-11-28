clc;clear;

addpath('../beaconlocation');
addpath('../beaconlocation/data3');

data_path{1} = '1_20141124T140010.txt';
data_path{2}='2_20141124T140435.txt';
data_path{3}='3_20141124T140720.txt';
data_path{4}='4_20141124T141040.txt';
data_path{5}='5_20141124T141400.txt';
data_path{6}='6_20141124T141630.txt';
data_path{7}='7_20141124T142346.txt';
data_path{8}='8_20141124T142626.txt';
data_path{9}='9_20141124T142953.txt';
data_path{10}='10_20141124T143218.txt';

beaconid=['D0:39:72:E8:05:69','B4:99:4C:8A:D1:EF','B4:99:4C:8A:C1:5E','D0:39:72:E8:06:94','D0:39:72:B7:DA:CD','D0:39:72:E8:06:9B','B4:99:4C:8A:C1:5A'];
% uuid='E2C56DB5-DFFB-48D2-B060-D0F5A71096E0';
 idnum=7;

for k=1:10
    for l=1:idnum
        RSSI{k}{l}=findbeacon(data_path{k},beaconid(k));
    end
end

 for k=1:10
     for l=1:7
         vector{k}(l)=mean(RSSI{k}{l});
     end
 end
