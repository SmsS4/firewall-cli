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

# Block http

### Example
```commandline
python -m pyfi.main block-http --content 0jk2398gkm392g8j29gj32498 --port 80
```

### Help
```
Usage: main.py block-http [OPTIONS]

  Blocks http if contains a specified content

Options:
  --content TEXT  drop packets contains this word
  --port INTEGER  use rules on this port
  --help          Show this message and exit.

```

# Block header

### Example
```commandline
python -m pyfi.main block-header --key 123123 --value 123123 --port 80
```

### Help
```
Usage: main.py block-header [OPTIONS]

  Blocks http request if contains a header

Options:
  --key TEXT      header's key
  --value TEXT    header's value
  --port INTEGER  use rules on this port
  --help          Show this message and exit.
```


# Dos udp-flood blocking
### Example
```commandline
 python -m pyfi.main dos-dns-flood --rate-limit 200
```
### Help
```
Usage: python -m pyfi.main dos-dns-flood [OPTIONS]

  Ratelimit on dns requests to prevent dns-flood attack

Options:
  --rate-limit INTEGER  number of allowd requests per second
  --help                Show this message and exit.
```

# Dos slowloris
### Example
```commandline
sudo python -m pyfi.main dos-slowloris --port 80 --connections-limit 200
```

### Help
```
Usage: main.py dos-slowloris [OPTIONS]

Options:
  --port INTEGER               port to limit number of connections
  --connections-limit INTEGER  number of allowed connections
  --protocol TEXT              protocol of connection. defaults to tcp
  --help                       Show this message and exit.
```

# Dos syn flood
### Example
```commandline
 python -m pyfi.main dos-syn-flood --port 80 --rate-limit 100
```

### Help
```
Usage: python -m pyfi.main dos-syn-flood [OPTIONS]

Options:
  --port INTEGER        port to limit number of connections
  --rate-limit INTEGER  number of allowed connections
  --protocol TEXT       protocol of connection. defaults to tcp
  --help                Show this message and exit.
```
