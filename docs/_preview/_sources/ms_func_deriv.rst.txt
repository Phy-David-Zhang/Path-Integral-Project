Functional Derivative
---------------------

The functional derivative we talk about here is not the same as the variation used widely in Lagrangian formalism --- although they look so much alike formally. To make sure you will not mistake them, we first illustrate what is the variation of a functional.

The variation of a functional :math:`F[\phi]` whose domain is a Banach space :math:`B` (a linear space where you can talk about the "length" --- norm of its element) is usually implemented as **Gâteaux derivative**

.. math::


   \frac{\delta F[\phi]}{\delta\phi} := (\forall \eta) :: \lim_{\varepsilon\rightarrow 0}\frac{F[\phi+\varepsilon\eta]-F[\phi]}{\varepsilon}

which very much resembles the directional derivative in ordinary Calculus. Please notice that the :math:`\eta` here is just an arbitrary element of the Banach space, and in its application it is any physical field.

The variation is the "derivative" of the argument :math:`\phi` itself, without any designation of it value at some point :math:`\phi(x)`; while functional derivative is defined differently. The functional derivative of :math:`F[\phi(x)]` with respect to **value** :math:`\phi(y)` is

.. math::


   \frac{\delta F[\phi(x)]}{\delta\phi(y)} = \lim_{\varepsilon\rightarrow 0}\frac{F[\phi(x)+\varepsilon\delta(x;y)]-F[\phi(x)]}{\varepsilon}

Therefore, you shall now see the differences between the variation and the functional derivative --- the variation performs "derivative" on :math:`\phi` itself, while the functional derivative does so on the value :math:`\phi(y)`. And thus a delta function has to be invoked to deal with the different points :math:`x` and :math:`y`. You will see in chapter Quantum Theory that it is this delta function which brings the infinities into the S-matrix.

