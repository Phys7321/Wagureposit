[period, sol, kinetic, potential, Etot] = pendulumod(3,0.25,0);

t=sol(:,1);
x=sol(:,2);
v=sol(:,3);
deltaE=(Etot-Etot(1))./Etot(1);

figure(1)
plot(t,x)
title('Position vs time')
xlabel('t')
ylabel('x')

figure(2)
plot(t,v)
title('velocity vs time')
xlabel('t')
ylabel('v')

figure(3)
plot(t,deltaE)
title('Delta E vs time')
xlabel('t')
ylabel('DeltaE')

figure(4)
plot(t,Etot)
title('Energy vs time')
xlabel('t')
ylabel('E')

figure(5)
plot(t,kinetic,t,potential)
title('PE and KE vs time')
legend('Kinetic Energy','Potential Energy')
xlabel('t')
ylabel('Energies')

figure(6)
plot(x,v)
title('Phase Space')
xlabel('x')
ylabel('v')


