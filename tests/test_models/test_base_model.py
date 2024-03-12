#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class BaseModelTest(unittest.TestCase):
    def __init__(self):
        mande_model = BaseModel()

        self.assertIsNotNone(mande_model.id)
        self.assertIsNotNone(mande_model.created_at)
        self.assertIsNotNone(mande_model.updated_at)

    def saving_test(self):
        mande_model = BaseModel()

        first_update = mande_model.updated_at
        now_update = mande_model.save()

        self.assertIsNotEqual(first_update, now_update)

    def dict_test(self):
        mande_model = BaseModel()

        my_dict = mande_model.to_dict()
        self.assertIsInstance(my_dict, dict)

        self.assertEqual(my_dict['created_at'], mande_model.created_at.isoformat())
        self.assertEqual(my_dict['updated_at'], mande_model.updated_at.isoformat())
        self.assertEqual(my_dict['__class__'], 'BaseModel')
        self.assertEqual(my_dict['id'], mande_model.id)

    def str_test(self):
        mande_model = BaseModel()

        self.assertTrue(str(mande_model).startswith('[BaseModel]'))
        self.assertIn(mande_model.id, str(mande_model))
        self.assertIn(str(mande_model.__dict__), str(mande_model))

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

if __name__ == "__main__":
    unittest.main()
