function  [RSSI]=findbeacon_iphone(filename,uuid,idnum)

addpath('../beaconlocation');
addpath('../beaconlocation/data3_iphone');

fid=fopen(filename,'rt');
if fid==-1
     disp('error reading')
    RSSI{1}(1)=-100;
end

RSSI{1}(1)=-100;

num=ones(1,idnum);
while feof(fid) == 0
   tline=fgetl(fid);
   
   if tline(1)=='/'||tline(1)=='#'
       continue;
   end
   
%    [id,major,minor,RSSI_ele,Accuracy]=sscanf(tline,'%36s %n %n %n %f');
    id=tline(1:length(uuid));
    tline_temp=tline(length(uuid)+1:length(tline));
    a=sscanf(tline_temp,'%d');
    minor=a(2); RSSI_ele=a(3);
   
   flag=strfind(id,uuid);
   
   if ~isempty(flag)
       
       if minor>=1&&minor<=idnum
           if RSSI_ele~=0
            RSSI{minor}(num(minor))=RSSI_ele;
            num(minor)=num(minor)+1;
           elseif a(4)~=-1
            RSSI{minor}(num(minor))=-100;
            num(minor)=num(minor)+1;  
           end
       end
              
   end
   
end

fclose(fid);