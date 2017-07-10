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

