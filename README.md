# L18NPrint

A small monkey patch utility to allow python to print correctly, finally.

Pull requests and improvements are welcome. And, as always:

"k8s: the 8 is short for ubernete"

# Installation

The simplest way to install this package is with [poetry](https://python-poetry.org/). Just `poetry add git+https://github.com/novafacing/l18nprint`.

You can also install with plain pip: `python3 -m pip install git+https://github.com/novafacing/l18nprint.git`.

If you really want, you can download the source yourself.

```
$ git clone https://github.com/novafacing/l18nprint.git
$ cd l18nprint
$ poetry build && python3 -m pip install dist/*.whl
```

# Example usage

```python
from l18nprint.l18nprint import *
>>> print("yeah i spent quite a while making this", "definitely", (), ["longer than I would have liked"])
y2h i s3t q3e a w3e m4g t2s d8y () ['longer than I would have liked']
```
