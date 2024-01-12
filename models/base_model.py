# models/base_model.py

import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

            if not kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = self.updated_at = datetime.now()
                from models import storage  # Local import
                storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates updated_at and saves the object to file storage."""
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
        of __dict__ of the instance. """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = dictionary['created_at'].isoformat()
        dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        return dictionary
