# PassParse

## Summary
Recently I helped implement some password policies and controls. While doing so we implemented a control that disallows users from setting passwords shorter than a particular length, and unless they have a certain number of the following categories - special chars, numbers, lowercase, or uppercase. Another control in place compares the passwords to a known wordlist, and doesn't allow them if they are already in the wordlist. We ended up taking various well known wordlists from dumps and pentest tools, aggregating them, and adding them to this list. The longer the list, however, the more processing time it requires. This script removes all words shorter than `-l` characters, and that don't have at least `-t` of the required character types. The tool also allows the user to declare which encoding type used to read the input file with `e`.

## Usage
```
./PassParse.py -h

usage: PassParse.py [-h] [-e ENCODING] -f FILE [-l LENGTH] [-t TYPECOUNT]

Manipulate wordlists for password based attacks and proactive defense.

optional arguments:
  -h, --help            show this help message and exit
  -e ENCODING, --encoding ENCODING
                        Encoding type used to read file (utf-8, utf-16, etc)
                        [Default: iso-9959-15]
  -f FILE, --file FILE  File path
  -l LENGTH, --length LENGTH
                        Minimum number of characters allowed per password
                        [Default: 12]
  -t TYPECOUNT, --typecount TYPECOUNT
                        Minimum number of character types allowed per password
                        (lowercase, uppercase, numbers, special chars)
                        [Default: 3]
```
