Scalar Field Theory with Interaction
------------------------------------

This section introduces the self-interaction theory of scalar field. As usual, the interaction is implemented as an additional interaction term :math:`\mathcal{L}_{\text{int}}` in Lagrangian. The interaction discussed here is assumed to satisfy the following condition

-  It is the self-interaction, i.e. :math:`\mathcal{L}_{\text{int}} = \mathcal{L}_{\text{int}}[\varphi]`
-  It has the form of polynomials.

Similarly, the construction starts from the generating functional. The generating functional of an interaction theory is

.. math::


   W[J] &= \int\mathcal{D}\varphi\exp\{\mathrm iS\} = \int\mathcal{D}\varphi\exp\{\mathrm i\!\!\int\!\!\mathcal{L}\! + \!\mathcal{L}_{\text{int}}[\varphi]\}\\
   &= \int\mathcal{D}\varphi\exp\{\mathrm i\!\!\int\!\!\mathcal{L}_{\text{int}}[\varphi]\}\exp\{\mathrm i\!\!\int\!\!\mathcal{L}\}

Next, we expand the first exponential (the one with interaction) according to definition

.. math::


   W[J] = \int\mathcal{D}\varphi\sum_{n=0}^\infty\frac{1}{n!}\left[\mathrm i\!\!\int\!\!\mathcal{L}_{\text{int}}[\varphi]\}\right]^n\exp\{\mathrm i\!\!\int\!\!\mathcal{L}\}

Now, recall our `first identity <./qft_ids.html>`__

.. math::


   \frac{1}{\mathrm{i}}\frac{\delta}{\delta J(x)}W_0[J] = \int\mathcal{D}\varphi\ \varphi(x)\exp\{\mathrm{i}S\}

Therefore, each :math:`\varphi(x)` in :math:`\mathcal{L}_{\text{int}}[\varphi]` can be *replaced* with :math:`\delta/\mathrm{i}\delta J(x)`, as long as :math:`\mathcal{L}_{\text{int}}[\varphi]` is a pure polynomial of :math:`\varphi`. In this case, we can write

.. math::


   W[J] = \int\mathcal{D}\varphi\sum_{n=0}^\infty\left[\mathrm i\!\!\int\!\!\mathcal{L}_{\text{int}}\!\!\left[\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J}\right]\}\right]^n\exp\{\mathrm i\!\!\int\!\!\mathcal{L}\}\\
   = \sum_{n=0}^\infty\frac{1}{n!}\left[\mathrm i\!\!\int\!\!\mathcal{L}_{\text{int}}\!\!\left[\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J}\right]\}\right]^n\int\mathcal{D}\varphi\exp\{\mathrm i\!\!\int\!\!\mathcal{L}\}

where expression :math:`\mathcal{L}_{\text{int}}\!\!\left[\delta/\mathrm{i}\delta J\right]` represents the the expression where all :math:`\varphi` in :math:`\mathcal{L}_{\text{int}}` is replaced with :math:`\delta/\mathrm{i}\delta J(x)`. The terms after the replacement no longer contain :math:`\varphi` and thus can be moved out of the path integral. And we find now that the path integral gives the generating functional :math:`W_0[J]` of free field. Transform back into the exponential form and we get

.. math::


   W[J] = \exp\{-\mathrm{i}\int\mathcal{L}_{\text{int}}\!\!\left[\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J}\right]\} W_0[J]

which is the result of second stage of our construction. The interaction of other kinds of fields (except for vector field in gauge theories) can be performed through similar manner.

