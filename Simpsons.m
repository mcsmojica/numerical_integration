clear; close all; clc;

% this script calculates an approximation of the net signed area of the
% region bounded by the curve y = e^x and an interval [-2,2] over the x-axis

% limits of integration (a and b)
a = -2;
b = 2;

% number n of subintervals
n = 10;

area_approx = compute_Simpsons(a,b,n);
disp(strcat('Simpsons rule area approximation for f(x) = exp(x) over [', num2str(a), ',', num2str(b) ,'] with n=', num2str(n), ' subintervals: ', num2str(area_approx)) );

function simpsons_approx = compute_Simpsons(a,b,n)
    if mod(n,2)~=0
        disp('n must be even.');
        return
    end
    
    % width of the each subinterval
    delta_x = (b-a)/n;
    
    % vector containing the endpoints of each subinterval
    xi_arr = a:delta_x:b;
    
    % vector containing the multipliers for each y_i
    % this gives an array of length n+1 called coeff_arr such that
    % coeff_arr = [1 4 2 4 2 ... 2 4 1]
    coeff_arr = repmat([4 2],[1,n/2]);
    coeff_arr = [1 coeff_arr];
    coeff_arr(end) = 1;
    
    % compute the function value at every x_i
    fxi = exp(xi_arr);
    
    % get the weighted sum: f(x_0) + 4f(x_1) + 2f(x_2) + ... + 2f(x_{n-2}) +
    % 4f(x_{n-1}) + f(xn)
    weighted_sum = dot(coeff_arr,fxi);
    
    % compute area approximation: (delta_x/3) * (weighted sum of f(x_i)s)
    simpsons_approx = (delta_x/3)*weighted_sum;
end