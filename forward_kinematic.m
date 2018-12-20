% Forward Kinematic
% Input = joint angles = theta, joint lengths = l
% Output = actual position (xa, ya)
function [xa, ya] = forward_kinematic(theta, l, n)
c = 0;
theta_abs = 0;
xa = 0;
ya = 0;
for i = 1: n %size(theta,1) %n 
    j = i;
    while j ~= 0
        %calculate absolute theta
        theta_abs = theta_abs + theta(j);
        j = j - 1;
    end
    
    % x component
    xa =  xa + l(i)* cos(theta_abs);
    
    % y component
    ya =  ya + l(i)* sin(theta_abs);
    
    % z component is zero 
    
    theta_abs = 0; %make it zero for every iteration
    
    c=c+1;

end
end