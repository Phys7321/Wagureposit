%%Part A
[period,sol]=pendulum_mod4(3,0.5,2,1,0);
t=sol(:,1);
x=sol(:,2);

figure(1)
plot(t,x);
title('theta vs time with theta = 1 thetadot = 0');
xlabel('time');
ylabel('theta');


[period,sol]=pendulum_mod4(3,0.5,2,0,1);
t=sol(:,1);
x=sol(:,2);

figure(2)
plot(t,x);
title('theta vs time with theta = 0 thetadot = 1');
xlabel('time');
ylabel('angle');

%%Part B
[period,sol]=pendulum_mod4(3,0.5,1,1,0);
t=sol(:,1);
x=sol(:,2);
period1=period;
frequency1=2*pi/period1;

figure(3)
plot(t,x);
title('part(b): theta vs time for omega = 1');
xlabel('time');
ylabel('angle');

[period,sol]=pendulum_mod4(3,0.5,4,1,0);
t=sol(:,1);
x=sol(:,2);
period4=period;
frequency4=2*pi/period4;

figure(4)
plot(t,x);
title('theta vs time for omega = 4');
xlabel('time');
ylabel('angle');

%%Part C






