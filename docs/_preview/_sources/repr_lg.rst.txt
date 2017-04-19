Representation of Lorentz Group
-------------------------------

This section introduces some very basic representation theory of Lorentz Group. In fact, the representation theory of Lorentz Group can be abundant, and here we only care about the non-trivial and pragmatic parts, namely the spinor representation and vector representation.

.. note:: Before Continuing, you need to cover at least `Basic Group Theory <./bg_liegp.html>`__.

Usually, a Lorentz transformation can be divided to boost and rotation. The boost along the :math:`x`-axis can be written as

.. math::


   K_x = 
   \left[
   \begin{matrix}
   \mathrm{ch}\lambda & \mathrm{sh}\lambda & 0 & 0\\
   \mathrm{sh}\lambda & \mathrm{ch}\lambda & 0 & 0\\
   0 & 0 & 1 & 0\\
   0 & 0 & 0 & 1
   \end{matrix}
   \right]

where :math:`\mathrm{ch}\lambda` is the hyperbolic cosine and :math:`\mathrm{sh}\lambda` is the hyperbolic sine. It is easy to verify that this is equivalent to the normal form of Lorentz transformation once notice that :math:`\mathrm{ch}\lambda = \gamma, \mathrm{sh}\lambda = \gamma v, \mathrm{th}\lambda = v`. Also, for the rotation along the :math:`z`-axis, we have

.. math::


   J_z = 
   \left[
   \begin{matrix}
   0 & 0 & 0 & 0\\
   0 & \cos\eta& \sin\eta & 0\\
   0 & -\sin\eta & \cos\eta & 0\\
   0 & 0 & 0 & 1
   \end{matrix}
   \right]

which should be familiar to all. You should be able to write down the boosts and rotations along the other axis. All the Lorentz transformation can be formed by these boosts and rotations.

We now want to find out the generators of the above boost. According to the form of infinitesimal transformation, the generator should be the first order derivative of the transformation at identity point, namely

.. math::


   \vec K_x = \left.\frac{\partial K_x}{\partial\lambda}\right|_{\lambda=0} = 
   \left[
   \begin{matrix}
   0 & 1 & 0 & 0\\
   1 & 0 & 0 & 0\\
   0 & 0 & 0 & 0\\
   0 & 0 & 0 & 0
   \end{matrix}
   \right]

You are encouraged to write down the generators for the other boosts and rotations. Moreover, you can also calculate explicitly :math:`\exp\{\lambda\vec K_x\}` as described in Basic Group Theory and verify that it equals :math:`K_x(\lambda)`.

Now that we have the generators, the infinitesimal transformation will have the form

.. math::


   1 + \eta_x\vec K_x + \eta_y \vec K_y + ...

To simplify the formulation, we introduce a anti-symmetric lists of matrix :math:`L_{\mu\nu}` as

.. math::


   L_{01} &= -L_{10} = \mathrm{i}\vec K_x,\ \ \ L_{02} = -L_{20} = \mathrm{i}\vec K_y,\ \ \ L_{03} = -L_{30} = \mathrm{i}\vec K_z\\
   L_{12} &= -L_{21} = \mathrm{i}\vec J_z,\ \ \ L_{23} = -L_{32} = \mathrm{i}\vec J_x,\ \ \ L_{13} = -L_{31} = \mathrm{i}\vec J_y\\

.. note:: Anti-symmetric means :math:`L_{\mu\nu} = -L_{\nu\mu}`, which implies the diagonal elements :math:`L_{ii} = 0`.

Therefore, the infinitesimal transformation is simplified to

.. math::


   1 - \frac{1}{2}\mathrm{i}\epsilon^{\mu\nu}L_{\mu\nu}

where :math:`\epsilon^{\mu\nu}` is the corresponding parameters (:math:`\epsilon^{01} = \eta_x` for example), and it is also anti-symmetric. The :math:`1/2` is necessary because we need to eliminate the factor :math:`2` in :math:`\epsilon^{01}L_{01} + \epsilon^{10}L_{10} = 2\epsilon^{01}L_{01}`.

Consequently, all Lorentz transformation can be written under the form

.. math::


   \varLambda(\epsilon) = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{\mu\nu}L_{\mu\nu}\}

This formula is called the **vector representation** of the Lorentz Group. This is the default representation for the tetrad.

.. note:: Rigorously speaking, the representation should be a map from the group element to the automorphism of a vector space. Thus, the above equation should be viewed as a map to map the group element (LHS) to an automorphism (RHS).

As we know, the generators :math:`L_{\mu\nu}` can be viewed as a "basis" of the Lorentz group. However, this is not the only "basis". Next, we are going to find out another one.

Before continuing, let's first define four matrices :math:`\gamma_\mu, \mu=0,1,2,3` that satisfy

.. math::


   \{\gamma_\mu, \gamma_\nu\} = \gamma_\mu\gamma_\nu + \gamma_\nu\gamma_\mu = 2\eta_{\mu\nu}

where :math:`\eta_{\mu\nu}` is the Minkowski metrics. Then, we would like to point out that the following matrices are also generators of Lorentz group

.. math::


   S_{\mu\nu} = \frac{1}{4}\mathrm{i}[\gamma_\mu, \gamma_\nu]

.. note:: Why? Well, we are not able to explain now since it needs Lie algebra theory. Go and find a reference about Lie algebra if you really wonder why.

Therefore, we can express the Lorentz transformation as

.. math::


   \varLambda(\epsilon) = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{\mu\nu}S_{\mu\nu}\}

This formulation is called **spinor representation** of the Lorentz group.

Finished. But I do want to add that the representation theory of Lorentz group is quite a enchanting theory. So I suggest a careful review on this theory if you are able. It will greatly deepen your understanding through the algebraic structure of the physical field.

