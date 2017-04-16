Classical Theory: Scalar Field
------------------------------

.. note:: This context will require knowledge on Lagrangian dynamics of fields. If you have not yet cover that in your previous learning, you will find `Lagrangian Form of Fields <@waiting>`__ helpful.

The Lagrangian of a scalar field is usually written as

.. math::


   \mathcal L = -\partial_\mu\varphi^*\partial^\mu\varphi - m^2\varphi^*\varphi

Alternatively, we can write

.. math::


   \mathcal L = \varphi^*(\partial^\mu\partial_\mu - m^2)\varphi

The equivalence between the two expression can be manifest once notice

.. math::


   \partial_\mu(\varphi^*\partial^\mu\varphi) = \varphi^*\partial^\mu\partial_\mu \varphi + \partial_\mu\varphi^*\partial^\mu\varphi = 0

The last equality is due to the fact that the left hand side is a surface term in the action integral.

Using the Lagrange equation, we get the equations of motion of scalar field

.. math::


   (\partial^\mu\partial_\mu - m^2)\varphi = 0\\
   (\partial^\mu\partial_\mu - m^2)\varphi^* = 0

This is the “real” **Klein-Gordon equation** — the equation of scalar field.

