import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

N = 100
dt = 5
t = np.arange(N) * dt

j = cp.Variable((N-1, 2))
a = cp.Variable((N, 2))
v = cp.Variable((N, 2))
s = cp.Variable((N, 2))

con = []
con += [a[0, :] == np.array([0, 0])]
con += [v[0, :] == np.array([100, 400])]
con += [s[0, :] == np.array([20000, 50000])]
con += [a[N-1, :] == np.array([0, 9.81])]
con += [v[N-1, :] == np.array([0, 0])]
con += [s[N-1, :] == np.array([0, 0])]

for i in range(1, N):
    con += [a[i, :] == a[i-1, :] + j[i-1, :] * dt]
    g = np.array([0, -9.81])
    f = -v[i-1, :] * 0.002# * cp.norm(v[i-1, :])
    con += [v[i, :] == v[i-1, :] + (a[i-1, :] + g + f) * dt]
    con += [s[i, :] == s[i-1, :] + v[i-1, :] * dt]
    # con += [a[i] <= 1]
    # con += [cp.norm(v[i, :]) <= 10]
    con += [cp.norm(j[i-1, :]) <= 10]
    if dt * (N - i) <= 10:
        con += [cp.norm(v[i, 0]) <= 0.1]

obj = cp.Minimize(cp.sum_squares(a))
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

    fig = plt.figure()
    plt.plot(s.value[:, 0], s.value[:, 1])
    plt.grid(True)
    plt.axis('equal')

    plt.show()
else:
    print('No solution')
