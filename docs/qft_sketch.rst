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

