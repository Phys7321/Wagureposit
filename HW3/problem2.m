%Large oscillation values?
[period,sol,kinetic,potential,Etot]=pendulumod(4,2,0);
t=sol(:,1);
x=sol(:,2);
v=sol(:,3);

figure(1)
plot(t,Etot);
title('Total Energy vs time');
xlabel('t');
ylabel('Energy');

%Different omega0 values

figure(2)
for i = [0.1,0.2,0.4,0.8,1.0]
    [period,sol] = pendulumod(4,i,0);
    plot(sol(:,1),sol(:,2))
    hold on;
end
title('Angle vs Time')
xlabel('t')
ylabel('theta')
legend('0.1','0.2','0.4','0.8','1.0')

figure(3)
for j = [0.1,0.2,0.4,0.8,1]
    [period,sol]=pendulumod(3,j,0);
    plot(sol(:,1),sol(:,3))
    hold on;
end

title('angular velocity vs time')
xlabel('t')
ylabel('theta dot')
legend('0.1','0.2','0.4','0.8','1')