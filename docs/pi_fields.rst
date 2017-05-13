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

