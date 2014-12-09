function [lambda,k,theta] = CalcWblParam(X)

delta = std(X);
k = delta/log(2);
if delta < 2
    lambda = 2*(k+0.15);
elseif delta <= 3.5
    lambda = delta*(k+0.15);
else
    lambda = 3.5*(k+0.15);
end
 theta = mean(X)-lambda*gamma(1+1/k);
 
    
