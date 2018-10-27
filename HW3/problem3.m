%3a
[period,sol]=pendulum_damped(3,1,0,0.5,0);
t=sol(:,1);
x=sol(:,2);
v=sol(:,3);

figure(1)
plot(t,x);
xlabel('time');
ylabel('theta');
title('angle vs time');

figure(2)
plot(t,v);
xlabel('time');
ylabel('angular velocity');
title('angular velocity vs time');

perioddamp=zeros(4,1);
kem = zeros(4,1);
pem = zeros(4,1);
eavgm = zeros(4,1);
gammam = [0.5,1,2,3];
periodun = zeros(4,1);
keundamp = zeros(4,1);
peundamp = zeros(4,1);
eundamp = zeros(4,1);

i = 1;
while i<5
    gamma = gammam(i);
   [period,sol,kinetic,potential,Etot] = pendulum_damped(3,gamma,1,0,0);
    perioddamp = period;
    keavg=mean(kinetic);
    peavg=mean(potential);
    eavg = mean(Etot);
    perioddamp(i) = perioddamp;
    kem(i) = keavg;
    pem(i) = peavg;
    eavgm(i) = eavg;
    gammam(i) = i;
    [period,sol,kinetic,potential,Etot] = pendulumod(3,1,0,0);
    periodun(i) = period;
    keundamp(i) = mean(kinetic);
    peundamp(i) = mean(potential);
    eundamp = mean(Etot);
    i = i + 1;
end
%Not working
freqdamp = 2*pi./perioddamp;
frequndamp = 2*pi./periodun;

figure(1)
plot(gammam,freqdamp,gammam,frequndamp);
title('part b Frequencies vs Gammas');
xlabel('Gamma value');
ylabel('Frequency')
legend('Damped Frequency','Undamped Frequency');

figure(2)
plot(gammam,kem,gammam,keundamp);
title('part b Kinetic Energies Average vs Gammas');
xlabel('Gamma value');
ylabel('KE Average(units)')
legend('Damped','Undamped');
figure(3)
plot(gammam,pem,gammam,peundamp);
title('part b Potential Energie Average vs Gammas');
xlabel('Gamma value');
ylabel('PE Average(units)')
legend('Damped','Undamped');
figure(4)
plot(gammam,eavgm,gammam,eundamp);
title('part b Average Energies vs Gammas');
xlabel('Gamma value');
ylabel('Total Energy Average (units)')
legend('Damped','Undamped');