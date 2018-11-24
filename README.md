# Cubic-C2-Splines
Calculates Cubic C2-Splines through 5 Points.

# Caveats:
<a href="https://www.codecogs.com/eqnedit.php?latex=x_0&space;&=&space;-2&space;\\&space;x_1&space;&=&space;-1&space;\\&space;x_2&space;&=&space;0&space;\\&space;x_3&space;&=&space;1&space;\\&space;x_4&space;&=&space;2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_0&space;&=&space;-2&space;\\&space;x_1&space;&=&space;-1&space;\\&space;x_2&space;&=&space;0&space;\\&space;x_3&space;&=&space;1&space;\\&space;x_4&space;&=&space;2" title="x_0 &= -2 \\ x_1 &= -1 \\ x_2 &= 0 \\ x_3 &= 1 \\ x_4 &= 2" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=y_0&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?y_0&space;=&space;0" title="y_0 = 0" /></a>

# Result
The Result are four Cubic Polynominals that satisfy

<a href="https://www.codecogs.com/eqnedit.php?latex=s_i(x_{i&plus;1})&space;=&space;y_{i&plus;1}&space;=&space;s_{i&plus;1}(x_{i&plus;1})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s_i(x_{i&plus;1})&space;=&space;y_{i&plus;1}&space;=&space;s_{i&plus;1}(x_{i&plus;1})" title="s_i(x_{i+1}) = y_{i+1} = s_{i+1}(x_{i+1})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=s'_i(x_{i&plus;1})&space;=&space;s'_{i&plus;1}(x_{i&plus;1})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s'_i(x_{i&plus;1})&space;=&space;s'_{i&plus;1}(x_{i&plus;1})" title="s'_i(x_{i+1}) = s'_{i+1}(x_{i+1})" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=s''_i(x_{i&plus;1})&space;=&space;s''_{i&plus;1}(x_{i&plus;1})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s''_i(x_{i&plus;1})&space;=&space;s''_{i&plus;1}(x_{i&plus;1})" title="s''_i(x_{i+1}) = s''_{i+1}(x_{i+1})" /></a>

and

<a href="https://www.codecogs.com/eqnedit.php?latex=s'(x_1)&space;=&space;s'(x_4)&space;=&space;0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s'(x_1)&space;=&space;s'(x_4)&space;=&space;0" title="s'(x_1) = s'(x_4) = 0" /></a>

# Output:
Should be self explanatory. Each Polynominal has the form
<a href="https://www.codecogs.com/eqnedit.php?latex=s_i(x)&space;=&space;\alpha_i&space;&plus;&space;\beta_i&space;(x-x_i)&space;&plus;&space;\gamma_i&space;(x-x_i)^2&space;&plus;&space;\delta_i&space;(x-x_i)^3" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s_i(x)&space;=&space;\alpha_i&space;&plus;&space;\beta_i&space;(x-x_i)&space;&plus;&space;\gamma_i&space;(x-x_i)^2&space;&plus;&space;\delta_i&space;(x-x_i)^3" title="s_i(x) = \alpha_i + \beta_i (x-x_i) + \gamma_i (x-x_i)^2 + \delta_i (x-x_i)^3" /></a>
