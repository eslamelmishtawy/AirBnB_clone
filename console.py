#!/usr/bin/python3
"""
cmd interpreter
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
classes = ['BaseModel', 'User']


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

    def do_create(self, args):
        """ create new instance of base class"""
        line = shlex.split(args)
        if (len(line) == 0):
            print("** class name missing **")
        if (line[0] not in classes):
            print("** class doesn't exist **")
        else:
            instance = eval(f"{line[0]}()")
            storage.save()
            print(instance.id)
    
    def do_show(self, args):
        """ Prints the string representation of an instance based on the class name """
        line = shlex.split(args)

        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()

            key = "{}.{}".format(line[0], line[1])
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """ Delete an instance based on the class name and id."""
        line = shlex.split(args)

        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(line[0], line[1])
            if key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """Print the string representation of all instances or a specific class"""
        obj = storage.all()

        line = shlex.split(args)

        if len(line) == 0:
            for key, value in obj.items():
                print(str(value))
        elif line[0] not in classes:
            print("** class doesn't exist **")
        else:
            for key, value in obj.items():
                if key.split('.')[0] == line[0]:
                    print(str(value))

    def do_update(self, args):
        """ Update an instance by adding or updating an attribute """
        line = shlex.split(args)

        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in classes:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            obj = storage.all()

            key = "{}.{}".format(line[0], line[1])
            if key not in obj:
                print("** no instance found **")
            elif len(line) < 3:
                print("** attribute name missing **")
            elif len(line) < 4:
                print("** value missing **")
            else:
                o = obj[key]
                name = line[2]
                value = line[3]
                try:
                    value = eval(value)
                except Exception:
                    pass
                setattr(obj, name, value)

                o.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
