Free Scalar Field Theory
------------------------

This section will introduce the free scalar field theory, i.e. stage 1 mentioned in the sketch. Our main goal here is to derive the generating functional of the free scalar field.

First we need a vacuum state as the initial and final state --- just like the start and end point in path integral of Quantum Mechanics. However, the vacuum is not so straight-forward in Quantum Field Theory. We hereby *define* the vacuum state :math:`|\Omega\rangle` as the configuration of field with the lowest possible energy, which is the general starting point of the term *vacuum*.

.. note:: In canonical quantization, there is an annihilation operator :math:`a` and thus the vacuum state can be defined as :math:`a|\Omega\rangle=0`. However, now we do not have any operators. Therefore, we *define* the state using the property it needs to satisfy.

Now, we express the probability of the free field from vacuum state to vacuum state in terms of path integral. The probability should be unity since there are no interactions. Therefore

.. math::


   W = \langle\Omega|\Omega\rangle = \mathcal{N}\int\mathcal{D}\varphi\exp\{-\frac{1}{2}\mathrm{i}\int\varphi(\partial^2\!\!-\!m^2)\varphi\} = 1

where we now know the normalization factor :math:`\mathcal{N}`. We hope that you still remember the Lagrangian for scalar field (If you don't, go and review `this <./clstheo_scalar.html>`__). The scalar field is real here, and it won't be miserable to generalize this into complex situation.

This formulation does not tell us anything except for a normalization factor, since it is trivial --- from vacuum to vacuum with no interaction. Now, we want to add some interactions. To achieve this, we introduce an auxiliary potential :math:`J` and the Lagrangian becomes

.. math::


   \mathcal{L} = -\varphi(\partial^2\!\!-\!m^2)\varphi + J\varphi

and the path integral becomes

.. math::


   W[J] = \langle\Omega|\Omega\rangle|_J = \mathcal{N}\int\mathcal{D}\varphi\exp\{-\frac{1}{2}\mathrm{i}\int\varphi(\partial^2\!\!-\!m^2)\varphi-2J\varphi\}

Now, we perform the path integral. As what we have done in Quantum Mechanics, expand the path integral according to the classical path. The classical path :math:`\varphi_0` satisfies

.. math::


   (\partial^2\!\!-\!m^2)\varphi_0 = J,\ \ \text{i.e.}\ \ \varphi_0 = \int \Delta_F J

where :math:`\Delta_F` is the Green's function satisfying

.. math::


   (\partial^2\!\!-\!m^2)\Delta_F(x;x') = -\delta(x;x')

.. warning:: Please be very careful about the minus sign in the right hand side of the above equation!

Consequently, we perform translation :math:`\varphi\mapsto\varphi + \varphi_0`. In path integral, a definite path :math:`\varphi_0` acts just like a constant (expand the path integral according to the definition and you will see why). A brief calculation will give

.. math::


   W[J] &= \exp\{-\frac{1}{2}\mathrm{i}\int J\Delta_F J\}\cdot \mathcal{N}\int\mathcal{D}\varphi\exp\{-\frac{1}{2}\mathrm{i}\int\varphi(\partial^2\!\!-\!m^2)\varphi\}\\
   &= \exp\{-\frac{1}{2}\mathrm{i}\int J\Delta_F J\}

Since this is the case of free field, we rewrite the conclusion as

.. math::


   W_0[J] = \exp\{-\frac{1}{2}\mathrm{i}\int J\Delta_F J\}

which is the desired result as it is in the sketch.

.. note:: In the following context, the generating functional is always assumed to be normalised, and we will neglect the normalization factor.

