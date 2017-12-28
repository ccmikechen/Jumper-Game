#!/usr/bin/env python3

import jumper.db.database as db
import sys

def main():
    cmd = sys.argv[1]

    if cmd == 'drop':
        db.drop()
    elif cmd == 'create':
        db.create()
    elif cmd == 'reset':
        db.reset()

if __name__ == "__main__":
    main()
