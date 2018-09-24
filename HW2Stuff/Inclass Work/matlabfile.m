period = integral(v, x(1), x(end))

i = 0;
g=[1:4];
ui = [1:4];
while i<5
    
    vg = @(x) 4./(x.^4 + i^4);
    ui(i+1) = i;
    periodv = integral(vg, x(1), i);
    g(i+1) = periodv;
    i = i + 1;
    
end
g
ui
plot(ui,g)
