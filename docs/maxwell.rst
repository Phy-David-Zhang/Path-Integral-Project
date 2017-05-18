Maxwell’s Equations
-------------------

This is only a summary of the Maxwell’s equations under the language of Differential Geometry. There is no intention to introduce in detail — you are expected to cover them in your Electrodynamics courses.

First, we have the electromagnetic tensor :math:`F_{\mu\nu}` satisfying

.. math::


   E_i = F_{0i}, \ \ \ \ \ B_i = -\frac{1}{2}\varepsilon_{ijk}F^{jk}

The Maxwell’s equations can be expressed using :math:`F_{\mu\nu}` as

.. math::


   \partial^\mu &F_{\mu\nu} = 0\\
   \partial_{[\mu} &F_{\rho\sigma]} = 0

You can verify that the above equations indeed imply the ordinary form of Maxwell’s equation. The second equality should imply that the tensor :math:`F_{\mu\nu}` can be expressed as

.. math::


   F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu

where :math:`A_\mu` is a “vector” (dual vector or 1-form to be precise). It is easily identified that :math:`A_\mu` represents the electromagnetic potential. With the above construction, the second equation of the Maxwell’s equations automatically holds, and hence the Maxwell’s equations is reduced to

.. math::


   \partial^\mu F_{\mu\nu} = 0

It is easily verified that the Lagrangian of the electromagnetic field is

.. math::


   \mathcal{L} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu}

If you find any of the above content unfamiliar, please find and review a textbook about Electrodynamics, and make sure you have fully understood all the contents before proceeding.

