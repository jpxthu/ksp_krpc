

$$
t = \sigma \tau
$$

$$
\cfrac{d\vec{X}}{d\tau} = \cfrac{d t}{d\tau} \cfrac{d\vec{X}}{d t} = \sigma \cfrac{d\vec{X}}{d t}
$$

$$
\cfrac{d}{dt}\bold{x} = f\left( \bold{x}(t), \bold{u}(t) \right)
$$

$$
\begin{aligned}
    \bold{x}'(\tau) &= \sigma f\left( \bold{x}(\tau), \bold{u}(\tau) \right) \\
    &\approx \hat{\sigma} f\left( \hat{\bold{x}}, \hat{\bold{u}} \right) +
        \hat{\sigma} \left. \cfrac{\partial f\left( \bold{x}, \bold{u} \right)}{\partial \bold{x}} \right|_{\hat{\bold{x}}, \hat{\bold{u}}} \left( \bold{x} - \hat{\bold{x}} \right) +
        \hat{\sigma} \left. \cfrac{\partial f\left( \bold{x}, \bold{u} \right)}{\partial \bold{u}} \right|_{\hat{\bold{x}}, \hat{\bold{u}}} \left( \bold{u} - \hat{\bold{u}} \right) +
        f\left( \hat{\bold{x}}, \hat{\bold{u}} \right) \left( \sigma - \hat{\sigma} \right) \\
    &= A(\tau)\bold{x}(\tau) + B(\tau)\bold{u}(\tau) + C(\tau)\sigma + D(\tau)
\end{aligned}
$$

$$
\begin{aligned}
    A(\tau) &\triangleq \hat{\sigma} \left. \cfrac{\partial f\left( \bold{x}, \bold{u} \right)}{\partial \bold{x}} \right|_{\hat{\bold{x}}(\tau), \hat{\bold{u}}(\tau)} \\
    B(\tau) &\triangleq \hat{\sigma} \left. \cfrac{\partial f\left( \bold{x}, \bold{u} \right)}{\partial \bold{u}} \right|_{\hat{\bold{x}}(\tau), \hat{\bold{u}}(\tau)} \\
    C(\tau) &\triangleq f\left( \hat{\bold{x}}(\tau), \hat{\bold{u}}(\tau) \right) \\
    D(\tau) &\triangleq - A(\tau)\hat{\bold{x}}(\tau) - B(\tau)\hat{\bold{u}}(\tau)
\end{aligned}
$$

Example:

$$
\bold{x}(t) = \begin{bmatrix}
    a \\ v \\ s
\end{bmatrix}, \bold{u}(t) = \begin{bmatrix}
    j
\end{bmatrix}
$$

$$
\bold{x}^{(i+1)} - \bold{x}^{(i)} = \begin{bmatrix}
    j\Delta t \\
    a\Delta t + \cfrac{1}{2}j\Delta t^2 \\
    v\Delta t + \cfrac{1}{2}a\Delta t^2 + \cfrac{1}{6}j\Delta t^3
\end{bmatrix} = \Delta t \begin{bmatrix}
    0 & 0 & 0 \\
    1 & 0 & 0 \\
    \cfrac{1}{2}\Delta t & 1 & 0
\end{bmatrix} \begin{bmatrix}
    a \\ v \\ s
\end{bmatrix} + \Delta t \begin{bmatrix}
    1 \\ \cfrac{1}{2}\Delta t \\ \cfrac{1}{6}\Delta t^2
\end{bmatrix} [j]
$$

$$
f(\bold{x}, \bold{u}) = \cfrac{d}{dt}\bold{x}(t) = \begin{bmatrix}
    j \\ a \\ v
\end{bmatrix}
$$

$$
\begin{aligned}
    A \triangleq& \hat{\sigma} \begin{bmatrix}
        0 & 0 & 0 \\
        1 & 0 & 0 \\
        0 & 1 & 0
    \end{bmatrix} \\
    B \triangleq& \hat{\sigma} \begin{bmatrix}
        1 \\ 0 \\ 0
    \end{bmatrix} \\
    C \triangleq& \begin{bmatrix}
        \hat{j} \\ \hat{a} \\ \hat{v}
    \end{bmatrix} \\
    D \triangleq& - A\bold{\hat{x}} - B\bold{\hat{u}}
\end{aligned}
$$

$$
\bold{x}^{(i+1)} - \bold{x}^{(i)} = A\bold{x} + B\bold{u} + C\sigma + D
$$

$$
\begin{bmatrix}
    \Delta a \\ \Delta v \\ \Delta s
\end{bmatrix} = \hat{\sigma} \begin{bmatrix}
    j \\ a \\ v
\end{bmatrix} + \begin{bmatrix}
    \hat{j} \\ \hat{a} \\ \hat{v}
\end{bmatrix} \sigma - \hat{\sigma} \begin{bmatrix}
    \hat{j} \\ \hat{a} \\ \hat{v}
\end{bmatrix}
$$
