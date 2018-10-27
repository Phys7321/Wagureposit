function [period,sol,kinetic,potential, Etot] = pendulum_damped(omega0,gamma,theta0,thetad0,grph) 
% Finds the period of a nonlinear pendulum given the length of the pendulum
% arm and initial conditions. All angles in radians.

%Setting initial conditions
if nargin==0 %nargin is the number of arguments put in the stuff in pendulum
    error('Must input length and initial conditions')
end 
if nargin==1
   theta0 = pi/2;
   thetad0=0;
   grph=1;
   gamma = 0;
end
if nargin==2
    theta0 = pi/2;
    thetad0 = 0;
    grph=1;
end
if nargin==3
    thetad0 = 0;
    grph=1;
end
if nargin == 4
    grph = 1;
end

g=9.81;
R = g/omega0^2;

T= 2*pi/omega0;
% number of oscillations to graph
N = 10;%ode 45 solve me 10 periods

%code to solve exact pendulum problems
tspan = [0 N*T];
%opts = odeset('events',@events,'refine',6); %Here for future event finder
opts = odeset('refine',6);
r0 = [theta0 thetad0]; %[initial position initial velocity]
[t,w] = ode45(@proj,tspan,r0,opts,g,gamma,R); %spits back in @proj thetadot and thetadotdot
sol = [t,w];
ind= find(w(:,2).*circshift(w(:,2), [-1 0]) <= 0); %(:,2) all rows second columns WHAT DOES CIRCSHIFT DO?
ind = chop(ind,4);          %circshift multiply w by sencond column of w at instant of velocity change
period= 2*mean(diff(t(ind)));

% Small-angle approximation solution
delta = atan(theta0/(omega0*thetad0));
y = theta0*sin(omega0*t+delta);

    

if grph % Plot Solutions of exact and small angle
    subplot(2,1,1)
    plot(t,w(:,1),'k-',t,y,'b--')
    legend('Exact','Small Angle')
    title('Exact vs Approximate Solutions')
    xlabel('t')
    ylabel('\phi')
    subplot(2,1,2)
    plot(t,w(:,1)-y,'k-')
    title('Difference between Exact and Approximate')
    xlabel('t')
    ylabel( '\Delta\phi')
end

time=floor(5*T);
index=find(t<=time);
index=max(index);
sol=sol(1:index,1:3);

m = 1;
kinetic=0.5*m*R^2.*sol(:,3).*sol(:,3);
potential=m*g*R*(1-cos(sol(:,2)));
Etot = kinetic + potential;

    
end
%-------------------------------------------
%

function rdot = proj(t,r,g,R,gamma)
    rdot = [r(2); -gamma.*r(2)-g/R*(r(1))]; %thetadot and thetadotdot, semicolon makes it a column vector
end


    
