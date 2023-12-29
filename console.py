#!/usr/bin/python3
""" Defination for the command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


classes = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "State": State,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }

cmds = ['all', 'create', 'update', 'show', 'destroy']


class HBNBCommand(cmd.Cmd):
    """A classs defination for HBNBCommand"""

    prompt = "(hbnb) "

    def precmd(self, line):
        """runs before any command"""

        if "." in line and "(" in line and ")" in line:
            cls = line.split(".")
            cnd = cls[1].split("(")
            _id = cnd[1].split(")")
            if cls[0] in classes and cnd[0] in cmds:
                line = cnd[0] + ' ' + cls[0] + ' ' + _id[0]
        return line

    def do_quit(self, line):
        """A quit command to exit the program"""

        return True

    def do_EOF(self, line):
        """EOF will also exit the program"""

        return True

    def help_help(self):
        """ help command"""

    def emptyline(self):
        """ This does nothing"""
        pass

    def do_create(self, line):
        """ A command that creates a given class instance"""
        if line == "":
            print("** class name missing **")
        elif line in classes:
            instance = classes[line]()
            instance.save()
            print(instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id
        """
        command = line.split()

        if line == "":
            print("** class name missing **")
        elif command[0] not in classes:
            print("** class doesn't exist **")
        elif len(command) != 2:
            print("** instance id missing **")
        elif command[0] + "." + command[1] not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[command[0] + "." + command[1]])

    def do_destroy(self, line):
        """ Destroys an instance of a class"""

        command = line.split()

        if line == "":
            print("** class name missing **")
        elif command[0] not in classes:
            print("** class doesn't exist **")
        elif len(command) != 2:
            print("** instance id missing **")
        elif command[0] + "." + command[1] not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[command[0] + "." + command[1]]
            storage.save()

    def do_all(self, line):
        """Prints all string representation of all
        instances based on the class name
        """

        if line == "":
            for value in storage.all().values():
                print([str(value)])

        elif line in classes:
            for key, value in storage.all().items():
                n_key = key.split(".")
                if n_key[0] == line:
                    print([str(value)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """

        command = line.split()

        if line == "":
            print("** class name missing **")
        elif command[0] not in classes:
            print("** class doesn't exist **")
        elif len(command) < 2:
            print("** instance id missing **")
        elif command[0] + "." + command[1] not in storage.all():
            print("** no instance found **")
        elif len(command) < 3:
            print("** attribute name missing **")
        elif len(command) < 4:
            print("** value missing **")
        else:
            command = command[0:4]
            key = command[0] + "." + command[1]
            instance = storage.all()[key]
            command[3] = eval(command[3])
            setattr(instance, command[2], command[3])
            instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
