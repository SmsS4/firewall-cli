# Block url/ip

### Example
```commandline
python -m pyfi.main block-addr --address varzesh3.com
python -m pyfi.main block-addr --address 123.123.123.123 --output
```

### Help
```
Usage: python -m pyfi.main block-addr [OPTIONS]
  Blocks ip/url

Options:
  -a, --address TEXT  ip/url to block
  --output            Blocks output (by default blocks input)
  --help              Show this message and exit.
```

# Block port

### Example
```commandline
python -m pyfi.main block-port --port 60000 --protocol tcp --output
```

### Help
```
Usage: python -m pyfi.main block-port [OPTIONS]

  Blocks port with given protocol

Options:
  --port INTEGER   port to block
  --protocol TEXT  protocol to block. tcp/udp
  --output         Blocks output
  --help           Show this message and exit.
```
