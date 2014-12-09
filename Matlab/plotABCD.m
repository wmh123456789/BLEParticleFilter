type = {'s','b','w','d'};
loc = {'a','b','c','d'};
% dis = {'2m','4m','6m','8m'};
dis = {'3m','5m','7m','9m'};
color = 'rgbm';

% i_type = 2;
% i_loc = 3;
% i_dis = 2;
% i_color =1;
i_P = 0;
for i_type = 1:1
    for i_loc = 1:3
        for i_dis = 4:4

% % Plot RSSI curve
% figure(1);
% plot(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])),color(i_color));
% % Plot Hist of RSSI
% figure(2);
% hist(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])),20);
i_P = i_P +1;

% Fit Weibull/norm distribute
% P(i_P,:) = wblfit(-1*eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));
[P(i_P,1) P(i_P,2)] = normfit(-1*eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));

% Plot as a Weibull/Norm
% figure(i_P);
% title(cell2mat([type(i_type) loc(i_loc) dis(i_dis)]));
% normplot(-1*eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));
% wblplot(-1*eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));

        end
    end
end
    
    
    