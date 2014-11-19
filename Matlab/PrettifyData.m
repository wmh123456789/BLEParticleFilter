% Remove 0 and 127

function newdata = PrettifyData(data)
L = length(data);
newdata = 0;
j = 1; 
for i = 1:L
    if data(i)~=0 && data(i)~=127
        newdata(j) = data(i);
        j = j+1;
    end
end
