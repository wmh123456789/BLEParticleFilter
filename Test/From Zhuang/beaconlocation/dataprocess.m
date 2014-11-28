clc;clear;

addpath('../beaconlocation');
addpath('../beaconlocation/data2');

data_path{1} = '1_20141123T155740.txt';
data_path{2}='2_20141123T155916.txt';
data_path{3}='3_20141123T160050.txt';
data_path{4}='4_20141123T160218.txt';
data_path{5}='5_20141123T160443.txt';
data_path{6}='6_20141123T160608.txt';
data_path{7}='7_20141123T160722.txt';
data_path{8}='8_20141123T160845.txt';
data_path{9}='9_20141123T161018.txt';
data_path{10}='10_20141123T161150.txt';
data_path{11}='11_20141123T161314.txt';
data_path{12}='12_20141123T161430.txt';

beaconid1='B4:99:4C:8A:AE:9F';
beaconid2='B4:99:4C:8A:C7:D4';
beaconid3='78:A5:04:41:5A:26';
beaconid4='78:A5:04:42:15:77';

for k=1:12
    RSSI1{k}=findbeacon(data_path{k},beaconid1);
    RSSI2{k}=findbeacon(data_path{k},beaconid2);
    RSSI3{k}=findbeacon(data_path{k},beaconid3);
    RSSI4{k}=findbeacon(data_path{k},beaconid4);
end

plotK(RSSI1,1);
plotK(RSSI2,2);
plotK(RSSI3,3);
plotK(RSSI4,4);





