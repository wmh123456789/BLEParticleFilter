function plotpdffit(x,pdf)

% Plot the hist
[N Bins] = hist(x,max(x)-min(x));
Bins = Bins+0.5
stem(Bins,N/length(x)); hold on;

% Plot the pdf fit
switch pdf
    case 'wbl'
        [lambda,k,theta] = CalcWblParam(x);
        Y = wblpdf(Bins-theta,lambda,k+2);        
        plot(Bins,Y,'r') ;    
    case 'norm'
        [miu, sigma] = normfit(x);
        Y = normpdf(Bins,miu,sigma);
        plot(Bins,Y,'g');
    otherwise
        'Not Support yet'
end
   
    
