#!/usr/bin/python3

"""The base model"""

from datetime import datetime
from uuid import uuid4

class BaseModel:
    def __init__(self):
        self.id = str(uuid4())

        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):

        self.updated_at = datetime.now()
    

    def __str__(self):
        return "[{}] ({}) {}".\
                format(type(self).__name__, self.id, self.__dict__)

    def to_dict(self):
        mande_dictionary = self.__dict__.copy()
        mande_dictionary['__class__'] = type(self).__name__
        mande_dictionary['created_at'] = mande_dictionary['created_at'].isoformat()
        mande_dictionary['updated_at'] = mande_dictionary['updated_at'].isoformat()
        return mande_dictionary
