clc;clear;

addpath('../beaconlocation');
addpath('../beaconlocation/data3_iphone');

data_path{1} = '1.txt';
data_path{2}='2.txt';
data_path{3}='3.txt';
data_path{4}='4.txt';
data_path{5}='5.txt';
data_path{6}='6.txt';
data_path{7}='7.txt';
data_path{8}='8.txt';
data_path{9}='9.txt';
data_path{10}='10.txt';

% beaconid=['D0:39:72:E8:05:69','B4:99:4C:8A:D1:EF','B4:99:4C:8A:C1:5E','D0:39:72:E8:06:94','D0:39:72:B7:DA:CD','D0:39:72:E8:06:9B','B4:99:4C:8A:C1:5A'];
uuid='E2C56DB5-DFFB-48D2-B060-D0F5A71096E0';
idnum=7;

for k=1:10
   RSSI{k}=findbeacon_iphone(data_path{k},uuid,idnum);
end

 for k=1:10
    a=size(RSSI{k});
     for l=1:a(2)
         vector{k}(l)=mean(RSSI{k}{l});
     end
 end




