import jax

from module import Param

def desc(name, *args, **kwargs):
    return name + '(' + ', '.join([repr(x) for x in args] + [f'{k}={v}' for (k,v) in kwargs.items()]) + ')'

def zeros(*shape):
    shape = jax.core.canonicalize_shape(shape)
    return Param(shape=shape, initializer=jax.nn.initializers.zeros, desc=desc('zeros', *shape))

def ones(*shape):
    shape = jax.core.canonicalize_shape(shape)
    return Param(shape=shape, initializer=jax.nn.initializers.ones, desc=desc('ones', *shape))

def normal(*shape, stddev=1.0):
    shape = jax.core.canonicalize_shape(shape)
    return Param(shape=shape, initializer=jax.nn.initializers.normal(stddev=stddev), desc=desc('normal', *shape, stddev=stddev))