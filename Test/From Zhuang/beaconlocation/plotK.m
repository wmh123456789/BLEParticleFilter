function plotK(RSSI,figurenum)

for k=1:12
    M(k)=mean(RSSI{k});
    mi(k)=min(RSSI{k});
    ma(k)=max(RSSI{k});
end

x=linspace(1,12,12);
figure(figurenum);
scatter(x,M,'o');
hold on;

for k=1:12
  line([x(k),x(k)],[mi(k),ma(k)]);
end
 axis([0 10 -100 -50])
