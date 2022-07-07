# Block url/ip

# Example
```commandline
python -m pyfi.main block-addr --address varzesh3.com
python -m pyfi.main block-addr --address 123.123.123.123 --output
```

## Help
```
Usage: python -m pyfi.main block-addr [OPTIONS]

  Blocks ip/url Args:     address: dst/src ip/url     output: blocks output
  traffic. default blocks input

Options:
  -a, --address TEXT  ip/url to block
  --output            Blocks output
  --help              Show this message and exit.
```