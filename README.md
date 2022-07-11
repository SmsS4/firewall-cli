### Question
برای شکستن پورت ناکینگ باید تمام حالت‌ها را امتحان کند. اگر تعداد ناک‌ها n باشد می‌شود
`65535*65534*65533...(65536-n)`
که یعنی اگر n بیشتر مساوی ۳ باشد می‌شود حداقل `281474976710656` حالت که انقدر زیاد است که فرد نتواند پورت‌ناکینگ را شکست دهد.

# Garbage firewall cli

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
python -m pyfi.main block-dns --addr varzesh3.ir
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

# Dos history
you have to run `python -m pyfi.main dos-add-logger` once to config database and history

### Example
```commandline
python -m pyfi.main dos-export
```

### Output example
```
IP                   NUMBER OF PACKETS    LENGTH OF PACKETS
190.2.145.41         15123                20349922
104.16.248.249       11                   4800
168.119.4.163        3                    168
8.8.8.8              117                  9760
188.120.248.18       833                  572388
168.119.209.188      112                  5824
127.0.0.1            63                   4655
66.102.1.188         13                   676
194.36.144.87        3                    168
3.64.117.201         3                    168
78.47.93.191         3                    168
45.9.61.155          2                    112
74.91.29.203         3                    156
0.0.0.0              10                   320
192.168.31.126       29                   1742
192.168.31.224       10                   320
178.22.122.100       15                   1090
74.91.29.206         31                   4254
127.0.0.53           15                   1138
192.168.31.1         19                   1948
185.125.190.58       2                    112
185.120.22.12        2                    112
74.91.29.202         7                    520
216.58.212.142       1                    52
192.168.31.209       4                    128
185.125.190.57       2                    112
142.250.186.132      11                   7388
193.158.22.13        2                    112
131.188.3.221        2                    112
131.188.3.220        2                    112
```

### Help
```
Usage: python -m pyfi.main dos-export [OPTIONS]

  Exports ips history

Options:
  --help  Show this message and exit.
```

# Port knocking

### Example
```commandline
 python -m pyfi.main port-knocking --knocks 12345,23456,34567  --port 80
```

### Help
```
Usage: python -m pyfi.main port-knocking [OPTIONS]

Options:
  --knocks TEXT   list of port to use for port knocking separated by `,`
  --port INTEGER  destination port
  --help          Show this message and exit.
```
