function  [RSSI]=findbeacon(filename,beaconid)

addpath('../beaconlocation');
addpath('../beaconlocation/data3');

fid=fopen(filename,'rt');
if fid==-1
     disp('error reading')
    RSSI=-100;
end

RSSI=-100;
num=1;
while feof(fid) == 0
   tline=fgetl(fid);
   if tline(1)=='/'
       continue;
   end
   flag=strfind(tline,beaconid);
   if ~isempty(flag)
       n=length(tline);
       RSSI(num)=str2double(tline(n-3:n));
       num=num+1;
   end
end

fclose(fid);