## SynapsePayRest-Python

Simple API wrapper for SynapsePay v3 REST API.

## Code Example

Check out [samples.md](samples.md) and our [API documentation](http://docs.synapsepay.com/v3.1) for examples.

## Installation

**note**: we are temporarily using the package name "synapse_pay_rest_native" on pip, but you should still import `synapse_pay_rest` after installing it.
```bash
pip install synapse_pay_rest_native
```

## Development
1. Clone the repo from GitHub.
2. Install requirements:
```bash
pip3 install -r requirements.txt
```

Running the test suite:
```bash
python3 -m unittest synapse_pay_rest.tests
```

## License

The MIT License (MIT)

Copyright (c) 2014 SynapsePay LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.