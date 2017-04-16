Solution of Klein-Gordon Equation
---------------------------------

.. note:: This section is important to the canonical quantisation method, and will not influence the overall logic. You may skip this if you wish.

In this section, we look at the general solution of the Klein-Gordon equation. We do this for :math:`\varphi`, and similar procedure can be easily carried out for :math:`\varphi^*`.

For any possible field :math:`\varphi`, we can perform Fourier expansion as

.. math::


   \varphi = \int{\mathrm d^4k\over(2\pi)^4}a(k)\exp\{-\mathrm i k^\mu x_\mu\}

.. note:: Well, you may notice that here we do not take the symmetric form of the Fourier transformation. Although personally I prefer the symmetric form, but trust me, it can make all the successive discussions awful.

Take the above expression back into the equation, we get the dispersion relation

.. math::


   k^2 + m^2 = 0

This relation serves as a constraint to the wave number :math:`k^\mu`. Thus, to gain the solution, all we need to do is to switch the integral measure to `delta measure <@waiting>`__

.. math::


   \varphi(x) = \int{\mathrm d^4k\over(2\pi)^4}a(k)\exp\{-\mathrm i k^\mu x_\mu\}\cdot2\pi\delta(k^2+m^2)

Factor :math:`2\pi` is necessary since we are going to perform the integral once, like

.. math::


   \varphi(x) &= \int{\mathrm d\omega \mathrm d^3k\over(2\pi)^4}a(k)\exp\{-\mathrm i k^\mu x_\mu\}\cdot2\pi\delta(-\omega^2 + \vec k^2 + m^2)\\
   &= \int{\mathrm d\omega^2 \mathrm d^3k\over2\omega(2\pi)^3}a(k)\exp\{-\mathrm i k^\mu x_\mu\}\cdot\delta(-\omega^2 + \vec k^2 + m^2)\\
   &= \int{\mathrm d^3k\over2\omega_k(2\pi)^3}a(k)\exp\{\mathrm i(\omega_k t - \vec k \vec x\} + \int{\mathrm d^3k\over(-2\omega_k)(2\pi)^3}a(k)\exp\{\mathrm i(-\omega_k t - \vec k \vec x\}\\
   &= \int{\mathrm d^3k\over2\omega_k(2\pi)^3}a(k)\exp\{\mathrm i(\omega_k t - \vec k \vec x\} + \int{\mathrm d^3k\over(2\omega_k)(2\pi)^3}a(-k)\exp\{\mathrm i(-\omega_k t + \vec k \vec x\}\\
   &= \int{\mathrm d^3k\over2\omega_k(2\pi)^3}\left[a(k)\exp\{-\mathrm i(k^\mu x_\mu\} + a(-k)\exp\{\mathrm i(k^\mu x_\mu\} \right]

where :math:`\omega_k = \sqrt{\vec k^2 + m^2}`. The fourth equality is nothing other than reversing the direction of :math:`\vec k`. Hence, we get the general form of the solution of Klein-Gordon equation.

