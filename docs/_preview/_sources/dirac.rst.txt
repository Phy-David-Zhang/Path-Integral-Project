Dirac Equation
--------------

.. note:: It is the time to invoke our `convention of indices <#>`__ here. In short, the Greek letter indices are the abstract or/and spacetime indices, Latin letter indices are specific, internal or ordinary indices.

Unlike to the Klein-Gordon equation, Dirac equation is an equation of spinor field. Under the requirement of Physics, the equation of spinor field should satisfy the following conditions
- It can imply Klein-Gordon equation
- It remains unchanged under the Lorentz transformation
The first requirement is due to the fact that the Klein-Gordon equation will imply the relativistic energy-momentum relation. Historically, Dirac put forward the equation under the consideration of performing the formal square root of the Klein-Gordon equation. The Dirac equation reads

.. math::


   \mathrm{i}\gamma^\mu\!\partial_\mu\psi - m\psi = 0

where :math:`\gamma_\mu = \gamma^a e_a^\mu` and :math:`e_a^\mu` is the tetrad. Next we briefly confirm that the equation does comply with the requirements.

It is easy to see that the first requirement is met once notice

.. math::


   (\mathrm{i}\gamma^\mu\!\partial_\mu + m)(\mathrm{i}\gamma^\nu\!\partial_\nu - m)\psi = -(\gamma^\mu\gamma^\nu\partial_\mu\partial_\nu + m^2)&\psi\\
   = (g^{\mu\nu}\partial_\mu\partial_\nu - m^2)\psi = (\partial^\mu\partial_\mu - m^2)&\psi = 0

The second condition requires

.. math::


   \mathrm{i}\gamma'^\mu\!\partial_\mu\psi' - m\psi' = 0

where :math:`\psi' = S\psi`, :math:`S` is the matrix of spinor representation of Lorentz transformation and :math:`\psi` satisfies the Dirac equation. This could be achieved if

.. math::


   S\gamma'^\mu S^{-1} = \gamma^\mu

We shall not prove the above identity but to provide a sketch of the proof. Since :math:`\gamma^\mu = \gamma^a e_a^\mu`, the above equation would require

.. math::


   S\gamma^a S^{-1} = \varLambda^a_b\gamma^b

This relation can be verified if take :math:`S` and :math:`\varLambda` to be infinitesimal transformation. And you will find the following trick useful

.. math::


   [A, BC] = \{A,B\}C - \{B, A\}C

Next, we construct the Lagrangian of the spinor field. An intuitive construction is just to multiply the Dirac equation by the Hermitian conjugate :math:`\psi^\dagger` of the spinor field

.. math::


   \mathcal{L}_{\text{tmp}} = -\psi^\dagger(\mathrm{i}\gamma^\mu\!\partial_\mu - m)\psi

However, this Lagrangian is not invariant under the Lorentz transformation, since

.. math::


   \mathcal{L'}_{\text{tmp}} = -\psi^\dagger [S^\dagger S](\mathrm{i}\gamma^\mu\!\partial_\mu - m)\psi

The representation :math:`S` is not necessarily unitary and thus :math:`S^\dagger S` is not necessarily identity. Therefore, we construct the Dirac conjugate of spinor field as

.. math::


   \bar{\psi} = \psi^\dagger\gamma^0

and construct the Lagrangian as

.. math::


   \mathcal{L} = -\bar{\psi}(\mathrm{i}\gamma^\mu\!\partial_\mu - m)\psi

Now you can verify that this Lagrangian is Lorentz invariant if notice

.. math::


   \gamma^0\cdot\gamma^0 = I,\ \ \ \gamma^0 S^\dagger\gamma^0 = S^{-1}

The theory of spinor field is somehow abundant, and this section only covers very basic conclusion about it. Therefore, you are suggested to refer to other textbooks about the Quantum Field Theory or spinor geometry for further information about spinor field theory.

