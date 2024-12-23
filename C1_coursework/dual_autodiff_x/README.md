# Automatic Differentiation with dual_autodiff

__Maintainer: Prithvi Singh__

This package is designed to handle automatic differentiation for functions in python. It utilizes forward mode differentiation with the help of dual numbers.


## Features

**Dual Numbers**: Initialise and manipulate dual numbers handled by the `Dual` class in the `dual.py` file.

**Forward Mode Differentiation**: Compute the derivatives of complex functions utilising dual numbers and the chain rule.

## Installation

To install the package clone this repository onto your laptop and install it manually using pip. 

## Usage

Here is a baseline example of how to use the dual_autodiff package:

```python
    from dual_autodiff import dual_autodiff as df
    x= df.Dual(2,1)
    y= df.Dual(1,3)

    print(x+y)
```

```
    #Output
    Dual(real=3,dual=3)
```
Algebraic functions are also defined with the following syntax:

```python 
    print(x.sin())
```
```
    #Output
    Dual(real=0.9092974268256817,dual=-0.4161468365471424)
```
Note that the dual part is the differentiation of sin(x) calculated at x=2 multiplied by the initial slope. 

$$
\frac{d}{dx}sin(f(x))=cos(f(x))\times \frac{d}{dx}f(x)
$$

Note that this approach provides the answer with machine precision as all the derivatives are calculated analytically using the chain rule.


## Documentation

Link to the [documentation page](https://your-readthedocs-url-here).

## Contributing

Contributions via pull requests are welcome!

## License

This project is distributed under the MIT License. See the `LICENSE` file for details.


Add chat GPT usage 

