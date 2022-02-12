import cvxpy as cp
import matplotlib.pyplot as plt
import numpy as np
import time

N = 50
MAX_ITER = 10
# t = np.arange(N) * dt

j = cp.Variable(N-1)
a = cp.Variable(N)
v = cp.Variable(N)
s = cp.Variable(N)
dt = cp.Variable(1)

res_j = np.zeros((1, N-1))
res_a = np.zeros((1, N))
res_v = np.zeros((1, N))
res_s = np.zeros((1, N))
res_dt = np.zeros((1, 1)) + 1
time_cost = []

t1 = time.time()

for iter_i in range(0, MAX_ITER):
    # print(iter_i)

    con_temp = []
    con_temp += [a[0] == 0]
    con_temp += [v[0] == 0]
    con_temp += [s[0] == 0]
    con_temp += [a[-1] == 0]
    con_temp += [v[-1] == 0]
    con_temp += [s[-1] == 50]

    for i in range(1, N):
        con_temp += [a[i] == a[i-1] + res_dt[iter_i, 0] * j[i-1] + res_j[iter_i, i-1] * (dt[0] - res_dt[iter_i, 0])]
        con_temp += [v[i] == v[i-1] + res_dt[iter_i, 0] * a[i-1] + res_a[iter_i, i-1] * (dt[0] - res_dt[iter_i, 0])]
        con_temp += [s[i] == s[i-1] + res_dt[iter_i, 0] * v[i-1] + res_v[iter_i, i-1] * (dt[0] - res_dt[iter_i, 0])]
        # con_temp += [a[i] <= 1]
        con_temp += [dt[0] >= 0.01]
        con_temp += [j[i-1] <= 10]
        con_temp += [j[i-1] >= -10]
        con_temp += [v[i] >= 0]
        con_temp += [v[i] <= 10]
    
    con = con_temp

    obj_sq = cp.sum_squares(dt)
    # obj_sq += cp.sum_squares(j - res_j[iter_i, :])
    # obj_sq += cp.sum_squares(a - res_a[iter_i, :])
    # obj_sq += cp.sum_squares(v - res_v[iter_i, :])
    obj_sq += cp.sum_squares(dt - res_dt[iter_i, :]) * 1
    obj = cp.Minimize(obj_sq)
    # obj = cp.Minimize(cp.sum_squares(j))

    # if iter_i == 0:
    #     prob = cp.Problem(obj, con)
    #     result = prob.solve()
    # else:
    prob = cp.Problem(obj, con)
    result = prob.solve(eps_abs=1e-5, eps_rel=1e-5)
    # result = prob.solve(warm_start=True)

    res_j = np.concatenate((res_j, [j.value]), axis=0)
    res_a = np.concatenate((res_a, [a.value]), axis=0)
    res_v = np.concatenate((res_v, [v.value]), axis=0)
    res_dt = np.concatenate((res_dt, [dt.value]), axis=0)
    time_cost += [prob.solver_stats.solve_time]

print('dt = ' + str(dt.value))
print('Time cost = ' + str(time.time() - t1))
print(prob.solver_stats)

fig, axs = plt.subplots(6, 1, sharex=True)
axs[0].plot(j.value)
axs[0].set_ylabel('j (m/s^3)')
axs[0].grid(True)

axs[1].plot(a.value)
axs[1].set_ylabel('acc (m/s^2)')
axs[1].grid(True)

axs[2].plot(v.value)
axs[2].set_ylabel('vel (m/s)')
axs[2].grid(True)

axs[3].plot(s.value)
axs[3].set_xlabel('t (sec)')
axs[3].set_ylabel('s (m)')
axs[3].grid(True)

axs[4].plot(time_cost)
axs[4].grid(True)

axs[5].plot(res_dt)
axs[5].grid(True)

plt.show()
