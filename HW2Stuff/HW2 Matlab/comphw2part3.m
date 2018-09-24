r = linspace(0,2,20);

phi = linspace(0,2*pi,20);
u = 1;
%phimax = 2*pi;
v3 = [1:20];
%rmax = @(phi) 2./(sin(phi) + cos(phi));

while u<21
    fun3 = @(r,phi) 9*10^(9)*r.*cos(phi)./(sqrt((rx(u)-r).^2));
    v = integral2(fun3, phi(1), phi(end), r(1),r(end));
    v3(u) = v;
    u = u + 1;
end

plot(rx,v)
    