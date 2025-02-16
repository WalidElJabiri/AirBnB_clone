#!/usr/bin/python3
"""
A basic command interpreter model.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    A basic command interpreter class.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program (Ctrl-D).
        """
        print("")
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
