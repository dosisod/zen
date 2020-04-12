# zen

![](https://github.com/dosisod/zen/workflows/tests/badge.svg)

A zen commandline game in python

## Installing and Running

```
$ git clone https://github.com/dosisod/zen
$ cd zen

$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip3 install -r requirements.txt

$ python3 -m zen
```

## Testing

Run tests like so:

```
$ pip3 install -r test-requirements.txt
$ pytest
$ mypy -p zen
$ mypy -p test
```
