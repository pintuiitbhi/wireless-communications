from sympy import fourier_series, pi, Piecewise
from sympy.abc import t
from sympy.plotting import plot

f = Piecewise((0, t < -pi), (0, t < 0), (t, t < pi), (0, True))
T = 2*pi

s = fourier_series(f, (t, -T/2, T/2))
F = s.truncate(5)
print(F)

n = [10, 50, 200]
p = plot(s.truncate(n[0]), (t, -10, 10), title="For 10 terms", line_color='firebrick', show=False)
p.xlabel = '$t$'
p.ylabel = '$F(t)$'
p.show()
p = plot(s.truncate(n[1]), (t, -10, 10), title="For 50 terms", line_color='darkblue', show=False)
p.xlabel = '$t$'
p.ylabel = '$F(t)$'
p.show()
p = plot(s.truncate(n[2]), (t, -10, 10), title="For 200 terms", line_color='green', show=False)
p.xlabel = '$t$'
p.ylabel = '$F(t)$'
p.show()