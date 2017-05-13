Evaluation of Path Integral
---------------------------

This section will tell you how to explicitly calculate the propagator using path integral. Take the free particle for example (you should try to generalise the calculation into other situations). The propagator of the free particle is

.. math::


   K = \lim_{n\rightarrow\infty}\int C(\epsilon)\prod_{i=1}^{n}\mathrm{d}[x(t_i)]\exp\{\mathrm{i}\sum_{i=1}^{n+1}\frac{1}{2}m\frac{[x(t_i)-x(t_{i-1})]^2}{\epsilon}\} 

To simplify the expression, denote :math:`x_i\equiv x(t_i)` and let :math:`m=2`. As a result, the integral simplifies to

.. math::


   K = \lim_{n\rightarrow\infty}\int C(\epsilon)\prod_{i=1}^{n}\mathrm{d}x_i\exp\{\mathrm{i}\sum_{i=1}^{n+1}\frac{(x_i-x_{i-1})^2}{\epsilon}\} 

Before trying to actually evaluate the above expression, we should first find out the normalisation factor :math:`C(\epsilon)`.

Determination of Normalisation Factor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The normalisation factor can be constrained under the infinitesimal evolvement. Suppose we now work on the interval :math:`(t, t+\epsilon)` where :math:`\epsilon` is an infinitesimal time step. Therefore, the normalisation condition requires

.. math::


   K(t; t+\epsilon) = \int c\,\mathrm{d}y \exp\{-\frac{(y-x)^2}{\mathrm{i}\epsilon}\} = 1

where :math:`y` is the position at :math:`t+\epsilon` and :math:`x` is the position at :math:`t`. Perform the integration and we get

.. math::


   c\cdot \sqrt{\mathrm{i}\pi\epsilon} = 1 \ \ \Rightarrow\ \ c = \frac{1}{\sqrt{\mathrm{i}\pi\epsilon}}

This normalisation factor emerges whenever we the time moves forward the amount :math:`\epsilon`. In our previous expression, we insert :math:`n` point into the interval :math:`(t,t')` which means we move forward :math:`n+1` steps. Therefore

.. math::


   C(\epsilon) = c^{n+1} = (\sqrt{\mathrm{i}\pi\epsilon})^{-n-1}

The normalisation factor of the other forms of Lagrangian can be derived through a similar way.

Expand according to Classical Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually, the path integral will have an upper and lower boundary, i.e. :math:`x'` and :math:`x_0`, which brings some trouble during the evaluation. Hence, we want to eliminate this trouble. The best way is to introduce a *relative* variable, i.e. select a certain path :math:`x_c` with :math:`x_c(t_0) = x_0` and :math:`x_c(t') = x'` and perform the path integral according to :math:`y\equiv x - x_c`. Of course, you can choose whatever path :math:`x_c` you like, but there is one path that will make the evaluation less miserable --- the classical path.

According to the variation principle, the classical path is defined as the path which satisfies

.. math::


   \left.\frac{\delta S}{\delta x}\right|_{x=x_c} = 0

Expand the action according to the classical path and we get

.. math::


   S = S_c + \left.\frac{\delta S}{\delta x}\right|_{x=x_c} y + \left.\frac{\delta^2 S}{\delta x^2}\right|_{x=x_c}y^2

This is nothing but a functional version of Taylor expansion. The expansion ends at second order since for most systems, the Lagrangian is quadratic. It is clear that the second term is zero. For the third term, it is exactly the same as :math:`S_c` for free particle situation. Therefore, we separate the action into the addition of a classical action and an action of :math:`y` which satisfies :math:`y_0 = y' = 0`.

.. note:: The above derivation will invoke functional Taylor expansion. If you can not yet accept this, it won't be miserable just to substitute :math:`x = x_c + y` into the original path integral and get the same result.

Evaluation by Quadratic Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our path integral now becomes

.. math::


   K = K_c \cdot \lim_{n\rightarrow\infty}\int (\sqrt{\mathrm{i}\pi\epsilon})^{-n-1}\prod_{i=1}^{n}\mathrm{d}y_i\exp\{\mathrm{i}\sum_{i=1}^{n+1}\frac{(y_i-y_{i-1})^2}{\epsilon}\} 

where

.. math::


   K_c = \exp\{\mathrm{i}S_c\}

is the "classical" part of the propagator.

A naive way of evaluating this integral is to follow the definition --- perform :math:`n` integration and then take the limit. However, recall that most of the physical models, the Lagrangian is quadratic. This provides another way of evaluating the path integral, which brings much ease.

To begin with, expand the summation

.. math::


   &y_1^2 + y_1^2 - 2y_1y_2 + y_2^2 + y_2^2 - 2y_2 y_3 + y_3^2 + ...\\
   =\ &2y_1^2 - y_1y_2 - y_1y_2 + 2y_2^2 - 2y_2 y_3 - 2y_2 y_3 + ...

The reason for a rearrangement of the terms can be seen if we write the expansion in matrix form

.. math::


   [y_1\ y_2\ y_3 \ldots y_n]
   \left[
   \begin{matrix}
   2 & -1 &  &  & & \\
   -1 & 2 & -1 &  & & \\
   & -1 & 2 & & & \\
   & & & \ddots & & \\
   & & & & & -1\\
   & & & & -1 & 2
   \end{matrix}
   \right]
   \left[
   \begin{matrix}
   y_1\\
   y_2\\
   y_3\\
   \vdots\\
   y_n\\
   \end{matrix}
   \right]
   \equiv \eta^T M \eta

where :math:`\eta` is an :math:`n`-dim vector and :math:`M` is the matrix in the middle. Therefore, the integral becomes

.. math::


   \lim_{n\rightarrow\infty}(\sqrt{\mathrm{i}\pi\epsilon})^{-n-1}\int \mathrm{d}\eta\exp\{-\eta^T A \eta\} 

where :math:`\mathrm d\eta` is just the abbreviation of :math:`\prod\mathrm dy` and :math:`A\equiv M/\mathrm i\epsilon`.

.. note:: It is a fairly common thing to transform something with multiple summation into the matrix form. You are suggested to have the vigilance about the summation which is possible to be transformed to matrix form since it may bring surprising extra clearance.

The integral is nothing other than a multi-dimensional Gaussian integral. We will directly invoke the result of the integral as there have been numerous materials on how to do the multi-dimensional Gaussian integral online. The result is

.. math::


   \int \mathrm{d}\eta\exp\{-\eta^T A \eta\} = \sqrt{\frac{\pi^n}{\det(A)_n}}

This inspires us to calculate the determinant of the matrix :math:`M` (and thus matrix :math:`A`). To do this, expand the determinant along the first row and we get the following recurrence relation

.. math::


   \det(M)_{n+1} = 2\det(M)_n - \det(M)_{n-1}

It is easy to see that this recurrence relation implies that the sequence :math:`\det(M)_n` is actually a arithmetic sequence. Therefore, an evaluation of the first two elements of the sequence will bring you

.. math::


   \det(M)_n = n+1

Thus

.. math::


   \det(A)_n = \det(M/\mathrm i\epsilon)_n = (n+1)/(\mathrm i\epsilon)^n

with which the integral is evaluated

.. math::


   \int \mathrm{d}\eta\exp\{-\eta^T A \eta\} = \sqrt{\frac{(\mathrm i\epsilon\pi)^n}{n+1}}

Combine with the other factors and we have

.. math::


   K = K_c\cdot\lim_{n\rightarrow\infty}(\sqrt{\mathrm{i}\pi\epsilon})^{-n-1}\sqrt{\frac{(\mathrm i\epsilon\pi)^n}{n+1}} = K_c\cdot\lim_{n\rightarrow\infty}\sqrt{\frac{1}{\mathrm i\pi\epsilon(n+1)}} 

Now, an important thing to notice is that :math:`\epsilon(n+1)` is actually :math:`\Delta t = t'-t_0`. Thus, we have the final formula of the propagator

.. math::


   K = \frac{1}{\sqrt{\mathrm i\pi\Delta t}}\exp\{\mathrm iS_c\}

You are suggested to explicitly calculate the classical action :math:`S_c` (notice that the classical path of a free particle is just a straight line) and compare this result with the one you may encounter in your previous Quantum Mechanics course.

Originally, we stop here. However, you might be pretty surprised about our later contexts if we do so. Hence, ... we decide to surprise you now.

    The modern path integral formalism of quantum theory has NOTHING to do with doing the path integral.

Yes, this is true and IMPORTANT. To make this less surprising, recall that we do not do the actual integral of the action in the Lagrangian formalism. Instead, we try to **transform the integration problem into differentiation problem**. So the existence of this section is nothing but to convince you that the integral truly exists and is well-defined.

Please do not feel to be cheated. Whenever you feel doubtful about our following derivation about the path integral, please remember to come here again to gain some confidence.

