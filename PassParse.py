#!/usr/bin/env python3

# Author:
# Matt May <mcmay.web@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.  You may obtain a
# copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.

import argparse,sys

def main():

    parser = argparse.ArgumentParser(description="Manipulate wordlists for password based attacks and proactive defense.")
    parser.add_argument("-e","--encoding", help="Encoding type used to read file (utf-8, utf-16, etc) [Default: iso-9959-15]", required=False)
    parser.add_argument("-f","--file", help="File path", required=True)
    parser.add_argument("-l","--length", help="Minimum number of characters allowed per password [Default: 12]", required=False)
    parser.add_argument("-t","--typecount", help="Minimum number of character types allowed per password (lowercase, uppercase, numbers, special chars) [Default: 3]", required=False)

    args = vars(parser.parse_args())

    try:

        lower = [
                 "a","b","c","d","e","f","g","h","i","j","k","l","m",
                 "n","o","p","q","r","s","t","u","v","w","x","y","z"
                ]

        capital = [
                   "A","B","C","D","E","F","G","H","I","J","K","L","M",
                   "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
                  ]

        number = ["1","2","3","4","5","6","7","8","9"]

        special = [
                   "`","~","!","@","#","$","%","^","&","*","(",")","-",
                   "_","=","+","[","{","]","}","\\","|",";",":","'",'"',
                   ",","<",".",">","/","?"," "
                  ]

        if args["encoding"]:
            enc = args["encoding"]
        else:
            enc = "iso-8859-15"

        if args["length"]:
            try:
                length = int(args["length"])
            except ValueError:
                print("ERROR: length argument can only accept integers")
                sys.exit()
        else:
            length = 12

        if args["typecount"]:
            try:
                typecount = int(args["typecount"])
            except ValueError:
                print("ERROR: typecount argument can only accept integers")
                sys.exit()
        else:
            typecount = 3

        with open(str(args["file"]), "r", encoding=enc) as f:
            for line in f:
                if len(line) < length:
                    continue
                    
                types = {
                         "lower": False,
                         "capital": False,
                         "number": False,
                         "special": False
                         }

                for letter in line:
                    if letter in lower and not types["lower"]:
                        types["lower"] = True
                        continue
                    elif letter in capital and not types["capital"]:
                        types["capital"] = True
                        continue
                    elif letter in number and not types["number"]:
                        types["number"] = True
                        continue
                    elif letter in special and not types["special"]:
                        types["special"] = True
                        continue

                if sum(types.values()) < typecount:
                     pass
                else:
                    print(line, end="") 

    except IOError:
        print("ERROR: There was a problem opening the file!")
        sys.exit()

    except LookupError:
        print("ERROR: Unknown encoding type: {}".format(enc))
        sys.exit()

    except UnicodeDecodeError as ex:
        print("ERROR: UnicodeDecodeError: {}".format(ex))
        sys.exit()

if __name__ == "__main__":
    main()
