# UNO STUBS

This package is for working With LibreOffice API.

These files are only stubs and their indented use is for building documents with Sphinx.

If your project needs support for uno when building docs with Sphinx then this package may help.

It will allow you to inherit from `unohelper.Base` do you don't get error `AttributeError: module 'unohelper' has no attribute 'Base'`.

## Installation

Can be pip installed.

```
pip install api_unostubs
```

In most cases will be added to `docs/requirements.txt` file.

```
api_unostubs>=0.2.0
```
