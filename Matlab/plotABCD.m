type = {'s','b','w','d'};
loc = {'a','b','c','d'};
dis = {'2m','4m','6m','8m'};
color = 'rgbm';

% i_type = 2;
% i_loc = 3;
i_dis = 1;
% i_color =1;
i_P = 0;
for i_type = 2:3
    for i_loc = 1:4
%         for i_dis = 1:4

% % Plot RSSI curve
% figure(1);
% plot(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])),color(i_color));
% % Plot Hist of RSSI
% figure(2);
% hist(eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])),20);
i_P = i_P +1;
% Fit Weibull distribute
% P(i_P,:) = wblfit(-1*eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));
% Plot as a Weibull
figure(i_P);
% title(cell2mat([type(i_type) loc(i_loc) dis(i_dis)]));
normplot(-1*eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));
% wblplot(-1*eval(cell2mat([type(i_type) loc(i_loc) dis(i_dis)])));

%         end
    end
end
    
    
    