A Brief History
---------------

Unlike other Quantum Field Theory textbook, our introduction to the
history will not be so long. In this section, we only plan to introduce
the part that has direct connection to the motivation of Quantum Field
Theory.

.. note:: The following context will call `Geometric Unit System <bg_geo_unit.html>`__ and `Einstein Summation Convention <bg_eins.html>`__. Review the link if you have never heard of them — they are important!

Assuming that you already have the knowledge of Quantum Mechanics. At
least you are able to recognise the most famous equation shown below

.. math:: \mathrm{i}\frac{\partial}{\partial t}\psi = -\frac{1}{2m}\nabla^2\psi + V\psi

It is called a wave equation. Why? If you take

.. math:: \psi = A\exp\{-\mathrm{i}\omega t + \mathrm{i}\vec k\cdot \vec x\}

into the equation, you will find that it is a solution of the
Schrödinger equation as long as the following holds

.. math:: \omega = \frac{\vec k^2}{m} + V \label{difrel}

Recall that we have the following relationship in Quantum Mechanics

.. math:: \omega = E,\ \ \ \ \  k^i = p^i

where :math:`E` is the energy and :math:`p^i` is the momentum with
:math:`i=1,2,3`. Now, we immediately find that the previous equation
becomes

.. math:: E = \frac{\vec p^2}{m} + V

which is nothing but the energy-momentum relationship in Newtonian
classical mechanics.

.. warning:: Now we release symbol :math:`\psi`. This indicates that :math:`\psi` in the following context will have a different meaning.

So now we are going to think: what if we want it to be relativistic?
Assuming that you already have the knowledge of Relativity. In Special
Theory of Relativity, the energy-momentum relationship becomes

.. math:: E^2 = \vec p^2 + m^2

To achieve this result, simply reverse the previous steps. The above
relationship should require

.. math:: \omega^2 = \vec k^2 + m^2

And this requires

.. math:: (\partial_\mu\partial^\mu - m^2)\varphi = 0

where the `signature of metric <@waiting>`__ here is :math:`+2`. This is
the famous “Klein-Gordon equation” — the relativistic version of
Schrödinger equation. The quotes here indicates that it still has some
subtle difference with the *real* Klein-Gordon equation, as we are going
to see next.

It seems that it is so easy to combine Quantum Mechanics and Special
Theory of Relativity. Nonetheless, things are not so trivial. The
Newtonian energy-momentum relation can guarantee that the energy of a
free (:math:`V=0`) particle is always positive. However, the
relativistic version can not. The relativistic energy-momentum relation
reveals that

.. math:: E = \pm\sqrt{\vec p^2+m^2}

where we discover that there are both positive and negative solutions
are possible. This issue is not paramount in classical theory, since the
energy of a classical particle can only varies continuously, and there
is a gap of :math:`2m` between the lowest positive energy :math:`E=m`
(where :math:`\vec p=0`) and the greatest negative value :math:`E=-m` (where
:math:`\vec p=0`). Thus, a classical particle can have either positive or
negative energy — the only matter is to set an initial sign.

However, recall that quantised particles can jump between discrete
energy levels. Hence, it is just a matter of probability for them to
jump from a positive energy to a negative one and … fall all the way
down to minus infinity. This then becomes a major difficulty of
“Klein-Gordon equation”.

Also, let’s investigate the continuity equation. In Quantum Mechanics,
there is

.. math::

   \mathrm{i}\frac{\partial}{\partial t}\varphi &= -\frac{1}{2m}\nabla^2\varphi + V\varphi\\
   -\mathrm{i}\frac{\partial}{\partial t}\varphi^* &= -\frac{1}{2m}\nabla^2\varphi^* + V\varphi^*

The first equation is the Schrödinger equation and the second equation
is nothing other than the complex conjugate of the first one.

Now, we apply :math:`\varphi^*` to the first equation and
:math:`\varphi` to the second one, and let the first one subtract the
second

.. math:: \varphi^*\mathrm{i}\frac{\partial}{\partial t}\varphi + \varphi\mathrm{i}\frac{\partial}{\partial t}\varphi^* = \varphi\frac{1}{2m}\nabla^2\varphi^* - \varphi^*\frac{1}{2m}\nabla^2\varphi

which, after a transform, becomes

.. math:: \mathrm{i}\frac{\partial}{\partial t}\varphi\varphi^* = \frac{1}{2m}\nabla(\varphi\nabla\varphi^* - \varphi^*\nabla\varphi)

To gain the continuity equation, the only thing to do is to identify the
probability density and probability current as

.. math:: \rho = \varphi\varphi^*,\ \ \ \ \ \vec{j} = {1\over2m\mathrm i}(\varphi\nabla\varphi^* - \varphi^*\nabla\varphi)

The probability density is the square of the wave function, and will
always be positive due to the property of square. Everything works fine
here.

However, if you derive the continuity equation corresponding to the
“Klein-Gordon equation”, you will find that the “probability density”
now becomes

.. math:: \rho \sim \varphi^*\frac{\partial}{\partial t}\varphi - \varphi\frac{\partial}{\partial t}\varphi^*

The minus sign indicates that it might be negative(!), which destroys
the probabilistic interpretation of quantum theory. This is another
major difficulty of “Klein-Gordon equation”.

To solve the difficulties, physicists decided to reinterpret symbol
:math:`\varphi` here as **classical field**, instead of wave function.
Then, similar to the Quantum Mechanics, path integral is used to
quantise the classical field.

Now, if you can follow the pace, welcome to the next section.
