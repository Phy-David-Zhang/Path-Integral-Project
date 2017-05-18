Correlation Function
--------------------

In both stage 2 and stage 3, we will encounter the following functional derivative

.. math::


   \tau(x_1,\ldots,x_n) := \left.\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J(x_1)}\cdots\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J(x_n)}W_0[J]\right|_{J=0}

Thus, we give this quantity a name **correlation function**, or :math:`n`\ **-point (Green's) function**. The origin of this name comes from the similarity of its formulation in canonical quantization and hence this name may look strange here.

It is not so straight-forward about the :math:`n`-point function, and thus we hope to reduce the formula. To do this, let us first evaluate the 2-point function

.. math::


   \tau(x_1,x_2) &= \left.\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J(x_1)}\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J(x_2)}\exp\{-\frac{1}{2}\mathrm i\!\!\int\!\! J\Delta_FJ\}\right|_{J=0} \\
   &= \left.\mathrm{i}\frac{\delta}{\delta J(x_1)}\int\!\!\Delta_F(x_2;)J\exp\{-\frac{1}{2}\mathrm i\!\!\int \!\!J\Delta_FJ\}\right|_{J=0}\\
   &=\left.\mathrm i\Delta_F(x_1;x_2)W_0[J]\right|_{J=0} + \left.(\int\Delta_F J)^2W_0[J]\right|_{J=0} = \mathrm i\Delta_F(x_1;x_2)

It is nothing other than :math:`\mathrm{i}` times the ordinary Green's function. Next, 3-point function

.. math::


   \tau(x_1,x_2,x_3)\sim \left.\Delta_F\int\Delta_FJ\right|_{J=0} + \left.(\int\Delta_FJ)^3\right|_{J=0} = 0

And 4-point function

.. math::


   \tau(x_1,x_2.x_3,x_4) &= \mathrm{i}\Delta_F(x_1;x_2)\mathrm{i}\Delta_F(x_3;x_4)\\
   &+ \mathrm{i}\Delta_F(x_1;x_3)\mathrm{i}\Delta_F(x_2;x_4) \\
   &+ \mathrm{i}\Delta_F(x_2;x_3)\mathrm{i}\Delta_F(x_1;x_4)\\
   &= (1\sim2)(3\sim4) + (1\sim3)(2\sim4) + (2\sim3)(1\sim4)

where we have used :math:`(1\sim2)` to represent :math:`\tau(x_1,x_2)`. Therefore, we can see the regularity --- the :math:`n`-point function is either :math:`0` or some combination of two point functions. Specifically, we have by induction

-  The odd-point function is :math:`0`.
-  The even-point function is

.. math::


   \tau(x_1,\ldots, x_{2n}) = \sum_{\text{perms}}(p_1\sim p_2)\ldots(p_{2n-1}\sim p_{2n})

which means the summation over all the permutations :math:`p`. This is the so-called **Wick's Theorem** --- transforming the :math:`n`-point function into the combination of 2-point function.

You are suggested to show yourself that the S-matrix can be written using correlation function as

.. math::


   S = \sum_{n=0}^\infty\frac{\mathrm i^n}{n!}\prod_x\varphi(x)\prod_x(\partial^2\!\!-\!m^2)\tau(x_1,\ldots,x_n)

where :math:`x` takes over :math:`x_1,\ldots,x_n`. This formula is the so-called **perturbative expansion** of the S-matrix.

