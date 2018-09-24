%first derivative
h = diff(X);
n = length(X);
dy = diff(Y)./diff(X);
xc = X(1:n-1);

%plot(xc,dy,X,Y)

%second derivative
dz = diff(dy)./diff(h);
xcc = X(1:n-2);
plot (xcc,dz,xc,dy)