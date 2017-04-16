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

