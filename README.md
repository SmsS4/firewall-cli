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

# Block ssh

### Example
```commandline
python -m pyfi.main block-ssh --user smss
```

### Help
```
Usage: main.py block-ssh [OPTIONS]

  Blocks user from accessing ssh to your computer

Options:
  --user TEXT  user to restrict access
  --help       Show this message and exit.
```


# Block dns

### Example
```commandline
sudo python -m pyfi.main block-dns --addr varzesh3.ir
```

### Help
```
Usage: main.py block-dns [OPTIONS]

  Blocks address for dns resolve

Options:
  --addr TEXT  address to block
  --help       Show this message and exit.
```

# Block dhcp

### Example
```commandline
 python -m pyfi.main block-dhcp --addr 00:00:5e:00:53:af
```

### Help
```
Usage: main.py block-dhcp [OPTIONS]

  Blocks dhcp protocol for specified mac address

Options:
  --addr TEXT  mac-address to block
  --help       Show this message and exit.

```
