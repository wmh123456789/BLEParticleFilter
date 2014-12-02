% plot(ba2m,'b');hold on;
% plot(bb2m,'r');hold on;
% plot(bc2m,'g');hold on;
% plot(bd2m,'k');hold on;

% plot(wa2m,'b');hold on;
% plot(wb2m,'r');hold on;
% plot(wc2m,'g');hold on;
% plot(wd2m,'k');hold on;

% plot(sa2m,'b');hold on;
% plot(sb2m,'r');hold on;
% plot(sc2m,'g');hold on;

type = {'s','b','w','d'};
loc = {'a','b','c','d'};
dis = {'2m','4m','6m','8m'};
color = 'rgbm';

i_type = 2;
i_loc = 3;
i_dis = 1;
i_color =1;

figure(1);
plot(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])),color(i_color));
figure(2);
hist(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])),20);


    
    
    
    