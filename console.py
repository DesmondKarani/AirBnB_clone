#!/usr/bin/python3
"""
HBNBCommand module: Entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, User, Place,
        State, City, Amenity, or Review"""
        classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
                   "State": State, "City": City,
                   "Amenity": Amenity, "Review": Review}
        args = arg.split()
        if not arg or args[0] not in classes:
            print("** class name missing **" if not arg else
                  "** class doesn't exist **")
        else:
            new_instance = classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all
        instances based or not on the class name"""
        args = arg.split()
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            print([str(obj) for obj in all_objs.values() if len(args) == 0
                   or obj.__class__.__name__ == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute"""
        args = arg.split(" ")
        if len(args) < 4:
            print("** class name missing **" if len(args) < 1 else
                  "** class doesn't exist **" if args[0] not in classes else
                  "** instance id missing **" if len(args) < 2 else
                  "** attribute name missing **" if len(args) < 3 else
                  "** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                instance = storage.all()[key]
                if args[2] not in ["id", "created_at", "updated_at"]:
                    setattr(instance, args[2], args[3].strip('"'))
                    instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
