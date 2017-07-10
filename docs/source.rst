What is Path Integral Project?
------------------------------

I promise, this might be the most comprehensible introduction of Quantum Field Theory existed, ever. Indeed, the Quantum Field Theory can be one of the most powerful but complicated advanced physical theories ever created. And, I was one of the many victims of this complication.

However, we want to put this situation to an end. Instead of directly throwing piles of academic illustration, we hope to clarify all the logic during the construction of Quantum Field Theory. Moreover, it is also expected that some mathematical structures in Quantum Field Theory to be clarified if possible.

Accordingly, the Path Integral Project emerges. This project will do a profound investigation towards the construction of Quantum Field Theory, and to see if any amendments during this process will provide hint towards a valid quantised gravitational theory.

Excited? Then just follow my pace to the next section. Welcome to the world of quantum field theory.

A Brief History
---------------

Unlike other Quantum Field Theory textbook, our introduction to the history will not be so long. In this section, we only plan to introduce the part that has direct connection to the motivation of Quantum Field Theory.

.. note:: The following context will call `Geometric Unit System <./bg_geo_unit.html>`__ and `Einstein Summation Convention <./bg_eins.html>`__. Review the link if you have never heard of them — they are important!

Assuming that you already have the knowledge of Quantum Mechanics. At least you are able to recognise the most famous equation shown below

.. math::


   \mathrm{i}\frac{\partial}{\partial t}\psi = -\frac{1}{2m}\nabla^2\psi + V\psi

It is called a wave equation. Why? If you take

.. math::


   \psi = A\exp\{-\mathrm{i}\omega t + \mathrm{i}\vec k\cdot \vec x\}

into the equation, you will find that it is a solution of the Schrödinger equation as long as the following holds

.. raw:: latex

   \begin{equation} 
   \omega = \frac{\vec k^2}{m} + V \label{difrel}
   \end{equation}

Recall that we have the following relationship in Quantum Mechanics

.. math::


   \omega = E,\ \ \ \ \  k^i = p^i

where :math:`E` is the energy and :math:`p^i` is the momentum with :math:`i=1,2,3`. Now, we immediately find that the previous equation becomes

.. math::


   E = \frac{\vec p^2}{m} + V

which is nothing but the energy-momentum relationship in Newtonian classical mechanics.

.. warning:: Now we release symbol :math:`\psi`. This indicates that :math:`\psi` in the following context will have a different meaning.

So now we are going to think: what if we want it to be relativistic? Assuming that you already have the knowledge of Relativity. In Special Theory of Relativity, the energy-momentum relationship becomes

.. math::


   E^2 = \vec p^2 + m^2

To achieve this result, simply reverse the previous steps. The above relationship should require

.. raw:: latex

   \begin{equation} 
   \omega^2 = \vec k^2 + m^2 
   \end{equation}

And this requires

.. math::


   (\partial_\mu\partial^\mu - m^2)\varphi = 0

where the `signature of metric <@waiting>`__ here is :math:`+2`. This is the famous “Klein-Gordon equation” — the relativistic version of Schrödinger equation. The quotes here indicates that it still has some subtle difference with the *real* Klein-Gordon equation, as we are going to see next.

It seems that it is so easy to combine Quantum Mechanics and Special Theory of Relativity. Nonetheless, things are not so trivial. The Newtonian energy-momentum relation can guarantee that the energy of a free (:math:`V=0`) particle is always positive. However, the relativistic version can not. The relativistic energy-momentum relation reveals that

.. math::


   E = \pm\sqrt{\vec p^2+m^2}

where we discover that there are both positive and negative solutions are possible. This issue is not paramount in classical theory, since the energy of a classical particle can only varies continuously, and there is a gap of :math:`2m` between the lowest positive energy :math:`E=m` (where :math:`\vec p=0`) and the greatest negative value :math:`E=-m` (where :math:`\vec p=0`). Thus, a classical particle can have either positive or negative energy — the only matter is to set an initial sign.

However, recall that quantised particles can jump between discrete energy levels. Hence, it is just a matter of probability for them to jump from a positive energy to a negative one and … fall all the way down to minus infinity. This then becomes a major difficulty of “Klein-Gordon equation”.

Also, let’s investigate the continuity equation. In Quantum Mechanics, there is

.. math::


   \mathrm{i}\frac{\partial}{\partial t}\varphi = -\frac{1}{2m}\nabla^2\varphi + V\varphi\\
   -\mathrm{i}\frac{\partial}{\partial t}\varphi^* = -\frac{1}{2m}\nabla^2\varphi^* + V\varphi^*

The first equation is the Schrödinger equation and the second equation is nothing other than the complex conjugate of the first one.

Now, we apply :math:`\varphi^*` to the first equation and :math:`\varphi` to the second one, and let the first one subtract the second

.. math::


   \varphi^*\mathrm{i}\frac{\partial}{\partial t}\varphi + \varphi\mathrm{i}\frac{\partial}{\partial t}\varphi^* = \varphi\frac{1}{2m}\nabla^2\varphi^* - \varphi^*\frac{1}{2m}\nabla^2\varphi

which, after a transform, becomes

.. math::


   \mathrm{i}\frac{\partial}{\partial t}\varphi\varphi^* = \frac{1}{2m}\nabla(\varphi\nabla\varphi^* - \varphi^*\nabla\varphi)

To gain the continuity equation, the only thing to do is to identify the probability density and probability current as

.. math::


   \rho = \varphi\varphi^*,\ \ \ \ \ \vec{j} = {1\over2m\mathrm i}(\varphi\nabla\varphi^* - \varphi^*\nabla\varphi)

The probability density is the square of the wave function, and will always be positive due to the property of square. Everything works fine here.

However, if you derive the continuity equation corresponding to the “Klein-Gordon equation”, you will find that the “probability density” now becomes

.. math::


   \rho \sim \varphi^*\frac{\partial}{\partial t}\varphi - \varphi\frac{\partial}{\partial t}\varphi^*

The minus sign indicates that it might be negative(!), which destroys the probabilistic interpretation of quantum theory. This is another major difficulty of “Klein-Gordon equation”.

To solve the difficulties, physicists decided to reinterpret symbol :math:`\varphi` here as **classical field**, instead of wave function. Then, similar to the Quantum Mechanics, path integral is used to quantise the classical field.

Now, if you can follow the pace, welcome to the next section.

Why Path Integral?
------------------

If you have any previous touch with Quantum Field Theory, you may know that there is a much more popular way to quantise the classical fields — canonical quantisation. However, in this introduction, we will not mention a word about it. If you are curious about the reason, this section will tell you why. However, if you are just a new learner, you can well skip this, it won’t affect.

Canonical Quantisation
~~~~~~~~~~~~~~~~~~~~~~

Take the scalar field for example. The canonical quantisation claims the following “quantisation condition”

.. math::


   [\varphi(\vec x, t), \pi(\vec x', t)] = \mathrm i\delta(\vec x-\vec x')

This is convenient since similar commutation relation has been studied thoroughly in Quantum Mechanics. However, it is this very first assumption that ruins the whole field theory.

To see this, let’s first review what the Quantum Mechanics claims. In Quantum Mechanics, we have the following commutation relation

.. math::


   [x_i, p_j] = \mathrm i\delta_{ij}

There is nothing wrong here if both :math:`x_i` and :math:`p_i` are operators, and the product refers to operator composition. As an example, explicitly write an representation as :math:`p_i = -\mathrm i\partial_i` will satisfy the above relation.

However, although many physicists claim that the commutation relation of fields is nothing but a continuous version of the point particle one, it is still mathematically impossible for such a “continuous” commutation relation to hold.

This can be seen through the following argument: field :math:`\varphi` and :math:`\pi` are both scalar field; according to the definition of scalar field product and subtraction, :math:`\varphi\pi` and :math:`\pi\varphi` will both be scalar field, so will their commutator :math:`[\varphi, \pi]`. Thus, the left hand side of the commutation relation will be a scalar field (or more specifically, operator valued scalar field).

However, the right hand side is not a scalar field. Instead, according to the most moderate point of view, :math:`\delta(\vec x - \vec x')` should be at most a generalized function. Therefore, the two sides of the equation can never be equal.

Comments on Delta Function
~~~~~~~~~~~~~~~~~~~~~~~~~~

The delta function is always a subtle object in Physics. First invented by Dirac in early 20th century, it has showed it magic in Quantum Mechanics for a countless of times. Hence, although the expression of Dirac delta function had been repeatedly refused, mathematicians were eventually forced to investigate this strange “function” seriously.

Indeed, there has been several successful interpretation of delta function, such as generalized function theory and Dirac delta measure in measure theory. However, these implementation can only hold if the delta function is inside the integral, no matter what the integral means.

This condition can be fully comply in Quantum Mechanics, which explains why the delta function achieves that much. However, in canonical quantisation, the commutation relation will require delta function to appear barely outside. A `further investigation <@waiting>`__ reveals that finally it is this carelessness that finally leads to the annoying infinities in S-matrix, and hence brings difficulties in quantising gravity.

Finally, we want to emphasise that the success of delta function in Quantum Mechanics does not mean that it will succeed in Quantum Field Theory too. The fact is: it fails. Therefore, in our introduction to Quantum Field Theory, canonical quantisation is avoided and any further usage of delta function will be carefully treated.

Theory of What?
---------------

Although philosophy is not a decisive factor of the effectiveness of a theory, it is still noticeable in the construction of a theoretical framework. This section embodies some of the author's thoughts on the insights of Quantum Field Theory. The main task of this section is to answer a question: is Quantum Field Theory a quantum theory of field? And if not, what it is?

.. note:: As a beginner, you may not be able to understand the following context quite well, and that's completely normal. The only thing that we want you to remember, is that Quantum Field Theory actually describes particles, instead of fields.

Quantum Theory of Fields
~~~~~~~~~~~~~~~~~~~~~~~~

Before doing any reasoning, it is necessary to clarify what exactly is meant by calling a quantum theory of something. Let's first look at Classical Mechanics and Quantum Mechanics, where they should be called a classical theory of particles and a quantum theory of particles respectively.

To construct a classical theory of particles, we need at least two things: the state of particle and the propagation rule of the state. Routinely, the state of particle can be parameterized by the position :math:`q` and its time derivative :math:`\dot{q}`. And, the evolution rules are given by the Lagrangian formalism

.. math::


   S = \int \mathcal{L}[q,\dot{q}]\,\mathrm{d}t

When we transform the classical theory of particles to quantum theory, namely quantize the classical theory, we replace the state with quantum state and propagation with path integral. Specifically, in Quantum Mechanics, we have the quantized state of particle governed by

.. math::


   |q'\rangle = \int\mathrm{d}q\,|q\rangle \int_q^{q'}\mathcal{D}q\exp\{\mathrm{i}S\}

Therefore, we can generalize to get the meaning of "quantum theory of :math:`X`\ ” as follows. First, we need a classical theory of :math:`X`, with state :math:`\Omega(X)` governed by

.. math::


   S = \int \mathcal{L}[\Omega(X)]\,\varepsilon

where :math:`\varepsilon` is some measure. Then, a quantum theory of :math:`X` consists of a quantum state of :math:`X` governed by

.. math::


   |X'\rangle = \int\mathrm{d}X\,|X\rangle \int_X^{X'}\mathcal{D}X\exp\{\mathrm{i}S\}

According to this *definition*, the quantum theory of field should essentially consist of a quantum state of field :math:`|\varphi\rangle` governed by the path integral of field

.. math::


   |\varphi'\rangle = \int\mathrm{d}\varphi\,|\varphi\rangle \int_\varphi^{\varphi'}\mathcal{D}\varphi\exp\{\mathrm{i}S\}

This is what we hope a quantum theory of field should look like --- by a direct analogy with what Quantum Mechanics looks like. Nonetheless, a typical Quantum Field Theory looks very different from the quantum theory of field as described above.

Quantum Field Theory
~~~~~~~~~~~~~~~~~~~~

The most noticeable difference between the Quantum Field Theory and a quantum theory of field lies in the construction of quantum state. A typical quantum theory of field should be equipped with a state of field. However, in Quantum Field Theory, the state is actually an element of **Fock space** defined as follows.

.. math::


   \mathcal{F} &= \bigoplus_{n=0}^\infty\mathcal{H}^{\otimes n}\\
   &= \mathbb{C}\ \ \ -\ \text{vacuum}\\
   &\oplus \mathcal{H}\ \ \ -\ \text{one particle state}\\
   &\oplus (\mathcal{H}\otimes\mathcal{H})\ \ \ - \ \text{two particle state}\\
   &\oplus\ldots\oplus\\
   &\oplus (\mathcal{H}\otimes\ldots\otimes\mathcal{H})\ \ \ -\ \text{many particle state}\\
   &\oplus\ldots\\

where :math:`\mathcal{H}` is the Hilbert space of one particle state. Therefore, the Fock space is actually a direct sum of states with all possible particle numbers.

The situation becomes somehow bizarre here --- the state in Quantum *Field* Theory is actually the state of *particles*, instead of *fields*. This is exactly one of the sources of the complication of Quantum Field Theory --- we use the field theory to describe the behaviour of particles.

A probable cause of this situation may be found from the history. The motivation of Quantum Field Theory in history came from the efforts to make Quantum Mechanics relativistic. Therefore, relativistic Quantum Mechanics should provide an answer to this eccentricity.

Relativistic Quantum Mechanics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The relativistic Quantum Mechanics tries to make Quantum Mechanics and *Special* Relativity compatible. One of the central ideas of relativistic Quantum Mechanics is that the particle number can vary. Therefore, it is reasonable to construct such a Fock space which consists of all states of all possible particle number.

To describe the change of particle number, we need creation :math:`a^\dagger_p` and annihilation :math:`a_p` operators, where :math:`a^\dagger_p` creates a particle of momentum :math:`p` and :math:`a_p` annihilates one. And interestingly, if we perform some formal Fourier transform for these operators

.. math::


   \int \mathrm{d}p\ (a^\dagger_p e^{\mathrm{i}px} + a_p e^{-\mathrm{i}px})\ \ \rightarrow\ \ \phi(x)

It turns out to be some scalar field. However, this "field" has significant difference with the field in the quantum theory of field, although it has quite a lot fair reasons to be called a field.

So What?
~~~~~~~~

In the author's point of view, it is not reasonable enough to make the two kinds of "field" identical. Unfortunately, it is in conventional Quantum Field Theory. And the author himself can not propose any better theories.

Therefore, in our introduction of Quantum Field Theory, we compromise. A quantum theory of field will first be constructed. Then it will be brute-forcely transformed to relativistic Quantum Mechanics in construction of scattering theory.

Classical Theory: Scalar Field
------------------------------

.. note:: This context will require knowledge on Lagrangian dynamics of fields. If you have not yet cover that in your previous learning, you will find `Lagrangian Form of Fields <./bg_lag_dyn.html>`__ helpful.

The Lagrangian of a scalar field is usually written as

.. math::


   \mathcal L = -\partial_\mu\varphi^*\partial^\mu\varphi - m^2\varphi^*\varphi

Alternatively, we can write

.. math::


   \mathcal L = \varphi^*(\partial^\mu\partial_\mu - m^2)\varphi

The equivalence between the two expression can be manifest once notice

.. math::


   \partial_\mu(\varphi^*\partial^\mu\varphi) = \varphi^*\partial^\mu\partial_\mu \varphi + \partial_\mu\varphi^*\partial^\mu\varphi = 0

The last equality is due to the fact that the left hand side is a surface term in the action integral.

Using the Lagrange equation, we get the equations of motion of scalar field

.. math::


   (\partial^\mu\partial_\mu - m^2)\varphi = 0\\
   (\partial^\mu\partial_\mu - m^2)\varphi^* = 0

This is the “real” **Klein-Gordon equation** — the equation of scalar field.

Solution of Klein-Gordon Equation
---------------------------------

.. note:: This section is important to the canonical quantisation method, and will not influence the overall logic. You may skip this if you wish.

In this section, we look at the general solution of the Klein-Gordon equation. We do this for :math:`\varphi`, and similar procedure can be easily carried out for :math:`\varphi^*`.

For any possible field :math:`\varphi`, we can perform Fourier expansion as

.. math::


   \varphi = \int{\mathrm d^4k\over(2\pi)^4}a(k)\exp\{-\mathrm i k^\mu x_\mu\}

.. note:: Well, you may notice that here we do not take the symmetric form of the Fourier transformation. Although personally I prefer the symmetric form, but trust me, it can make all the successive discussions awful.

Take the above expression back into the equation, we get the dispersion relation

.. math::


   k^2 + m^2 = 0

This relation serves as a constraint to the wave number :math:`k^\mu`. Thus, to gain the solution, all we need to do is to switch the integral measure to `delta measure <@waiting>`__

.. math::


   \varphi(x) = \int{\mathrm d^4k\over(2\pi)^4}a(k)\exp\{-\mathrm i k^\mu x_\mu\}\cdot2\pi\delta(k^2+m^2)

Factor :math:`2\pi` is necessary since we are going to perform the integral once, like

.. math::


   \varphi(x) &= \int{\mathrm d\omega \mathrm d^3k\over(2\pi)^4}a(k)\exp\{-\mathrm i k^\mu x_\mu\}\cdot2\pi\delta(-\omega^2 + \vec k^2 + m^2)\\
   &= \int{\mathrm d\omega^2 \mathrm d^3k\over2\omega(2\pi)^3}a(k)\exp\{-\mathrm i k^\mu x_\mu\}\cdot\delta(-\omega^2 + \vec k^2 + m^2)\\
   &= \int{\mathrm d^3k\over2\omega_k(2\pi)^3}a(k)\exp\{\mathrm i(\omega_k t - \vec k \vec x\} + \int{\mathrm d^3k\over(-2\omega_k)(2\pi)^3}a(k)\exp\{\mathrm i(-\omega_k t - \vec k \vec x\}\\
   &= \int{\mathrm d^3k\over2\omega_k(2\pi)^3}a(k)\exp\{\mathrm i(\omega_k t - \vec k \vec x\} + \int{\mathrm d^3k\over(2\omega_k)(2\pi)^3}a(-k)\exp\{\mathrm i(-\omega_k t + \vec k \vec x\}\\
   &= \int{\mathrm d^3k\over2\omega_k(2\pi)^3}\left[a(k)\exp\{-\mathrm i(k^\mu x_\mu\} + a(-k)\exp\{\mathrm i(k^\mu x_\mu\} \right]

where :math:`\omega_k = \sqrt{\vec k^2 + m^2}`. The fourth equality is nothing other than reversing the direction of :math:`\vec k`. Hence, we get the general form of the solution of Klein-Gordon equation.

The Symmetry of Fields
----------------------

To extend our investigation towards spinor field and vector field, it is inevitable to introduce the change of components of fields under Lorentz transformation. This context, however, can be as complicated as a combination of Differential Geometry, Lie Group and Lie Algebra theory and Fibre Bundle theory. It would be much better if you are able to fully review these contexts. But anyway, we still try to provide a very basic introduction either to make our logic coherent or to provide motivation as you are studying those enigmatic mathematical theories.

.. note:: To understand this section, you at least need to know `some very basic Differential Geometry <./bg_diff_geo.html>`__ and `basic Linear Algebra <./bg_linalg.html>`__.

Currently, we are talking about classical fields. The classical field is a kind of physical object. Therefore, despite that we can develop some tools (e.g. coordinate system or basis) to describe it, it should in a whole remain unchanged after certain manual transformation (e.g. re-selection of the basis).

However, this does not mean that the components of the field will remain invariant. In fact, except for the scalar field (we will analyse this later), many other types of fields will encounter a component change after the change of basis or coordinate system. Hence, based on the behaviour of the variation of components, we can classify the physical fields.

A conclusion is needed: it is possible to naturally set up an :math:`n`-dim vector space associated to every point in an :math:`n`-dim manifold. The basis of this specific vector space is called **tetrad** (or :math:`n`-**frame**, **veirbein** in some references).

    We are not going to elucidate this conclusion since it would be a harangue. If you are interested, please referred to textbooks on Differential Geometry for further details.

In Quantum Field Theory, we care about three types of fields --- scalar field, spinor field and vector field. Please notice that the term "scalar" and "vector" here are domain specific, which means that they might have a similar but essentially different meaning in other contexts.

**Scalar field** is a kind of field which does not change under any transformation of tetrad; **spinor field** transforms according to spinor representation of the Lorentz group, and **vector field** transforms according to the vector representation.

I know you don't understand. But don't worry, it is going to be illustrated next.

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

To simplify the formulation, we introduce a anti-symmetric lists of matrix :math:`L_{ab}` as

.. math::


   L_{01} &= -L_{10} = \mathrm{i}\vec K_x,\ \ \ L_{02} = -L_{20} = \mathrm{i}\vec K_y,\ \ \ L_{03} = -L_{30} = \mathrm{i}\vec K_z\\
   L_{12} &= -L_{21} = \mathrm{i}\vec J_z,\ \ \ L_{23} = -L_{32} = \mathrm{i}\vec J_x,\ \ \ L_{13} = -L_{31} = \mathrm{i}\vec J_y\\

.. note:: Anti-symmetric means :math:`L_{ab} = -L_{ba}`, which implies the diagonal elements :math:`L_{ii} = 0`.

Therefore, the infinitesimal transformation is simplified to

.. math::


   1 - \frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}

where :math:`\epsilon^{ab}` is the corresponding parameters (:math:`\epsilon^{01} = \eta_x` for example), and it is also anti-symmetric. The :math:`1/2` is necessary because we need to eliminate the factor :math:`2` in :math:`\epsilon^{01}L_{01} + \epsilon^{10}L_{10} = 2\epsilon^{01}L_{01}`.

Consequently, all Lorentz transformation can be written under the form

.. math::


   \varLambda(\epsilon) = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}\}

This formula is called the **vector representation** of the Lorentz Group. This is the default representation for the tetrad.

.. note:: Rigorously speaking, the representation should be a map from the group element to the automorphism of a vector space. Thus, the above equation should be viewed as a map to map the group element (LHS) to an automorphism (RHS).

As we know, the generators :math:`L_{ab}` can be viewed as a "basis" of the Lorentz group. However, this is not the only "basis". Next, we are going to find out another one.

Before continuing, let's first define four matrices :math:`\gamma_a, a=0,1,2,3` that satisfy

.. math::


   \{\gamma_a, \gamma_b\} = \gamma_a\gamma_b + \gamma_b\gamma_a = -2\eta_{ab}

where :math:`\eta_{ab}` is the Minkowski metrics. Then, we would like to point out that the following matrices are also generators of Lorentz group

.. math::


   S_{ab} = \frac{1}{4}\mathrm{i}[\gamma_a, \gamma_b]

.. note:: Why? Well, we are not able to explain now since it needs Lie algebra theory. Go and find a reference about Lie algebra if you really wonder why.

Therefore, we can express the Lorentz transformation as

.. math::


   \varLambda(\epsilon) = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}S_{ab}\}

This formulation is called **spinor representation** of the Lorentz group.

Finished. But I do want to add that the representation theory of Lorentz group is quite a enchanting theory. So I suggest a careful review on this theory if you are able. It will greatly deepen your understanding through the algebraic structure of the physical field.

Scalar, Spinor and Vector (Tensor) Field
----------------------------------------

.. note:: Please make sure you have covered the previous section `Representation of Lorentz Group <./repr_lg.html>`__.

This section will tell you how to define the scalar, spinor and vector (tensor) field. But before that, it is suggested to cover `Basic Linear Algebra <./bg_linalg.html>`__ for clarification of possible ambiguity of "vector". To avoid this ambiguity, we use term **linear space** for the *vector space* in `Linear Algebra <./bg_linalg.html>`__.

Physical Field
~~~~~~~~~~~~~~

In Quantum Field Theory, **field** is a central concept. In general, field is a map from the spacetime point to some object (numbers, arrows, etc.). All fields can form a linear space if the *object* also forms a linear space (as a practice, think about how to define that space). Although looked trivial, there is one thing that makes this concept intriguing --- spacetime point. Spacetime point can be too abstract for analysis such that, like what we do in Group Theory, we should set up a manifold for it. With a manifold, every spacetime point has its unique coordinates, which is a powerful tool for analysis.

However, the choice of coordinate system is artificial, and a law of nature should never depend on such an artificial object. Thus, it is crucial that the field should not vary after a change of coordinate system (and anything possibly related, basis of the field for example).

But that does not mean that the components of the field will also be invariant. In fact, **based on the different behaviour of the field components under transformations, we divide the physical field into several types** --- scalar field, spinor field and vector (tensor) field. Specifically, any field (as an element of a linear space) can be written as

.. math::


   \phi = \phi_i \cdot e^i

where :math:`\phi_i` is the components of the field and :math:`e^i` is a basis for the linear space. Now, if we perform a transformation :math:`g` to the basis, the components should transform inversely in order to make the combination invariant, i.e.

.. math::


   \phi = g^{-1}(\phi_i)\cdot g(e^i)

Nonetheless, the above expression is meaningless. As we have pointed out, the transformation is usually constructed using Lie group. And in Quantum Field Theory, it is Lorentz Group. However, we find that the expression :math:`g^{-1}(\phi_i)` and :math:`g(e^i)` undefined, since there is no definition indicating how to apply an element of Lie group to the components and basis of the field. Thus, to let the expression make sense, we need additional information of how the group element acts on the components and the basis. This designation is called **representation** of Lie group.

.. warning:: Important Notice: the dot in the previous two equations may not have the significance of certain "product". You will see this later.

A simple example is when the Lie group is :math:`\mathrm{GL}(n)`. Then a trivial representation is just to define the action as the matrix multiplication. In Quantum Field Theory, the representation of Lorentz Group on the basis is always this trivial one, but that on the components can be various. Therefore, we give this representation a name: **field representation**.

.. note:: Just a reminder, although you might not notice, you are actually using the idea of Fibre Bundle. If you would like, try to find some basic tutorial on principal bundle and fibre bundle associated to a principal bundle. And you will then be able to feel the elegance.

Scalar Field
~~~~~~~~~~~~

The scalar field is the field whose field representation is scalar representation. The **scalar representation** is defined as

.. math::


   \varLambda(\phi_i) = \phi_i

which means the components of the field does not change at all under the transformation.

Vector Field
~~~~~~~~~~~~

The vector field is the field whose field representation is vector representation. Thus, the components transform as

.. math::


   \varLambda(A_i) = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}{\}_i}^jA_j

.. note:: To understand the above equation, you need `Basic Group Theory <./bg_liegp.html>`__ and `Representation of Lorentz Group <./repr_lg.html>`__.

First let's examine the above expression. First, you have to recall what is the exponential map. Remember that the result of the exponential map (:math:`\exp\{...\}`) is a matrix, and thus :math:`\exp\{...{\}_i}^j\phi_j` is nothing but a matrix multiply a column vector.

Next, remember that we have said the transformation of the basis follows the trivial representation which is defined just as the matrix product

.. math::


   \varLambda(e_i) = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}{\}_i}^je_j

Therefore we have

.. math::


   A = \varLambda^{-1}(A^i)\cdot\varLambda(e_i) = A^i \exp\{\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}{\}_i}^j \cdot \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}{\}_j}^k e_k = A^j\cdot e_j

Now you can see why we write a dot :math:`\cdot` between the components and the basis --- under vector representation (where some triviality applies), the :math:`\cdot` in the above derivation can be "viewed" as the matrix product. However, this "view" will fail in some other non-trivial situations --- as described any minute next.

Spinor Field
~~~~~~~~~~~~

The spinor field is the field whose field representation is spinor representation. The **spinor representation** is define as

.. math::


   \varLambda(\psi_i) = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}S_{ab}{\}_i}^j\psi_j, \ \ \text{where}\ \ \varLambda = \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}\}

Just like what we have done in the previous section, write down explicitly

.. math::


   A^i \exp\{\frac{1}{2}\mathrm{i}\epsilon^{ab}S_{ab}{\}_i}^j \cdot \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}{\}_j}^k e_k =  A^j\cdot e_j ???

We see that the parameters :math:`\epsilon^{ab}` are the same in the two sides of “\ :math:`\cdot`\ ”, but the "basis" is different. Thus, if we still view :math:`\cdot` as the matrix product, the equality will no longer hold.

Hence, we need a new definition in this case, which means under the new product, there is

.. math::


   \exp\{\frac{1}{2}\mathrm{i}\epsilon^{ab}S_{ab}\} \cdot \exp\{-\frac{1}{2}\mathrm{i}\epsilon^{ab}L_{ab}\} \rightarrow \text{identity matrix}

In Fibre Bundle theory, we achieve this by introducing an equivalence class. Yes, it looks like that we are "brute-forcely" identify the the above result as an identity matrix. But as a matter of fact, there is no preliminary intentions to make :math:`\cdot` here as a product --- it just looks like that in vector field. In Fibre Bundle theory, fields of all kinds are described universally using the equivalence class.

Tensor Field
~~~~~~~~~~~~

The tensor of order :math:`n` is nothing but a quantity :math:`T_{\mu_1\cdots \mu_n}` of :math:`n` indices with each of them transforming like the vector. For instance, if you put two vectors :math:`A_\mu` and :math:`B_\nu` together, i.e. :math:`A_\mu B_\nu`, the result will be a tensor.

.. note:: Actually it is a tough decision for me to write down the above "non-sense". Yes, rigorously speaking, the above descriptions are total non-sense --- but they appear in many textbooks. In fact, there is no indices which are able to "transform like vector", and there is no way to "put vectors together" (It has its name --- tensor product!). Unfortunately it will make our introduction to QFT too cumbersome so we decide not to cover Tensor Analysis. However! You are strongly suggested to try your best to cover that --- it is as essential, and beautiful, and powerful as any other wonderful theories you met before.

Although we do not cover Tensor Analysis, we will provide a list for you to determine whether you have mastered it.

    -  Tensor of type :math:`(k, l)` is a multi-linear map from the Cartesian product of :math:`k` dual vector spaces and :math:`l` vector spaces.
    -  The tensor product of a tensor of type :math:`(k, l)` and a tensor of type :math:`(k', l')` is a tensor of type :math:`(k+k', l+l')`.
    -  The dimension of the space of tensor of type :math:`(k, l)` is :math:`n^{(k+l)}`, where :math:`n` is the dimension of the vector space in the definition of the tensor.
    -  The act of the tensor on a vector (or dual vector) is equivalent to the composite of tensor product and tensor contraction.

You should be able to understand in detail the above statements before you can say you have mastered Tensor Analysis.

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

Maxwell’s Equations
-------------------

This is only a summary of the Maxwell’s equations under the language of Differential Geometry. There is no intention to introduce in detail — you are expected to cover them in your Electrodynamics courses.

First, we have the electromagnetic tensor :math:`F_{\mu\nu}` satisfying

.. math::


   E_i = F_{0i}, \ \ \ \ \ B_i = -\frac{1}{2}\varepsilon_{ijk}F^{jk}

The Maxwell’s equations can be expressed using :math:`F_{\mu\nu}` as

.. math::


   \partial^\mu &F_{\mu\nu} = 0\\
   \partial_{[\mu} &F_{\rho\sigma]} = 0

You can verify that the above equations indeed imply the ordinary form of Maxwell’s equation. The second equality should imply that the tensor :math:`F_{\mu\nu}` can be expressed as

.. math::


   F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu

where :math:`A_\mu` is a “vector” (dual vector or 1-form to be precise). It is easily identified that :math:`A_\mu` represents the electromagnetic potential. With the above construction, the second equation of the Maxwell’s equations automatically holds, and hence the Maxwell’s equations is reduced to

.. math::


   \partial^\mu F_{\mu\nu} = 0

It is easily verified that the Lagrangian of the electromagnetic field is

.. math::


   \mathcal{L} = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu}

If you find any of the above content unfamiliar, please find and review a textbook about Electrodynamics, and make sure you have fully understood all the contents before proceeding.

Quantum Mechanics
-----------------

Well, we have no intentions to go over much about Quantum Mechanics. You are supposed to master the basics of Quantum Mechanics before continuing.

Beginning this section, we will gradually step into the path integral approach to a quantum theory. As all our contemporaries, we start from the path integral formalism of Quantum Mechanics, and then transit to Quantum Field Theory.

To make sure that you are fully prepared, please review the following list and see if you can identify all of them

    -  Schrodinger Equation (Time Dependent and Time Independent)
    -  Typical Solutions of Schrodinger Equation (e.g. harmonic oscillators)
    -  States, observables, and their implementations (Hilbert space and operators) and interpretations (e.g. expectation values).
    -  Dirac Notation
    -  The three pictures of Quantum Mechanics, and their relationships.

Path Integral and Propagator
----------------------------

.. note:: This section requires knowledge on Green's function. Although we will briefly review some basics, you are still suggested to pick up a textbook on Mathematical Methods of Physics for a careful review.

In this section, you will make your first acquaintance with path integral. In quantum theory, path integral is a method of constructing the **propagator**. So we begin with the propagator.

Schrödinger’s Equation and Propagator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning:: The symbols invoked in this section (e.g. :math:`\psi`) have a dedicated meaning, which will be different from other sections in this project.

First, we need to recall **Green's function**. Mathematically, Green's function :math:`G(x;x')` of an operator :math:`L` is defined as

.. math::


   LG(x;x') = \delta(x;x')

This method is very useful to solve equations like

.. math::


   L\varphi(x) = J(x)

since if we know the Green's function :math:`G(x;x')` of :math:`L`, the solution is simply

.. math::


   \varphi(x) = \int G(x;x') J(x')\,\mathrm{d}x'

One can easily verify if notice

.. math::


   L\varphi(x) &= L\int G(x;x') J(x')\,\mathrm{d}x' \\
   &= \int LG(x;x') J(x')\,\mathrm{d}x' = \int \delta(x;x') J(x')\,\mathrm{d}x' = J(x)

where the second equality is due to the fact that :math:`L` consists only operation on :math:`x` and is totally irrelevant to :math:`x'`.

In Quantum Mechanics, we have the Schrödinger’s equation

.. math::


   \left[\mathrm{i}\frac{\partial}{\partial t} + \frac{1}{2m}\nabla^2\right]|\psi\rangle = 0

All within the bracket can be viewed as an operator, and thus possesses a Green's function

.. math::


   \left[\mathrm{i}\frac{\partial}{\partial t} + \frac{1}{2m}\nabla^2\right]K(t,x;t',x') = \delta(x;x')\delta(t;t')

With this propagator, we can calculate the state of anytime after from an initial state

.. math::


   |\psi(t')\rangle = \int K(x,t;x',t')|\psi(t)\rangle\mathrm{d}x\mathrm{d}t

Therefore, the initial state :math:`|\psi(t)\rangle` *propagates* to the final state :math:`|\psi(t')\rangle` with the help of :math:`K(x,t;x',t')`. As a consequence, :math:`K(x,t;x',t')` is called the **propagator**.

Path Integral
~~~~~~~~~~~~~

The previous argument is only one way to construct Quantum Mechanics, i.e. suppose the Schrödinger equation holds -> derivation of the propagator. In 1948, Feynman proposed another way of reasoning: path integral -> propagator -> Schrödinger equation.

Feynman suggest the propagator takes the form

.. math::


   K = \int \mathcal{D}x \exp\{\mathrm{i}S[x]\}

.. note:: Rigorously speaking, we should use :math:`\propto` instead of :math:`=` in the above equation, since the RHS may produce annoying constant factors. However, this factor can be eliminated through normalisation. Therefore, all the subsequent path integral will automatically carry this normalisation process.

where :math:`S[x]` is the action of the system, and :math:`\int\mathcal{D}x` is the so-called path integral. Next, we carefully examine the above equation.

Take 1D free particle for example. The Lagrangian of 1D free particle is

.. math::


   L = \frac{1}{2}m\dot{x}^2

Thus, the action is

.. math::


   S[x] = \int\mathrm{d}t\,\frac{1}{2}m\dot{x}^2

Suppose we now work on the start point :math:`x, t` and end point :math:`x', t'`. The path integral requires "integrating along all paths". However, the "all path" can be hard to manipulate, since it is something uncountable. More specifically, it should be something like

.. math::


   \int [...]\mathrm{d}[x(t_1)]\int [...]\mathrm{d}[x(t_2)]\int [...]\mathrm{d}[x(t_3)]...

where every point within interval :math:`(t,t')` needs an integration. This is clearly impossible since there are uncountable elements within :math:`(t,t')`. Hence, we come up with the idea of a kind of "sampling".

For an arbitrary large number (:math:`n`) of points within :math:`(t,t')` (the "sample" of :math:`n` points), the following formula

.. math::


   \int [...]\mathrm{d}[x(t_1)] \int [...]\mathrm{d}[x(t_2)] ... \int [...]\mathrm{d}[x(t_n)]

exists, we *define* this result as the integration of all path, i.e. the path integral of :math:`[...]`. The fact that the size of the "sample" can be *arbitrarily* large insures that the integral actually goes over *every path*.

.. note:: The trick to turn some infinite objects to something arbitrary can be very common in Mathematics. For instance, the concept *infinitely large* can be in fact *arbitrarily large* or *no upper bound*. The limit in Mathematics also follows similar idea.

To formally implement this, insert :math:`n` points into :math:`(t,t')` and perform :math:`n` integrations

.. math::


   \prod_{i=1}^{n}\int\exp\{\mathrm{i}\frac{1}{2}m\frac{[x(t_i)-x(t_{i-1})]^2}{\epsilon}\}\mathrm{d}[x(t_i)]

where we also expand the integration in the action into discrete form, and :math:`\epsilon = (t'-t)/(n+1)` is the size of each small interval. Then, ask the "sample size" :math:`n` to go to infinity

.. math::


   \lim_{n\rightarrow\infty}\int C(\epsilon)\prod_{i=1}^{n}\mathrm{d}[x(t_i)]\exp\{\mathrm{i}\sum_{i=1}^{n+1}\frac{1}{2}m\frac{[x(t_i)-x(t_{i-1})]^2}{\epsilon}\}

where we also adjust the order and introduce a normalisation factor :math:`C(\epsilon)` to ensure the convergence. You should be able to prove this adjustment once notice that all :math:`x(t_i)` are independent variables. The above formula is the definition of the path integral

.. math::


   \int\mathcal{D}x\exp\{\mathrm{i}\int\mathrm{d}t\frac{1}{2}m\dot{x}\}

As a practice, you should try to write down the definition of a general path integral

.. math::


   \int\mathcal{D}x\exp\{\mathrm{i}\int\mathrm{d}t L\}

You may find the above elucidation hard to comprehend. That's normal. Try to draw some diagrams or analyse step by step. It might help.

Evaluation of Path Integral
---------------------------

This section will tell you how to explicitly calculate the propagator using path integral. Take the free particle for example (you should try to generalise the calculation into other situations). The propagator of the free particle is

.. math::


   K = \lim_{n\rightarrow\infty}\int C(\epsilon)\prod_{i=1}^{n}\mathrm{d}[x(t_i)]\exp\{\mathrm{i}\sum_{i=1}^{n+1}\frac{1}{2}m\frac{[x(t_i)-x(t_{i-1})]^2}{\epsilon}\} 

To simplify the expression, denote :math:`x_i\equiv x(t_i)` and let :math:`m=2`. As a result, the integral simplifies to

.. math::


   K = \lim_{n\rightarrow\infty}\int C(\epsilon)\prod_{i=1}^{n}\mathrm{d}x_i\exp\{\mathrm{i}\sum_{i=1}^{n+1}\frac{(x_i-x_{i-1})^2}{\epsilon}\} 

Before trying to actually evaluate the above expression, we should first find out the normalisation factor :math:`C(\epsilon)`.

Determination of Normalisation Factor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The normalisation factor can be constrained under the infinitesimal evolvement. Suppose we now work on the interval :math:`(t, t+\epsilon)` where :math:`\epsilon` is an infinitesimal time step. Therefore, the normalisation condition requires

.. math::


   K(t; t+\epsilon) = \int c\,\mathrm{d}y \exp\{-\frac{(y-x)^2}{\mathrm{i}\epsilon}\} = 1

where :math:`y` is the position at :math:`t+\epsilon` and :math:`x` is the position at :math:`t`. Perform the integration and we get

.. math::


   c\cdot \sqrt{\mathrm{i}\pi\epsilon} = 1 \ \ \Rightarrow\ \ c = \frac{1}{\sqrt{\mathrm{i}\pi\epsilon}}

This normalisation factor emerges whenever we the time moves forward the amount :math:`\epsilon`. In our previous expression, we insert :math:`n` point into the interval :math:`(t,t')` which means we move forward :math:`n+1` steps. Therefore

.. math::


   C(\epsilon) = c^{n+1} = (\sqrt{\mathrm{i}\pi\epsilon})^{-n-1}

The normalisation factor of the other forms of Lagrangian can be derived through a similar way.

Expand according to Classical Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually, the path integral will have an upper and lower boundary, i.e. :math:`x'` and :math:`x_0`, which brings some trouble during the evaluation. Hence, we want to eliminate this trouble. The best way is to introduce a *relative* variable, i.e. select a certain path :math:`x_c` with :math:`x_c(t_0) = x_0` and :math:`x_c(t') = x'` and perform the path integral according to :math:`y\equiv x - x_c`. Of course, you can choose whatever path :math:`x_c` you like, but there is one path that will make the evaluation less miserable --- the classical path.

According to the variation principle, the classical path is defined as the path which satisfies

.. math::


   \left.\frac{\delta S}{\delta x}\right|_{x=x_c} = 0

Expand the action according to the classical path and we get

.. math::


   S = S_c + \left.\frac{\delta S}{\delta x}\right|_{x=x_c} y + \left.\frac{\delta^2 S}{\delta x^2}\right|_{x=x_c}y^2

This is nothing but a functional version of Taylor expansion. The expansion ends at second order since for most systems, the Lagrangian is quadratic. It is clear that the second term is zero. For the third term, it is exactly the same as :math:`S_c` for free particle situation. Therefore, we separate the action into the addition of a classical action and an action of :math:`y` which satisfies :math:`y_0 = y' = 0`.

.. note:: The above derivation will invoke functional Taylor expansion. If you can not yet accept this, it won't be miserable just to substitute :math:`x = x_c + y` into the original path integral and get the same result.

Evaluation by Quadratic Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Our path integral now becomes

.. math::


   K = K_c \cdot \lim_{n\rightarrow\infty}\int (\sqrt{\mathrm{i}\pi\epsilon})^{-n-1}\prod_{i=1}^{n}\mathrm{d}y_i\exp\{\mathrm{i}\sum_{i=1}^{n+1}\frac{(y_i-y_{i-1})^2}{\epsilon}\} 

where

.. math::


   K_c = \exp\{\mathrm{i}S_c\}

is the "classical" part of the propagator.

A naive way of evaluating this integral is to follow the definition --- perform :math:`n` integration and then take the limit. However, recall that most of the physical models, the Lagrangian is quadratic. This provides another way of evaluating the path integral, which brings much ease.

To begin with, expand the summation

.. math::


   &y_1^2 + y_1^2 - 2y_1y_2 + y_2^2 + y_2^2 - 2y_2 y_3 + y_3^2 + ...\\
   =\ &2y_1^2 - y_1y_2 - y_1y_2 + 2y_2^2 - 2y_2 y_3 - 2y_2 y_3 + ...

The reason for a rearrangement of the terms can be seen if we write the expansion in matrix form

.. math::


   [y_1\ y_2\ y_3 \ldots y_n]
   \left[
   \begin{matrix}
   2 & -1 &  &  & & \\
   -1 & 2 & -1 &  & & \\
   & -1 & 2 & & & \\
   & & & \ddots & & \\
   & & & & & -1\\
   & & & & -1 & 2
   \end{matrix}
   \right]
   \left[
   \begin{matrix}
   y_1\\
   y_2\\
   y_3\\
   \vdots\\
   y_n\\
   \end{matrix}
   \right]
   \equiv \eta^T M \eta

where :math:`\eta` is an :math:`n`-dim vector and :math:`M` is the matrix in the middle. Therefore, the integral becomes

.. math::


   \lim_{n\rightarrow\infty}(\sqrt{\mathrm{i}\pi\epsilon})^{-n-1}\int \mathrm{d}\eta\exp\{-\eta^T A \eta\} 

where :math:`\mathrm d\eta` is just the abbreviation of :math:`\prod\mathrm dy` and :math:`A\equiv M/\mathrm i\epsilon`.

.. note:: It is a fairly common thing to transform something with multiple summation into the matrix form. You are suggested to have the vigilance about the summation which is possible to be transformed to matrix form since it may bring surprising extra clearance.

The integral is nothing other than a multi-dimensional Gaussian integral. We will directly invoke the result of the integral as there have been numerous materials on how to do the multi-dimensional Gaussian integral online. The result is

.. math::


   \int \mathrm{d}\eta\exp\{-\eta^T A \eta\} = \sqrt{\frac{\pi^n}{\det(A)_n}}

This inspires us to calculate the determinant of the matrix :math:`M` (and thus matrix :math:`A`). To do this, expand the determinant along the first row and we get the following recurrence relation

.. math::


   \det(M)_{n+1} = 2\det(M)_n - \det(M)_{n-1}

It is easy to see that this recurrence relation implies that the sequence :math:`\det(M)_n` is actually a arithmetic sequence. Therefore, an evaluation of the first two elements of the sequence will bring you

.. math::


   \det(M)_n = n+1

Thus

.. math::


   \det(A)_n = \det(M/\mathrm i\epsilon)_n = (n+1)/(\mathrm i\epsilon)^n

with which the integral is evaluated

.. math::


   \int \mathrm{d}\eta\exp\{-\eta^T A \eta\} = \sqrt{\frac{(\mathrm i\epsilon\pi)^n}{n+1}}

Combine with the other factors and we have

.. math::


   K = K_c\cdot\lim_{n\rightarrow\infty}(\sqrt{\mathrm{i}\pi\epsilon})^{-n-1}\sqrt{\frac{(\mathrm i\epsilon\pi)^n}{n+1}} = K_c\cdot\lim_{n\rightarrow\infty}\sqrt{\frac{1}{\mathrm i\pi\epsilon(n+1)}} 

Now, an important thing to notice is that :math:`\epsilon(n+1)` is actually :math:`\Delta t = t'-t_0`. Thus, we have the final formula of the propagator

.. math::


   K = \frac{1}{\sqrt{\mathrm i\pi\Delta t}}\exp\{\mathrm iS_c\}

You are suggested to explicitly calculate the classical action :math:`S_c` (notice that the classical path of a free particle is just a straight line) and compare this result with the one you may encounter in your previous Quantum Mechanics course.

Originally, we stop here. However, you might be pretty surprised about our later contexts if we do so. Hence, ... we decide to surprise you now.

    The modern path integral formalism of quantum theory has NOTHING to do with doing the path integral.

Yes, this is true and IMPORTANT. To make this less surprising, recall that we do not do the actual integral of the action in the Lagrangian formalism. Instead, we try to **transform the integration problem into differentiation problem**. So the existence of this section is nothing but to convince you that the integral truly exists and is well-defined.

Please do not feel to be cheated. Whenever you feel doubtful about our following derivation about the path integral, please remember to come here again to gain some confidence.

Path Integral of Fields
-----------------------

In previous sections, path integral in Quantum Mechanics has been constructed and evaluated. So we are now sure that the path integral for particles can be well-defined. Thus, to construct Quantum Field Theory, all we need to do is to construct the path integral of physical fields.

However, this is not something direct and intuitive. As is shown in previous sections, the object to be integrated in Quantum Mechanics, namely :math:`x(t)` has only one parameter :math:`t`, i.e. it is 1-dimensional. However, we now need to work on fields :math:`\Phi(x)` where :math:`x` is 4-dimensional (and probably :math:`d`-dimensional in the future). This can cause the functional determinant to be divergent and the path integral will go to zero after taking the limit.

.. note:: There is no intention to demonstrate explicitly how the determinant goes divergent. But it won't be much too complicated just to simply repeat the evaluation process shown in the previous section for, say, 2D field and see its divergence.

In this case, methods must be addressed to solve the divergent problem. A straight-forward way is to reduce the path integral of field with multi-dimensional parameters to products of that in 1-dimensional, which is a solved problem. To achieve this, define the path integral of fields as (take 2-dim for example)

.. math::


   W &= \int \mathcal{D}\Phi(x,y)\exp\{\mathrm{i}S[\Phi, \partial_\mu\Phi\} \\
   &= \int \mathcal{D}\Phi_x(y)\exp\{\mathrm{i}S[\Phi, \partial_y\Phi\}\int \mathcal{D}\Phi_y(x)\exp\{\mathrm{i}S[\Phi, \partial_x\Phi\}

.. note:: The second example of `Function and Image Element <./ms_func_img.html>`__ will be helpful for understanding the above expression.

Hence, now the path integral will become the product of two path integrals with finite result. However, this path integral can be different from the *intuitive one*. How can we say that this *new* path integral will hold for our initial idea about the path integral? Well, please recall that we have mentioned at the end of the previous section that the path integral formalism pragmatically has nothing to do with the actual path integral. The only purpose of this section is to **demonstrate that the path integral can be finite**. As for how the path integral is used in Quantum Field Theory, well, keep going, and you will understand.

Sketch of Path Integral Formalism
---------------------------------

Before we step into the path integral formalism, we give an overall sketch as well as some *rules* of our construction here. Beware, that the *rules* are not necessarily accepted or respected by all the academics.

Sketch of Theoretical Construction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The construction will start from analyzing the general path integral of scalar field from some *stable state* to itself (usually it is *vacuum state* :math:`|\Omega\rangle`)

.. math::


   \langle \Omega|\Omega\rangle = N\int\mathcal{D}\varphi\exp\{-\frac{1}{2}\mathrm{i}\int\varphi[\partial^2-m^2]\varphi\} = 1

where :math:`N` is a normalization factor. The last equality comes from the property *stable*, which means it will not change under the situation of free field, which will determine the normalization factor. Now, we construct a quantity called **generating functional** by adding an arbitrary *potential* :math:`J`

    **Stage 1**

    .. math::


       W_0[J] = \langle\Omega|\Omega\rangle |_J &= N\int\mathcal{D}\varphi\exp\{-\mathrm{i}\int\frac{1}{2}\varphi[\partial^2-m^2]\varphi - J\varphi\}\\
       &= \exp\{-\frac{1}{2}\mathrm{i}\int J\Delta_FJ\}

The above generating functional includes merely the scalar field without any other *actual* interaction terms (the :math:`J` term is an auxiliary term with no physical significance). If the Lagrangian includes the interaction terms :math:`\mathcal{L}_{\text{int}}`, the generating functional will be

    **Stage 2**

    .. math::


       W[J] &= \exp\{-\mathrm{i}\int\mathcal{L}_{\text{int}}\!\!\left[\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J}\right]\} W_0[J] \\
       &= \exp\{-\mathrm{i}\int\mathcal{L}_{\text{int}}\!\!\left[\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J}\right]\}\exp\{-\frac{1}{2}\mathrm{i}\int J\Delta_FJ\}

As is indicated, this expression deals with some *stable state*. Now we hope to generalized it into other ordinary states, like from state :math:`\alpha` to state :math:`\beta`. This forms the well-renowned **S-matrix** (scattering matrix)

    **Stage 3**

    .. math::


       S = \langle \beta|\alpha\rangle = S[J]|_{J=0} = \left.\exp\{\mathrm{i}\int\varphi_{\text{as}}(\partial^2 - m^2)\frac{\delta}{\delta J}\}W[J]\right|_{J=0}

where :math:`\varphi_{\text{as}}` is the asymptotic field corresponding to the initial and final state. The last equality is the famous **LSZ reduction formula**.

The theoretical construction will end at S-matrix. For a connection with the experiment, scattering **cross-section** can be derived through the S-matrix, which is directly measurable in the scattering experiment.

Some Rules
~~~~~~~~~~

It has been `stated before <./intro_why.html>`__ that we will not introduce any contents from canonical quantization into our construction of the path integral formalism. Therefore, actually we are not able to have concepts like *state* which is widely used in quantum theory. In this case, we *have to* use some configuration of fields as *state* (like asymptotic field). But this would imply that there must be some subtle identical relationship between field and state, which is somehow rejected by canonical quantum field theory.

As a matter of fact, the problem caused by the lack of field operator and successive state only arises when constructing S-matrix, which means that stage 1 and stage 2 will not be affected anyway. In our philosophy, the path integral formalism, as a parallel companion of canonical quantization, should be *free* from the concepts in canonical form. Therefore, we will try our best not to invoke concepts like field operator and the corresponding state, or at least push them as *later* as possible.

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

Correlation Function
--------------------

In both stage 2 and stage 3, we will encounter the following functional derivative

.. math::


   \tau(x_1,\ldots,x_n) := \left.\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J(x_1)}\cdots\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J(x_n)}W_0[J]\right|_{J=0}

Thus, we give this quantity a name **correlation function**, or :math:`n`\ **-point (Green's) function**. The origin of this name comes from the similarity of its formulation in canonical quantization and hence this name may look strange here.

It is not so straight-forward about the :math:`n`-point function, and thus we hope to reduce the formula. To do this, let us first evaluate the 2-point function

.. math::


   \tau(x_1,x_2) &= \left.\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J(x_1)}\frac{1}{\mathrm{i}}\!\frac{\delta}{\delta J(x_2)}\exp\{-\frac{1}{2}\mathrm i\!\!\int\!\! J\Delta_FJ\}\right|_{J=0} \\
   &= \left.\mathrm{i}\frac{\delta}{\delta J(x_1)}\int\!\!\Delta_F(x_2;)J\exp\{-\frac{1}{2}\mathrm i\!\!\int \!\!J\Delta_FJ\}\right|_{J=0}\\
   &=\left.\mathrm i\Delta_F(x_1;x_2)W_0[J]\right|_{J=0} + \left.(\int\Delta_F J)^2W_0[J]\right|_{J=0} = \mathrm i\Delta_F(x_1;x_2)

It is nothing other than :math:`\mathrm{i}` times the ordinary Green's function. Next, 3-point function

.. math::


   \tau(x_1,x_2,x_3)\sim \left.\Delta_F\int\Delta_FJ\right|_{J=0} + \left.(\int\Delta_FJ)^3\right|_{J=0} = 0

And 4-point function

.. math::


   \tau(x_1,x_2.x_3,x_4) &= \mathrm{i}\Delta_F(x_1;x_2)\mathrm{i}\Delta_F(x_3;x_4)\\
   &+ \mathrm{i}\Delta_F(x_1;x_3)\mathrm{i}\Delta_F(x_2;x_4) \\
   &+ \mathrm{i}\Delta_F(x_2;x_3)\mathrm{i}\Delta_F(x_1;x_4)\\
   &= (1\sim2)(3\sim4) + (1\sim3)(2\sim4) + (2\sim3)(1\sim4)

where we have used :math:`(1\sim2)` to represent :math:`\tau(x_1,x_2)`. Therefore, we can see the regularity --- the :math:`n`-point function is either :math:`0` or some combination of two point functions. Specifically, we have by induction

-  The odd-point function is :math:`0`.
-  The even-point function is

.. math::


   \tau(x_1,\ldots, x_{2n}) = \sum_{\text{perms}}(p_1\sim p_2)\ldots(p_{2n-1}\sim p_{2n})

which means the summation over all the permutations :math:`p`. This is the so-called **Wick's Theorem** --- transforming the :math:`n`-point function into the combination of 2-point function.

You are suggested to show yourself that the S-matrix can be written using correlation function as

.. math::


   S = \sum_{n=0}^\infty\frac{\mathrm i^n}{n!}\prod_x\varphi(x)\prod_x(\partial^2\!\!-\!m^2)\tau(x_1,\ldots,x_n)

where :math:`x` takes over :math:`x_1,\ldots,x_n`. This formula is the so-called **perturbative expansion** of the S-matrix.

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

Function and Image Element
--------------------------

This section is fairly important --- it introduces some important concepts in ... functions. Alright, we just want to tell you that the function and its image elements are not the same thing. Well, you may find this ostensible. However, the denotations of function and its image elements can be really misleading. You may clearly identify that something like :math:`f` and :math:`f(x_0)` are different things. But can you always notice that :math:`f` and :math:`f(x)` are different things, especially when :math:`x` is some *variable* instead of *constant* like :math:`x_0`?

There are no intentions to detailedly discuss the issue, since it will finally becomes a philosophical war between objective and formal Mathematics. Here, we directly take the view of objective Mathematics. Under this philosophy, the function :math:`f` is a mathematical object which is a subset of the Cartesian product of domain and image (satisfying some conditions); while :math:`f(x)` is an element of image (no matter whether :math:`x` is a constant or not). Therefore, they are *essentially* different objects.

To help understand this, especially the differences it causes in Quantum Field Theory, we set up the following examples

    **Example 1.** In Lagrangian formalism and Path Integral Formalism respectively, two kinds of functional derivatives are invoked --- :math:`\delta/\delta f` and :math:`\delta/\delta f(x)`. The former is the derivative with respect to the function :math:`f`, and the latter is the derivative with respect to the element :math:`f(x)`. You will see in that it is the definition of the latter one which causes the famous infinity problem in Quantum Field Theory; while nothing happens to the former one.

    **Example 2.** In some cases, we will write something like

    .. math::


       f_x(y)=f(x,y)

    Although there is a equality sign in the equation, there are essential difference between :math:`f_x` and :math:`f` --- the former is a family of functions of :math:`y` (labelled by :math:`x`) and the latter is a function of two variable :math:`x` and :math:`y`. The equality essentially means solely that the *value* is the same.

Functional Derivative
---------------------

The functional derivative we talk about here is not the same as the variation used widely in Lagrangian formalism --- although they look so much alike formally. To make sure you will not mistake them, we first illustrate what is the variation of a functional.

The variation of a functional :math:`F[\phi]` whose domain is a Banach space :math:`B` (a linear space where you can talk about the "length" --- norm of its element) is usually implemented as **Gâteaux derivative**

.. math::


   \frac{\delta F[\phi]}{\delta\phi} := (\forall \eta) :: \lim_{\varepsilon\rightarrow 0}\frac{F[\phi+\varepsilon\eta]-F[\phi]}{\varepsilon}

which very much resembles the directional derivative in ordinary Calculus. Please notice that the :math:`\eta` here is just an arbitrary element of the Banach space, and in its application it is any physical field.

The variation is the "derivative" of the argument :math:`\phi` itself, without any designation of it value at some point :math:`\phi(x)`; while functional derivative is defined differently. The functional derivative of :math:`F[\phi(x)]` with respect to **value** :math:`\phi(y)` is

.. math::


   \frac{\delta F[\phi(x)]}{\delta\phi(y)} = \lim_{\varepsilon\rightarrow 0}\frac{F[\phi(x)+\varepsilon\delta(x;y)]-F[\phi(x)]}{\varepsilon}

Therefore, you shall now see the differences between the variation and the functional derivative --- the variation performs "derivative" on :math:`\phi` itself, while the functional derivative does so on the value :math:`\phi(y)`. And thus a delta function has to be invoked to deal with the different points :math:`x` and :math:`y`. You will see in chapter Quantum Theory that it is this delta function which brings the infinities into the S-matrix.

Geometric Unit System
---------------------

This is an introduction to the geometric unit used widely in the theoretical contexts of Physics.

In Physics, there are many important constants, such as light speed in vacuum :math:`c`, (reduced) Plank constant :math:`\hbar`, absolute permittivity :math:`\varepsilon_0`, etc. If we include all these constants in an equation, the expression can be cumbersome. To solve this problem, the simplest way is to introduce the following convention

.. math::


   c=1,\ \ \ \ \ \hbar=1

Therefore, all multiplication of these constants in the equation will disappear. But wait! You may immediately notice a problem: the dimension! Yes, it seems that the above equation violates a fundamental requirement — balance of dimension. The left hand side is a physical constant with dimension, but the right hand side is a pure number.

Well, this in fact does not matter so much. You can view it as a redefinition of units. For example, to make light speed :math:`c=1`, all we need to do is to redefine the time unit as the time within which light travels a unit length. This is called **Geometric Unit System**. As a result, the convention :math:`c=1` will be equivalent to :math:`[L]=[T]`, where :math:`[L]` stands for the length dimension and :math:`[T]` for time dimension. Similarly, it is easy to figure out that :math:`\hbar=1` leads to :math:`[L]=[M]^{-1}`.

Hope you get the point. Now you should not feel unfamiliar with sentences like “momentum has a dimension of :math:`[L]^{-1}`\ ”. The theory of dimension analysis guarantees that there will not be a problem with this convention as long as you do a correct calculation.

Einstein Summation Convention
-----------------------------

This is an introduction to the Einstein summation convention used widely in the theoretical contexts in Physics.

The definition of the convention is simple: repeating upper and lower indices implies summation, unless stated otherwise, i.e.

.. math::


   x^iy_i = \sum_{i\in I}x^iy_i

where set :math:`I` is the set of possible values of the indices.

Please notice that there are other versions of Einstein summation convention. One version may consider all the dummy indices as summation. However, in this context, only the repeated upper and lower indices should be interpreted as summation, expression as :math:`x_iy_i` does not apply to the summation convention.

Basic Differential Geometry
---------------------------

Differential Geometry can be one of the most crucial foundations of theoretical Physics. Thus, we suggest everyone who aims at fundamental theoretical Physics to have a detailed review of Differential Geometry. We are not going to introduce thoroughly here, since that would make up another book. You can rely on this if you just want to understand our main context, nevertheless, you are strongly suggested to look for other Differential Geometry introductory for many other important details.

Get Started: Motivation
~~~~~~~~~~~~~~~~~~~~~~~

In Calculus, we have studied many properties of functions, like continuity, differentiability and so on. However, these properties only apply to functions — whose domain is a number set (such as :math:`\mathbb R^n`). However, pragmatically we are dealing with ordinary maps — whose domain is an ordinary set (ranging from all particles of the desk in front of you to the spacetime of the universe). At this time, we find that we are lack of the structure (just like a kind of property) on that ordinary set. For example, you can not judge whether a map from the phone to its number is differentiable or not. Hence, extra structures are needed.

How does this related to Physics? You may consider the electric potential :math:`\phi` which is a vector field in spacetime. The vector field is nothing but a map from the set of all points in spacetime to the real number set. And the set of all points in spacetime can be an example of the *ordinary set* in our previous illustration.

Prerequisites: Topology
~~~~~~~~~~~~~~~~~~~~~~~

The first structure we need is the topology. The topology of a set will help us define the continuity of the map. In Calculus, a function is continuous if the inverse image of any of the open interval in the image will be an open interval (You can prove that this is equivalent to the :math:`\varepsilon`-:math:`\delta` form in Calculus). Thus, if we want to define continuity of any map, the only structure we need is to define the “open interval” of the set.

This inspires us to manually designate some subsets of the set to be **open** (plus some conditions). And the continuity of the map can be defined in similar way. We are not going to expand here — it can be a long story. The only thing you need to remember is that we can now talk about the openness of the subset and the continuity of a map.

Set up a Coordinate System
~~~~~~~~~~~~~~~~~~~~~~~~~~

Next we move on to the differentiability of a map. To do this, we equip every open subset with an open subset of a number set. To be more specific, construct a continuous bijection :math:`\psi_\alpha` for each subset :math:`U_\alpha` of set :math:`M` to an open subset of :math:`\mathbb R^n`.

To see how this works, let’s look at map :math:`\psi_\alpha`. It maps the point :math:`p` of set :math:`M` into :math:`n` numbers in :math:`\mathbb R^n`. Or equivalently, it assigns :math:`n` numbers to point :math:`p`. Yes! Those numbers are nothing other than the **coordinates** of point :math:`p`. And, map :math:`\psi_\alpha` will then be the **coordinate system** on subset :math:`U_\alpha`. Set equipped with the coordinate system is called manifold.

Now, we can define the differentiability of the map between manifolds. Since every point has its coordinates, the map between points becomes functions between coordinates. Thus, the differentiability of the map can be defined as that of those functions, which is well-defined in Calculus.

Another thing that we would like to mention is the separation of point and its coordinates. In many elementary Physics textbooks, point and coordinates are the *same thing*. But now, we strongly suggest to distinguish these two entities — you will benefit a lot if you take this seriously in the future.

Spacetime Geometry
~~~~~~~~~~~~~~~~~~

Here, we introduce briefly (*extremely briefly*) about the spacetime geometry. In fact, there is a spectacular construction of spacetime geometry in Differential Geometry theory. So if you are able, try to learn something about it. You will never regret.

In 3 dimensional Euclidean space, we have Gougu Theorem

.. math::


   \Delta s^2 = \Delta x^2 + \Delta y^2 + \Delta z^2

In differential form, it is

.. math::


   \mathrm d s^2 = \mathrm d x^2 + \mathrm d y^2 + \mathrm d z^2

Symbol :math:`\mathrm d s^2` here is called **line element**. You may notice that the coefficients of the three terms in right hand side are all :math:`1`. This is a typical characteristic of flat 3D Euclidean space. Now we think: what if the coefficients are not :math:`1`? In fact, the configuration of those coefficients labels a kind of *geometry*. As an important example, look at

.. math::


   \mathrm d s^2 = -\mathrm d t^2 + \mathrm d x^2 + \mathrm d y^2 + \mathrm d z^2

Clearly this is not the 4D Euclidean space, since there is a :math:`-1` here. Actually, this is **Minkowski spacetime** widely used in Special Relativity and Quantum Field Theory. You can also write other numbers or even functions for those coefficients. Certain functions will even let the spacetime to curve. But these are the content of General Relativity which we do not aim at here. (Again if you have time, take a look at it. It’s wonderful.)

We can write the Minkowski line element formally as

.. math::


   \mathrm d s^2 = [\mathrm d t\ \mathrm d x\ \mathrm d y\ \mathrm d z]
   \left[
   \begin{matrix}
   -1 & 0 & 0 & 0\\
   0 & 1 & 0 & 0\\
   0 & 0 & 1 & 0\\
   0 & 0 & 0 & 1
   \end{matrix}
   \right]
   \left[
   \begin{matrix}
   \mathrm d t\\
   \mathrm d x\\
   \mathrm d y\\
   \mathrm d z\\
   \end{matrix}
   \right]

The :math:`4\times 4` matrix in the above equation, usually denoted by :math:`\eta_{\mu\nu}`, is called the **metric** of the spacetime. The sum of all the diagonal element (:math:`+2` in this case) is called the **signature** of the metric. Many textbooks of Quantum Field Theory uses Minkowski metric as :math:`\eta = \mathrm{diag}(1,-1,-1,-1)`, whose signature is :math:`-2`. However, to comply with the convention in the Theory of Relativity, we use the :math:`+2` metric.

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

Basic Linear Algebra
--------------------

    There is no intention to introduce Linear Algebra in this section. We have assumed that you have already accomplished training on Linear Algebra. This section serves just as a brief review of the vector space.

The following is the definition of a vector space, or linear space in some references.

    **Definition.** The vector space :math:`V` over field :math:`F` is a set with two binary operation: **addition** :math:`+:V\times V\rightarrow V` and **scalar multiplication** :math:`\cdot:F\times V\rightarrow V` satisfying

    1. Commutativity: :math:`v+u=u+v`

    2. Associativity of addition: :math:`(v+u)+w = v+(u+w)`

    3. Additive identity: :math:`\exists 0, \forall v\in V, 0+v=v+0=v`

    4. Additive inverse: :math:`\exists (-v), v + (-v) = 0`

    5. Associativity of scalar multiplication: :math:`\beta(\alpha v) = (\beta\alpha)v`

    6. Compatibility of addition and scalar multiplication: :math:`(\alpha+\beta)v = \alpha v + \beta v`, :math:`\alpha(v+u) = \alpha v + \alpha u`

    7. Scalar multiplicative identity: :math:`\exists 1, 1\cdot v = v`

There is no need to be so keen on the definition of vector space, but there does exist some important facts worth noticing. From the definition can we discover that the vector space is actually a very general concept --- it would be more appropriate to call it a paradigm. Thus, when facing vector space, one should be very careful to distinguish the general vector space and some specific vector spaces.

As an example, the real number set over real number field with addition and scalar multiplication as the ordinary addition and multiplication of real numbers forms a vector space. In this case, all real numbers are vectors of real number set --- this is somehow different from our previous intuition, since a real number is widely referred as "scalar" instead of a vector.

As another example, the tensor space of any type is a vector space. But in many applicative contexts, the tensor of order one is specifically referred as vector.

The reason for this section is to remind you that there might be multiple meanings corresponding to the term "vector". Thus, sometimes if you find the argument containing "vector" incomprehensible, please remember that there might be the problem of the ambiguity of the term "vector".

Basics of Lie Group Theory
--------------------------

This section is a very basic introduction of Lie Group & Lie Algebra theory. Again, we would like to mention that there Lie Group & Lie Algebra is a tremendously abundant, and this section concerns only tips of the tips. The aim of this introduction is simply to provide you with an overall view of how Lie Group & Lie Algebra is implemented into physical theories. Therefore, we strongly recommend a more detailed investigation on this branch of Mathematics if possible.

Group and Lie Group
~~~~~~~~~~~~~~~~~~~

Group structure is an algebraic structure on a set, namely

    **Definition.** Group :math:`G` is a set equipped with a binary operation **multiplication**: :math:`\cdot: G\times G\rightarrow G` satisfying

    1. Associativity: :math:`(gh)k = g(hk)`

    2. Identity Element: :math:`\exists e, eg = ge = g`

    3. Inverse Element: :math:`\forall g, \exists g^{-1}, gg^{-1} = g^{-1}g =e`

Translate to human language: group is a set; you can perform multiplication of any two element of the set, and the multiplication satisfies three conditions.

The reason to invoke group into Physics lies on its similarity to the symmetry. Take translational symmetry for instance. The three translation operation clearly satisfies the associativity. There exists an identity translation (no translation). And for every translation there exists an inverse operation that transforms everything back. Similar argument also holds for rotation and other symmetries.

But a simple group structure does not provide enough tools for our analysis. We clearly are not satisfied with description as "translation :math:`a`\ ” and "translation :math:`b`\ ”. We hope that we can say "translation of :math:`5` units". How can we do that? You got it! We need a manifold.

Now, **Lie group** debuts. Lie group is nothing more complex than a set that is both a group and a manifold. The manifold provides the coordinates for each of the group element, and we can use a variety of tools provided by Differential Geometry.

Generator and Exponential Map
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of a very important tool provided by the Differential Geometry is the possibility to analyse the group element through generators. Take the 3D translation as an example. With a differential structure in hand, we can express some group element like "translation of 5 units along x axis". Here, the group element is designated by a parameter "5 units" and a *direction* "x axis". The generator is nothing other than the *direction* here. Therefore, every group element can be written as a parameter with a *direction*.

    Mathematically speaking, the generator is the element of the vector space at identity element of the Lie group. If you can not understand the previous statement, a review of linear structure on manifolds will be beneficial. There is no intention to expand here.

Next, we are going to explicitly illustrate how to the generator *generate* the group element. Suppose we now have a infinitesimal transformation

.. math::


   1+\epsilon A

where :math:`1` means the identity element, :math:`\epsilon` is a first order infinitesimal parameter and :math:`A` is the generator. To generate the element :math:`g` with *direction* :math:`A` and parameter :math:`t`, divide :math:`t` by :math:`n` and ask :math:`n\rightarrow\infty`. Therefore, the infinitesimal parameter :math:`\epsilon=t/n`. Then, apply the transformation :math:`n` times to get

.. math::


   g = \lim_{n\rightarrow\infty}(1+\frac{t}{n}A)^n\equiv\exp\{tA\}

Symbol :math:`\equiv` means "denoted by". The expression :math:`\exp\{tA\}` is called the **exponential map** of element :math:`g`. The reason for this denotation will be apparent if you notice a conclusion in Calculus

.. math::


   \exp\{x\} = (1 + \frac{x}{n})^n

It seems that we have got nothing but a denotation. However, the following theorem will show the power of the exponential map

    **Theorem.** For matrix group, thre is :math:`\exp = \mathrm{Exp}`.

In the above theorem, map :math:`\mathrm{Exp}` is defined as

.. math::


   \mathrm{Exp}(tA) = 1 + tA + \frac{t^2A^2}{2!} + \ldots = \sum_{k=0}^{\infty}\frac{t^kA^k}{k!}

and the matrix group means the group with all elements being square matrix. Notice that most group that are of great concern is the matrix group. There is no doubt that this theorem will provide great convenience.

    The trick of expanding the definition of function of real number to function of other object using the Taylor expansion is widely used in Mathematics. Thus, if you see some function that is originally only defined on numbers but actually acts on something else, you should then regard the definition of the function as the corresponding Taylor expansion.

Special Lie Groups
~~~~~~~~~~~~~~~~~~

This section will introduce several crucial matrix Lie groups that are widely used in physical theories. In fact, in frontier research, there are numerous kinds of Lie groups that frequently appear in the theories. This section will only introduce two of them --- **orthogonal group** (including **Lorentz group**) and **unitary group**.

**General Linear Group** :math:`\mathrm{GL}(n)`

We start from the most basic matrix Lie group --- :math:`n`-dim General Linear Group, or :math:`\mathrm{GL}(n)`, which consists of all bijective linear map from an :math:`n`-dim vector space :math:`V` to itself, with group multiplication defined as the map composition. If we select a basis of space :math:`V`, then the map will become an invertible square matrix of order :math:`n`, or square matrix :math:`A` of order :math:`n` with :math:`\det(A)\neq0`.

There is something "general", then there must be something "special". Yes, if we ask :math:`\det(A)=1`, then the matrices form the :math:`n`-dim **Special Linear Group**, or :math:`\mathrm{SL}(n)`. Moreover, this definition is not only suitable for General Linear Group only. Actually, when we say "special ... group", it just means "... group" with the determinant of the group element being :math:`1` specifically.

**Orthogonal Group** :math:`\mathrm{O}(n)` and :math:`\mathrm{O}(m,n)`

When defining :math:`\mathrm{GL}(n)`, we have no restriction on the vector space :math:`V`. Now, if there is also a metric defined on :math:`V`, then we can add more restriction to the transformation --- preserve the "length". More specifically, suppose space :math:`V` has a Euclidean metric :math:`\delta_{\mu\nu}`. Thus, the preservation of "length" can be expressed as

.. math::


   \delta_{\mu\nu}Z^\mu_\rho Z^\nu_\sigma v^\rho v^\sigma = \delta_{\mu\nu}v^\mu v^\nu

or written in matrix form

.. math::


   v^{\mathrm{T}}Z^{\mathrm{T}}Zv = v^{\mathrm{T}} v = v^{\mathrm{T}}Iv

where :math:`I` is the identity matrix. Thus, the preservation of "length" will be equivalent to

.. math::


   Z^{\mathrm{T}}Z = I

All this kind of matrices form the :math:`n`-dim Orthogonal Group, or :math:`\mathrm{O}(n)`. And from the illustration of the previous section, you should be able to understand what is **Special Orthogonal Group**, or :math:`\mathrm{SO}(n)`.

The story does not end here. Just now we ask the space :math:`V` to have a Euclidean metric. Now we want to ask the metric to be more general --- not necessary to be positively definite. More specifically, the diagonal elements of the metric can have :math:`m` occurrences as :math:`-1` and :math:`n` occurrences as :math:`1`. Also ask the matrix to preserve the "length". This kind of matrices form group :math:`\mathrm{O}(m,n)`. A famous example of this kind of group is :math:`\mathrm{O}(1,3)`. It has a dedicated name **Lorentz Group**, and it can be so vital that we decide to open a new section for it.

**Lorentz Group** :math:`\mathrm{L}` or :math:`\mathrm{O}(1,3)`

As is introduced in the previous section, the Lorentz Group is the linear group whose vector space :math:`V` has a Minkowski metric :math:`\eta_{\mu\nu}`. Yes, it is the Minkowski metric that makes it so significant in the physical theories.

The Lorentz Group has quite a complicated structure which we have no intention to address. But we would like to mention one important thing: the Lorentz Group can be divided into four branches, using the :math:`\varLambda^0_0` element (the leftmost and uppermost element) and determinant (either :math:`+1` or :math:`-1`). We use :math:`+/-` and :math:`\uparrow/\downarrow` to denote the four branches, e.g. :math:`\mathrm{L}^\uparrow_+` means :math:`\varLambda^0_0\geqslant1` and :math:`\det(\varLambda)=+1`.

Although there are a massive amount of properties revealed, we stop here --- many interesting facts about the Lorentz Group and its representation will be discussed in the introduction of representation theory.

**Unitary Group** :math:`\mathrm{U}(n)`

All our previous groups are based on the vector space :math:`V` which is *real*. Now we ask it to be complex. Then we get the complex General Linear Group :math:`\mathrm{GL}(n,\mathbb{C})`. Similarly, if there is an inner product (just like the metric in real space) defined on the complex vector space, we can ask the transformation to preserve "length". Thus, we get the unitary group :math:`\mathrm{U}(n)`. Again, we stop here. If you want to know more about the Unitary Group and its similarity or distinction with Orthogonal Group, please refer to the references concerning Lie Group & Lie Algebra.
