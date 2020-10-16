# PrioHeap

![test badge](https://github.com/adefossez/prioheap/workflows/test/badge.svg)

A priority queue from the textbooks. Python implementation is surprinsigly not modern.

## Installation

```python
pip3 install prioheap
```

## Usage

The API is dead simple:

```python
import prioheap

prio = prioheap.PrioHeap()
prio.add(0) # add element
prio.add(3)
prio.peak()  # return highest element, e.g. 3
prio.add(1)
prio.pop()  # remove and return highest element, 3.

len(prio), bool(prio)  # those are supported
iter(prio), list(prio)  # iterate elements in decreasing order
```

## Test

To run the unit tests from the root of this repository:
```python
python3 -m tests
```

## License

License is Unlincense, so public domain.
