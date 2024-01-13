#!/usr/bin/python3
"""
cmd interpreter
"""
import cmd


class HBNBcmd(cmd.Cmd):
    """
    class for air bnb clone project
    """
    prompt = '(hbnb) '


if __name__ == '__main__':
    HBNBcmd().cmdloop()
