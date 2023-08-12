#!/usr/bin/python3
"""
BaseModel: A basic model with unique id, creation time, and update time.
TODO: we need to complete the description of the model here
"""

import uuid
import datetime


class BaseModel:
    """
    BaseModel class.

    Attributes:
        id (str): Unique identifier (uuid).
        created_at (datetime.datetime onject): Creation timestamp.
        updated_at (datetime.datetime object): Update timestamp.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
            If a dictionary of a basemodel is passed as **kwarg:
              1.Sets all atributes from the dictionary **kwargs
               other than "__class__" key.
              2.Convert created_at/updated_at to datetime objects
               before setting them as attributes.
            No **kwarg passed:
              1.Sets id to a random uuid4.
              2.Sets created_at/updated_at to the current date and time.

        No_return value.
        """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        # From a single line to 3 due to pip8 80 char rule lol
                        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
                        # dt_obj means date object
                        # Note_to_self: obj.key => assiging something to the
                        # attribute "key".
                        dt_obj = datetime.datetime.strptime(value, iso_format)
                        setattr(self, key, dt_obj)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Return a string representation of the object.

        Return (str): With format: "[className] (id) __dict__"
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute to the current date and time.

        No_return value.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Convert the object to a dictionary.

        Returns (Dictionary):
            dict: dictionary representation of the object with the class name
                  and created_at/updated_at attributes as an isoformat.
        """
        modified_dict = self.__dict__.copy()
        modified_dict["__class__"] = str(self.__class__.__name__)
        modified_dict["created_at"] = self.created_at.isoformat()
        modified_dict["updated_at"] = self.updated_at.isoformat()
        return modified_dict
