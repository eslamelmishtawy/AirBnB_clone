#!/usr/bin/python3
"""
cmd interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    class for air bnb clone project
    """
    prompt = '(hbnb) '
    def do_quit(self, line):
        """ handle quit """
        return True

    def do_EOF(self, line):
        """ handle EOF """
        return True

    def emptyline(self):
        """empty line do nothing  """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
