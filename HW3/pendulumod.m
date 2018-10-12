function [period,sol,kinetic,potential, Etot] = pendulumod(omega0,theta0,thetad0,grph) 
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
end
if nargin==2
    thetad0 = 0;
    grph=1;
end
if nargin==3
    grph=1;
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
[t,w] = ode45(@proj,tspan,r0,opts,g,R); %spits back in @proj thetadot and thetadotdot
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

    m = 1;
    kinetic = 0.5*m.*w(:,2).^2;
    potential = 0.5*omega0^2*m.*w(:,1).^2;
    Etot = kinetic + potential;

    
end
%-------------------------------------------
%

function rdot = proj(t,r,g,R)
    rdot = [r(2); -g/R*(r(1))]; %thetadot and thetadotdot, semicolon makes it a column vector
end


    
