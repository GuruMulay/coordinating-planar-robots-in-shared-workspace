clc;
clear all;
cd('.')
% cd('~/proj/csu_courses_git/ece555/coordinating-planar-robots-in-shared-workspace')
%%%%% IMPORTANT: !!!Change the directory suitably!!! %%%%%

r1 = importdata('r1.txt');
r2 = importdata('r2.txt');

z1 = zeros(size(r1,1),1);
r1 = [r1';z1']';

z2 = zeros(size(r2,1),1);
r2 = [r2';z2']';

R1 = [1 0 0; 0 -1 0; 0 0 -1];
R2 = [1 0 0; 0 -1 0; 0 0 -1];
Pt1 = [0 -300 0];
Pt2 = [500 -300 0];
T1 = [1 0 0 0; 0 -1 0 300; 0 0 -1 0; 0 0 0 1];

p0 =  [250; 300; 0]; %[600; 600; 0]%[500; 300; 0] %[200; 300; 0]

c1 = r1*R1;
c2 = r2*R2;

p1(:,1) =  c1(:,1)- Pt1(1,1);
p1(:,2) =  c1(:,2)- Pt1(1,2);
p1(:,3) =  c1(:,3)- Pt1(1,3);
 
p2(:,1) =  c2(:,1)- Pt2(1,1);
p2(:,2) =  c2(:,2)- Pt2(1,2);
p2(:,3) =  c2(:,3)- Pt2(1,3);

% dlmwrite('r1_rotated',p1(:,1:2),'-append','delimiter','\t', 'precision', 10)
% dlmwrite('r2_rotated',p2(:,1:2),'-append','delimiter','\t', 'precision', 10)

B1 = p1(:,1:2)
B2 = p2(:,1:2)

B = B1

A = importdata('arm_r1');
s = size(A);
n = A(1,1) % number of joints in the robot 
lambda = A(1,2) % damped least squares parameter
arm = A(2:end,1:end);

%%B = importdata('r1_rotated');
s = size(B);
m = s(1) - 1
%%m = B(1,1) % number of desired positions of end-effector tooltip
%lambda = B(1,2) % damped least squares parameter
%%trajectory = B(2:end,1:end);
trajectory = B(1:end,1:end);
xd = trajectory(1:end,1); %desired x
yd = trajectory(1:end,2); %desired y

l = arm(1:n,1) %generalized for n and not the length of data points
theta0 = arm(1:n,2)

[xa, ya] = forward_kinematic(theta0, l, n) %actual x and y
xa
ya

c = 0
theta = theta0
file = fopen('angles_r1','wt');

for i = 0: m  %7  %m
    i
    theta_dot = ones(n,1); % intialize to finite value > epsilon at every pt. in trajectory ('while' condition)
    X_dot = ones(size(trajectory,2),1); % initialize to non-zero fininte value > epsilon
    
    %while((100000*xa ~= 100000*xd(i+1,1) | 100000*ya ~= 100000*yd(i+1,1)) & c < 10 )
    while(sum(abs(theta_dot) >= 0.000001) & c < 20000) % sum(abs(X_dot) >= 0.000001) 
        % sum -> to make sure EVERY theta_dot is less than epsilon | c -> limit to avoid infinite loop
        c = c + 1; %It doesn't go in infinite loop, but for infinitesimally small epsilon (theta_dot) code might go in infinite loop; hence limited by c.
        
        deltax = xd(i+1,1) - xa;
        deltay = yd(i+1,1) - ya;
        X_dot = [deltax; deltay];
        J_tip = jacobian(theta, l, n); 
        
        %DLS Logic with Faster DLS Inverse -->
        theta_dot = J_tip.'*inv(J_tip*J_tip.' + lambda*lambda*eye(size(J_tip,1)))*X_dot;
        %theta_dot = inv(J_tip.'*J_tip + lambda*lambda*eye(size(J_tip,2)))*J_tip.'*X_dot %Slower Inverse
        
        theta_d = theta + theta_dot;
        [xa, ya] = forward_kinematic(theta_d, l, n);
        theta = theta + theta_dot; %update theta
        %pause
    end
    
    %write the number of iterations it took to converge for every angle-set
%     dlmwrite('c_iterations',c','-append','delimiter','\t', 'precision', 10)
    c = 0
    disp(i)
    
    %%%%%%%%%%%%%%%%%%%%% Write Outputs %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    print = sprintf('Write File ------- m = %d', i)
    theta
    
    dlmwrite('angles_r1',theta','-append','delimiter','\t', 'precision', 10)
    xa;
    ya;
    XY = [xa ; ya]
    %dlmwrite('XY',XY','-append','delimiter','\t', 'precision', 10)
    print = sprintf('----------------- m = %d', i)
end
i
lambda

%%%%%%%%%%%%%% Plot theangles, trajectory for the arm-joints %%%%%%%%%%%%%
%check_angles
