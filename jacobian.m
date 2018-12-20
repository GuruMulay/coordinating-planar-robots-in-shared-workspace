% Jacobian Calculation
% Input = joint angles = theta, joint lengths = l
% Output = Jacobian matrix
function [J_tip] = jacobian(theta, l, n)
c = 0;
temp = 0;
theta_abs = 0;
theta_absolute = zeros(n,1); %(n X 1) vector of absolute theta

%Absolute theta calculation for each of n links
for i = 1: n %size(theta,1) %n 
    j = i;
    while j ~= 0
        %calculate absolute theta
        theta_abs = theta_abs + theta(j);
        j = j - 1;   
    end
    theta_absolute(i,1) = theta_abs;
    theta_abs = 0; %make it zero for every iteration
end


for i = 1: n 
    print = sprintf('----------------- iteration = %d', i);
    
    % x component for link i %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    j = i;
    while j ~= n+1
        temp =  temp + l(j)* sin(theta_absolute(j,1));
        j = j + 1;   
    end
    
    % J_tip(1,i) = -l1*sin(theta1) - l2*sin(theta1 + theta2) .....
    J_tip(1,i) = -temp;
    temp = 0;
    
    % y component for link i %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    j = i;
    while j ~= n+1
        temp =  temp + l(j)* cos(theta_absolute(j,1));
        j = j + 1;
    end
    
    % J_tip(1,i) = l1*cos(theta1) + l2*cos(theta1 + theta2) .....
    J_tip(2,i) = temp;
    temp = 0;
    
    % z component is zero %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
    
    c=c+1;

end

end
