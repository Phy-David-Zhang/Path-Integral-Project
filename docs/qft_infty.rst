First Glance at Infinities
--------------------------

This section will show you how the infinities emerge in Quantum Field Theory through a resonated toy of physicists --- :math:`\varphi^4` theory. The interaction term of :math:`\varphi^4` theory is

.. math::


   \mathcal{L}_{\text{int}} = -\frac{1}{4!}g\varphi^4

Recall that the generating functional of interaction theory is

.. math::


   W[J] = \exp\{-\mathrm{i}\int\mathcal{L}_{\text{int}}\!\!\left[\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J}\right]\} W_0[J]

Suppose the interaction is weak enough for us to neglect all terms of order higher than one. Therefore, the generating functional up to the first order is

.. math::


   W_\uparrow^{(1)}[J] = (1 - \mathrm{i}\int\mathcal{L}_{\text{int}}\!\!\left[\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J}\right]\})W_0[J] = (1 - \frac{\mathrm{i}g}{4!}\int\left[\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J}\right]^4\})W_0[J]

Notice that in this case the four functional derivatives are at the same point :math:`x`. Therefore, a calculation similar to the previous section will show

.. math::


   \frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J(x)}\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J(x)}W_0[J] = \tau(x,x) =  \mathrm i\Delta(x;x)\ \ ???

We see that the right hand side contains the value of Green's function at *zero*, which is clearly infinity. With higher order terms which contains even more derivatives, there might be even more infinities.

To deal with this infinities, we use a mathematical technique called **renormalization**. Looking back to where the infinities come and we find

.. math::


   \frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J(x)}(-\int\Delta_F(x;y)J(y)\mathrm{d}y)

makes no sense, since the functional derivative requires that :math:`\Delta_F(x;y)` be a function, but it is essentially a distribution (or generalized function). But things are not so bad. The Green's function is a distribution which usually has a function correspondence, and for most of the physical equations that we care, it has.

Nonetheless, the function corresponding to :math:`\Delta(x;y)` **has no definition** on :math:`x=y`. Therefore, the above expression hopes to get something **undefined**. This makes things much easier. If it is undefined, the most straight-forward way is to place an additional definition.

The renormalization procedure does exactly this stuff. Usually, we will impose some conditions (such as define the *physical mass* as the square-root of minus zero-point of two-point convex function) so that the value :math:`\Delta(x;x)` can be defined.

You are not expected to understand the harangue in the bracket in previous paragraph. The renormalization is a big topic and we will open a new chapter later for a systematically discussion.

