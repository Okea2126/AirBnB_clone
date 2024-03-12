#!/usr/bin/python3

"""The base model"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self *args, **kwargs):

        if not kwargs:
            from models import storage
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def save(self):

        self.updated_at = datetime.now(

    def __str__(self):
        return "[{}] ({}) {}".\
                format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        mande_dictionary = self.__dict__.copy()
        mande_dictionary['__class__'] = type(self).__name__
        mande_dictionary['created_at'] = mande_dictionary['created_at'].isoformat()
        mande_dictionary['updated_at'] = mande_dictionary['updated_at'].isoformat()
        return mande_dictionary
