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

