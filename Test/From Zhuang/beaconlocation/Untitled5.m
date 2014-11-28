for k=1:10
    
     for l=1:length(vector_iphone{k})
        if vector_iphone{k}(l)==NaN
            vector_iphone{k}(l)=-100;
        end
    end
     if length(vector_iphone{k})<7
        for l=length(vector_iphone{k})+1:7
            vector_iphone{k}(l)=-100;
        end
     end

    
end


x=linspace(1,7,7);
for k=1:10
    figure(k)
    plot(x,vector{k});
    hold on;
    plot(x,vector_iphone{k},'r--');
     axis([1 7 -100 -40])
end
