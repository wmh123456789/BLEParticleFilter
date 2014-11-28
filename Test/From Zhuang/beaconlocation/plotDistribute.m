function plotDistribute(RSSI,figurenum)

for k=1:12
    mi(k)=min(RSSI{k});
    ma(k)=max(RSSI{k});
    A{k}=zeros(1,ma(k)-mi(k)+1);
    num=length(RSSI{k})
    for l=1:num
        A{k}(RSSI{k}(l)-mi(k)+1)= A{k}(RSSI{k}(l)-mi(k)+1)+1;
    end
    x=linspace(mi(k),ma(k),ma(k)-mi(k)+1);
    figure(figurenum+k-1);
    plot(x,A{k});

end

