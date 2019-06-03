# JSON Tree
#### Display a tree-view of a JSON-formatted string using only the Python3 core library.  (No Imports.)

## Assumptions
* Badly-formmatted JSON should raise an error.
* Well-formed but empty JSON should yield nothing.
* No plans to build this out into a fully-fledged JSON parser, so maintaining object heirarchy was of lesser concern.

## Installation

> Run as a standalone script (I had a setup.py for a pip install, but it seemed like unnecessary overhead.) 

* Download the repo and change directory to json_tree directory
```
cd /path/to/json_tree
```

## Usage example
Basic Usage:
```
python json_tree.py
```
> I was going to add a `--alpha` option, but that would have required using sys.argv at the least.

Run Tests:
```
python test.py
```

## Release History
* 0.0.1
    * Work in progress

## Meta

Distributed under MIT Public license. See ``LICENSE`` for more information.

## Contributing

1. Fork it (<https://github.com/eric02138/json_tree/fork>)
2. Create your feature branch (`git checkout -b feature/someaddition`)
3. Commit your changes (`git commit -am 'Add someaddtion'`)
4. Push to the branch (`git push origin feature/someaddition`)
5. Create a new Pull Request