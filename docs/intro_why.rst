Why Path Integral?
------------------

If you have any previous touch with Quantum Field Theory, you may know
that there is a much more popular way to quantise the classical fields —
canonical quantisation. However, in this introduction, we will not
mention a word about it. If you are curious about the reason, this
section will tell you why. However, if you are just a new learner, you
can well skip this, it won’t affect.

Canonical Quantisation
~~~~~~~~~~~~~~~~~~~~~~

Take the scalar field for example. The canonical quantisation claims the
following “quantisation condition”

.. math:: [\varphi(\vec x, t), \pi(\vec x', t)] = \mathrm i\delta(\vec x-\vec x')

This is convenient since similar commutation relation has been studied
thoroughly in Quantum Mechanics. However, it is this very first
assumption that ruins the whole field theory.

To see this, let’s first review what the Quantum Mechanics claims. In
Quantum Mechanics, we have the following commutation relation

.. math:: [x_i, p_j] = \mathrm i\delta_{ij}

There is nothing wrong here if both :math:`x_i` and :math:`p_i` are
operators, and the product refers to operator composition. As an
example, explicitly write an representation as
:math:`p_i = -\mathrm i\partial_i` will satisfy the above relation.

However, although many physicists claim that the commutation relation of
fields is nothing but a continuous version of the point particle one, it
is still mathematically impossible for such a “continuous” commutation
relation to hold.

This can be seen through the following argument: field :math:`\varphi`
and :math:`\pi` are both scalar field; according to the definition of
scalar field product and subtraction, :math:`\varphi\pi` and
:math:`\pi\varphi` will both be scalar field, so will their commutator
:math:`[\varphi, \pi]`. Thus, the left hand side of the commutation
relation will be a scalar field (or more specifically, operator valued
scalar field).

However, the right hand side is not a scalar field. Instead, according
to the most moderate point of view, :math:`\delta(\vec x - \vec x')`
should be at most a generalized function. Therefore, the two sides of
the equation can never be equal.

Comments on Delta Function
~~~~~~~~~~~~~~~~~~~~~~~~~~

The delta function is always a subtle object in Physics. First invented
by Dirac in early 20th century, it has showed it magic in Quantum
Mechanics for a countless of times. Hence, although the expression of
Dirac delta function had been repeatedly refused, mathematicians were
eventually forced to investigate this strange “function” seriously.

Indeed, there has been several successful interpretation of delta
function, such as generalized function theory and Dirac delta measure in
measure theory. However, these implementation can only hold if the delta
function is inside the integral, no matter what the integral means.

This condition can be fully comply in Quantum Mechanics, which explains
why the delta function achieves that much. However, in canonical
quantisation, the commutation relation will require delta function to
appear barely outside. A `further investigation <@waiting>`__ reveals
that finally it is this carelessness that finally leads to the annoying
infinities in S-matrix, and hence brings difficulties in quantising
gravity.

Finally, we want to emphasise that the success of delta function in
Quantum Mechanics does not mean that it will succeed in Quantum Field
Theory too. The fact is: it fails. Therefore, in our introduction to
Quantum Field Theory, canonical quantisation is avoided and any further
usage of delta function will be carefully treated.
