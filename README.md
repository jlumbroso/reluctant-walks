# Sampling from Reluctant Quarter-Plane Walks

Reluctant walks tend to exit the quarter-plane in which they are constrained, but this work shows how to randomly sample large reluctant walks anyway.

## Installation

Since the package is registered in Python's central repository, you can install it using `pip`:

```
pip install reluctant_walks
```

Although the package will degrade gracefully, it has some dependencies for certain of its functionalities:

- The [Sage environment](http://www.sagemath.org/), to solve the equation necessary to compute the best slope for any family of quarter-plane walk. (Without Sage, it is possible to experiment on the "*79 non-trivial small stepset models*" for which we have precomputed the best slope with some accuracy.)

- Either [GenRGenS](https://www.lri.fr/genrgens/index.php?idpage=2) or [Maple](https://www.maplesoft.com/) as a backend to randomly sample walks given an algebraic grammar, if you wish to be able to randomly generate walks.

In addition, it is recommended to have `matplotlib` to visualize the walks, and Jupyter Notebook to experiment with the package. See the `notebook` folder for examples.

## Example

Below is a single walk of size 2000 in green, on a backdrop of many other walks that were also sampled, but which do not remain in the upper-right quarter-plane. There are further such examples in the [VisualizingWalks.ipynb](notebook/VisualizingWalks.ipynb) notebook.

![Plot of a constrained walk in green, on a backdrop of unconstrained walks.](examples/images/example.png?raw=true "Plot of a constrained walk in green, on a backdrop of unconstrained walks.")

## Bibliography

Bousquet-Mélou, Mireille, and Marni Mishna (2010). "[Walks with small steps in the quarter plane.](https://arxiv.org/abs/0810.4387)" *Contemporary Mathematics*, 520, pp. 1-40.

Lumbroso, Jeremie, Marni Mishna, and Yann Ponty (2017). "[Taming Reluctant Random Walks in the Positive Quadrant.](https://www.sciencedirect.com/science/article/pii/S1571065317300793)" *Electronic Notes in Discrete Mathematics* (59), pp. 99-114.
