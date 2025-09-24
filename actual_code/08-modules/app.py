import utils as u  # aliasing our import
import random

# import pandas as pd
# import numpy as np

triangle = u.Shape("triangle")  # namespaced!

print(u.default_shape)

u.printer("Hello!")

###

from utils import Shape, printer as p

parallelogram = Shape("parallelogram")  # use without namespacing!
p(f"This is printing! {parallelogram}")


if __name__ == "__main__":
  print(u.__file__)
  print(u.__name__)
  print(u.__doc__)
  print(__name__)