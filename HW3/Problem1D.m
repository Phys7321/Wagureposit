[period, sol, kinetic, potential, Etot] = pendulumod(3,1,0.5);

t=sol(:,1);
x=sol(:,2);
v=sol(:,3);
deltaE=(Etot-Etot(1))./Etot(1);

figure(1)
plot(x,v)
title('Phase Space')
xlabel('x')
ylabel('v')