Two Significant Identities
--------------------------

In this section, you are going to meet two significant identities which play central roles in the following constructions. These identities are

.. math::


   \frac{1}{\mathrm{i}}\frac{\delta}{\delta J(x)}W_0[J] = \int\mathcal{D}\varphi\ \varphi(x)\exp\{\mathrm{i}S\}\\
   (\partial^2\!\!-\!m^2)\frac{1}{\mathrm{i}}\frac{\delta}{\delta J(x)}W_0[J] = J(x)W_0[J]

.. note:: To understand this section, you will find `Functional Derivative <./ms_func_deriv.html>`__ helpful.

First Identity
~~~~~~~~~~~~~~

The first identity can be verified through a calculation of functional derivative of :math:`W_0[J]` with respect to :math:`J(x)`. Specifically, we have

.. math::


   \frac{\delta}{\delta J(x)}W_0[J] &= \int\mathcal{D}\varphi\frac{\delta}{\delta J(x)}\left[\exp\{-\frac{1}{2}\mathrm{i}\int\varphi(\partial^2\!\!-\!m^2)\varphi + \mathrm{i}\int J\varphi\}\right]\\
   &= \int\mathcal{D}\varphi\frac{\delta}{\delta J(x)}\left[\mathrm{i}\int J\varphi\}\right]\exp\{\mathrm{i}S\} = \int\mathcal{D}\varphi\ \mathrm{i}\varphi(x)\exp\{\mathrm{i}S\}

The right hand side of the identity is sometimes interpreted as the *average value* of the field :math:`\varphi(x)` due to its formal similarities with the definition of average value in statistical mechanics.

Second Identity
~~~~~~~~~~~~~~~

The second identity can be gained through a direct calculation. Specifically, there is

.. math::


   \frac{1}{\mathrm{i}}\frac{\delta}{\delta J(x)}W_0[J] = \frac{1}{\mathrm{i}}\frac{\delta}{\delta J(x)}\exp\{-\frac{1}{2}\mathrm{i}\int J\Delta_F J\} = -\left[\int\Delta_F J(x)\right]\ W_0[J]

Therefore

.. math::


   (\partial^2\!\!-\!m^2)\frac{1}{\mathrm{i}}\frac{\delta}{\delta J(x)}W_0[J] = -\left[\int(\partial^2\!\!-\!m^2)\Delta_F J(x)\right]\ W_0[J] = J(x)W_0[J]

You are strongly suggested to remember the two identities since they are the very foundations of the following constructions of interaction theory and S-matrix.

