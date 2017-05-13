Path Integral and Propagator
----------------------------

.. note:: This section requires knowledge on Green's function. Although we will briefly review some basics, you are still suggested to pick up a textbook on Mathematical Methods of Physics for a careful review.

In this section, you will make your first acquaintance with path integral. In quantum theory, path integral is a method of constructing the **propagator**. So we begin with the propagator.

Schrödinger’s Equation and Propagator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning:: The symbols invoked in this section (e.g. :math:`\psi`) have a dedicated meaning, which will be different from other sections in this project.

First, we need to recall **Green's function**. Mathematically, Green's function :math:`G(x;x')` of an operator :math:`L` is defined as

.. math::


   LG(x;x') = \delta(x;x')

This method is very useful to solve equations like

.. math::


   L\varphi(x) = J(x)

since if we know the Green's function :math:`G(x;x')` of :math:`L`, the solution is simply

.. math::


   \varphi(x) = \int G(x;x') J(x')\,\mathrm{d}x'

One can easily verify if notice

.. math::


   L\varphi(x) &= L\int G(x;x') J(x')\,\mathrm{d}x' \\
   &= \int LG(x;x') J(x')\,\mathrm{d}x' = \int \delta(x;x') J(x')\,\mathrm{d}x' = J(x)

where the second equality is due to the fact that :math:`L` consists only operation on :math:`x` and is totally irrelevant to :math:`x'`.

In Quantum Mechanics, we have the Schrödinger’s equation

.. math::


   \left[\mathrm{i}\frac{\partial}{\partial t} + \frac{1}{2m}\nabla^2\right]|\psi\rangle = 0

All within the bracket can be viewed as an operator, and thus possesses a Green's function

.. math::


   \left[\mathrm{i}\frac{\partial}{\partial t} + \frac{1}{2m}\nabla^2\right]K(t,x;t',x') = \delta(x;x')\delta(t;t')

With this propagator, we can calculate the state of anytime after from an initial state

.. math::


   |\psi(t')\rangle = \int K(x,t;x',t')|\psi(t)\rangle\mathrm{d}x\mathrm{d}t

Therefore, the initial state :math:`|\psi(t)\rangle` *propagates* to the final state :math:`|\psi(t')\rangle` with the help of :math:`K(x,t;x',t')`. As a consequence, :math:`K(x,t;x',t')` is called the **propagator**.

Path Integral
~~~~~~~~~~~~~

The previous argument is only one way to construct Quantum Mechanics, i.e. suppose the Schrödinger equation holds -> derivation of the propagator. In 1948, Feynman proposed another way of reasoning: path integral -> propagator -> Schrödinger equation.

Feynman suggest the propagator takes the form

.. math::


   K = \int \mathcal{D}x \exp\{\mathrm{i}S[x]\}

.. note:: Rigorously speaking, we should use :math:`\propto` instead of :math:`=` in the above equation, since the RHS may produce annoying constant factors. However, this factor can be eliminated through normalisation. Therefore, all the subsequent path integral will automatically carry this normalisation process.

where :math:`S[x]` is the action of the system, and :math:`\int\mathcal{D}x` is the so-called path integral. Next, we carefully examine the above equation.

Take 1D free particle for example. The Lagrangian of 1D free particle is

.. math::


   L = \frac{1}{2}m\dot{x}^2

Thus, the action is

.. math::


   S[x] = \int\mathrm{d}t\,\frac{1}{2}m\dot{x}^2

Suppose we now work on the start point :math:`x, t` and end point :math:`x', t'`. The path integral requires "integrating along all paths". However, the "all path" can be hard to manipulate, since it is something uncountable. More specifically, it should be something like

.. math::


   \int [...]\mathrm{d}[x(t_1)]\int [...]\mathrm{d}[x(t_2)]\int [...]\mathrm{d}[x(t_3)]...

where every point within interval :math:`(t,t')` needs an integration. This is clearly impossible since there are uncountable elements within :math:`(t,t')`. Hence, we come up with the idea of a kind of "sampling".

For an arbitrary large number (:math:`n`) of points within :math:`(t,t')` (the "sample" of :math:`n` points), the following formula

.. math::


   \int [...]\mathrm{d}[x(t_1)] \int [...]\mathrm{d}[x(t_2)] ... \int [...]\mathrm{d}[x(t_n)]

exists, we *define* this result as the integration of all path, i.e. the path integral of :math:`[...]`. The fact that the size of the "sample" can be *arbitrarily* large insures that the integral actually goes over *every path*.

.. note:: The trick to turn some infinite objects to something arbitrary can be very common in Mathematics. For instance, the concept *infinitely large* can be in fact *arbitrarily large* or *no upper bound*. The limit in Mathematics also follows similar idea.

To formally implement this, insert :math:`n` points into :math:`(t,t')` and perform :math:`n` integrations

.. math::


   \prod_{i=1}^{n}\int\exp\{\mathrm{i}\frac{1}{2}m\frac{[x(t_i)-x(t_{i-1})]^2}{\epsilon}\}\mathrm{d}[x(t_i)]

where we also expand the integration in the action into discrete form, and :math:`\epsilon = (t'-t)/(n+1)` is the size of each small interval. Then, ask the "sample size" :math:`n` to go to infinity

.. math::


   \lim_{n\rightarrow\infty}\int C(\epsilon)\prod_{i=1}^{n}\mathrm{d}[x(t_i)]\exp\{\mathrm{i}\sum_{i=1}^{n+1}\frac{1}{2}m\frac{[x(t_i)-x(t_{i-1})]^2}{\epsilon}\}

where we also adjust the order and introduce a normalisation factor :math:`C(\epsilon)` to ensure the convergence. You should be able to prove this adjustment once notice that all :math:`x(t_i)` are independent variables. The above formula is the definition of the path integral

.. math::


   \int\mathcal{D}x\exp\{\mathrm{i}\int\mathrm{d}t\frac{1}{2}m\dot{x}\}

As a practice, you should try to write down the definition of a general path integral

.. math::


   \int\mathcal{D}x\exp\{\mathrm{i}\int\mathrm{d}t L\}

You may find the above elucidation hard to comprehend. That's normal. Try to draw some diagrams or analyse step by step. It might help.

