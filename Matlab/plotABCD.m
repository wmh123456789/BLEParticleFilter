type = {'s','b','w','d'};
loc = {'a','b','c','d','e','f','g','h','o'};
% dis = {'2m','4m','6m','8m'};
% dis = {'3m','5m','7m','9m'};
dis = {'2m','3m','4m','5m','6m','7m','8m','9m'};
color = 'rgbm';

% i_type = 2;
% i_loc = 3;
% i_dis = 2;
% i_color =1;
i_P = 0;
for i_type = 2:2
    for i_loc = 1:1
        for i_dis = 1:8

% % Plot RSSI curve
% figure(1);
% plot(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])),color(i_color));
% % Plot Hist of RSSI
% figure(2);
% hist(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])),20);
i_P = i_P +1;

% Fit Weibull/norm distribute
% P(i_P,:) = wblfit(-1*eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));
% [P(i_P,1) P(i_P,2)] = normfit(-1*eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));
[P(i_P,1) P(i_P,2) P(i_P,3)] =  CalcWblParam(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));
P(i_P,4) = P(i_P,1)+ P(i_P,3);
P(i_P,5) = mean(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));

% Plot Weibull/Norm fit 
figure(i_P);
plotpdffit(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])),'wbl');
plotpdffit(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])),'norm');

% Plot as a Weibull/Norm
% figure(i_P);
% title(cell2mat([type(i_type) loc(i_loc) dis(i_dis)]));
% normplot(-1*eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));
% wblplot(-1*eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));




        end
    end
end
    
    
    