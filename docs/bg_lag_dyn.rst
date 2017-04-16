Lagrangian Dynamics of Fields
-----------------------------

.. note:: Before step into this section, we suggest you review the Lagrangian dynamics of classical point particles, as we are not going to go through that.

The Lagrangian density of a field :math:`\phi(x)` is a map :math:`\mathcal L(\phi,\partial_\mu\phi)` of field :math:`\phi` and its derivative :math:`\partial_\mu\phi`. Thus, the action can be constructed as

.. math::


   \mathcal S = \int \mathcal L(\phi,\partial_\mu\phi)\,\mathrm d^4x

Now, perform the variation of the action

.. math::


   \delta S &= \int \delta\mathcal L \,\mathrm d^4x\\
   &= \int \left({\partial\mathcal L\over \partial \phi}\delta\phi + {\partial\mathcal L\over\partial\partial_\mu\phi}\delta\partial_\mu\phi\right)\,\mathrm d^4x\\
   &= \int \left({\partial\mathcal L\over \partial \phi}\delta\phi + {\partial\mathcal L\over\partial\partial_\mu\phi}\partial_\mu\delta\phi\right)\,\mathrm d^4x\\
   &= \int \left({\partial\mathcal L\over \partial \phi} - \partial_\mu {\partial\mathcal L\over\partial\partial_\mu\phi}\right)\delta\phi\,\mathrm d^4x + \int \partial_\mu \left({\partial\mathcal L\over\partial\partial_\mu\phi}\delta\phi\right)\,\mathrm d^4x\\
   &= \int \left({\partial\mathcal L\over \partial \phi} - \partial_\mu {\partial\mathcal L\over\partial\partial_\mu\phi}\right)\delta\phi\,\mathrm d^4x = 0

The second equality is due to the fact that the variation of :math:`\phi` does not change the coordinate system; the fourth equality is because the second integral is a surface term under Stokes theorem, and the variation on the surface is zero.

Thus, to make the equality hold, the only possible way is

.. math::


   {\partial\mathcal L\over \partial \phi} - \partial_\mu {\partial\mathcal L\over\partial\partial_\mu\phi} = 0

This is the Lagrangian equation for fields.

