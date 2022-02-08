import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

N = 100
dt = 0.1
t = np.arange(N) * dt

j = cp.Variable(N-1)
a = cp.Variable(N)
v = cp.Variable(N)
s = cp.Variable(N)

con = []
con += [a[0] == 0]
con += [v[0] == 0]
con += [s[0] == 0]
con += [a[N-1] == 0]
con += [v[N-1] == 0]
con += [s[N-1] == 50]

for i in range(1, N):
    con += [a[i] == a[i-1] + j[i-1] * dt]
    con += [v[i] == v[i-1] + a[i-1] * dt]
    con += [s[i] == s[i-1] + v[i-1] * dt]
    # con += [a[i] <= 1]
    con += [v[i] <= 10]

obj = cp.Minimize(cp.sum_squares(j))
prob = cp.Problem(obj, con)

result = prob.solve()

if prob.status == "optimal":
    fig, axs = plt.subplots(4, 1, sharex=True)
    axs[0].plot(t[0:N-1], j.value)
    axs[0].set_ylabel('j (m/s^3)')
    axs[0].grid(True)

    axs[1].plot(t, a.value)
    axs[1].set_ylabel('acc (m/s^2)')
    axs[1].grid(True)

    axs[2].plot(t, v.value)
    axs[2].set_ylabel('vel (m/s)')
    axs[2].grid(True)

    axs[3].plot(t, s.value)
    axs[3].set_xlabel('t (sec)')
    axs[3].set_ylabel('s (m)')
    axs[3].grid(True)

    plt.show()
else:
    print('No solution')
