#!/usr/bin/python3
""" A command interpreter fot the AirBnB console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Class definition for HBNBCommand"""

    prompt = '(hbnb)'

    def do_quit(self, args):
        """ command to quit the command line interface"""

        return True

    def do_EOF(self, args):
        """ command to exit the command line interface"""

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
