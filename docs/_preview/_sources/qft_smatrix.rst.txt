Scattering Matrix
-----------------

Scattering matrix, or **S-matrix**, is one of the major and core concept in both Particle and High Energy Physics --- since this is the most straight-forward way to verify the form of interaction.

The S-matrix is defined as an *infinite dimensional matrix* with each matrix element :math:`S_{\beta\alpha}` being the probability of the state evolving from :math:`\alpha` to :math:`\beta`, i.e.

.. math::


   S_{\beta\alpha} = \langle\beta|\alpha\rangle

.. note:: As a matter of fact, the S-matrix is not a typical "matrix". It is just a quantity with each one of them can be labelled by two indices. Also, in canonical quantization, S-matrix is actually an operator which, if it is finite dimensional, can be expressed as a matrix (but in Quantum Field Theory it is not). Therefore, when you see some concept which is a *matrix*, it might not mean to be a typical matrix, but some operator or quantity of two indices.

In Quantum Field Theory (as well as Particle Physics), we are especially interested in the following situation

    Two or more beams of free particle are generated and targeted at some point, interact with each other at the limited region near the point, then leave the interaction region, become free particles again and finally detected by the particle detectors.

The key point in the above picture is that the interaction only happens at a restricted region, and the particles are free outside the region. This approximation can be pretty accurate if the region is selected wisely so that the particles are separated by a considerably long distance. And it is prevalently implemented in many particle colliders.

The above picture suggests us write the field in the path integral as the addition of an "interact field" :math:`\varphi` and a free asymptotic field :math:`\varphi_{\text{as}}`, i.e. perform the following variable translation in the path integral

.. math::


   \varphi \mapsto \varphi + \varphi_{as}

where the asymptotic field :math:`\varphi_{\text{as}}` satisfies

.. math::


   (\partial^2\!\!-\!m^2)\varphi_{\text{as}} = 0

Therefore, the S-matrix with auxiliary field :math:`J` supplied is

.. math::


   S_0[J] = \int\mathcal{D}\varphi\exp\{-\mathrm{i}\int\frac{1}{2}\varphi[\partial^2\!\!-\!m^2]\varphi - J\varphi - J\varphi_{\text{as}}\} = \exp\{\mathrm{i}\varphi_{\text{as}}J\}W_0[J]

Similar formula also holds for situation with interaction. Then, just as what we have done in the last section, expand the exponential as Taylor series

.. math::


   S[J] = \sum_{n=0}^\infty\frac{1}{n!}\left[\mathrm{i}\varphi_{\text{as}}J\right]^nW[J]

Recall we have our `second identity <./qft_ids.html>`__

.. math::


   (\partial^2\!\!-\!m^2)\frac{1}{\mathrm{i}}\frac{\delta}{\delta J(x)}W_0[J] = J(x)W_0[J]

This inspires us that we can replace every :math:`J` in the Taylor series with :math:`(\partial^2\!\!-\!m^2)\delta/\mathrm{i}\delta J`. Hence

.. math::


   S[J] = \sum_{n=0}^\infty\frac{1}{n!}\left[\mathrm{i}\varphi_{\text{as}}(\partial^2\!\!-\!m^2)\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J}\right]^nW[J] = \exp\{\mathrm{i}\varphi_{\text{as}}(\partial^2\!\!-\!m^2)\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J}\}W[J]

To obtain the S-matrix, simply set the auxiliary field :math:`J` as zero

.. math::


   S = \left.\exp\{\mathrm{i}\varphi_{\text{as}}(\partial^2\!\!-\!m^2)\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J}\}W[J]\right|_{J=0}

This is the so-called **LSZ reduction formula**, which gives the S-matrix with inbound and outbound state designated by asymptotic field :math:`\varphi_{\text{as}}` from the generating functional.

