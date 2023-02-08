#!/usr/bin/python3
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
import pep8


class TestBaseModel(unittest.TestCase):
    """TASK 1 UNIT TESTS"""
    def test_bas_mod_id(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.id, str)

    def test_bas_mod_crt(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.created_at, datetime)

    def test_bas_mod_upd(self):
        bm1 = BaseModel()
        self.assertIsInstance(bm1.updated_at, datetime)

    def test_uwu_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_ini_tim(self):
        bm1 = BaseModel()
        self.assertEqual(bm1.created_at, bm1.updated_at)

    def test_sav_upd_met(self):
        bm1 = BaseModel()
        cat = bm1.created_at
        uat = bm1.updated_at
        bm1.save()
        self.assertEqual(bm1.created_at, cat)
        self.assertNotEqual(bm1.updated_at, uat)

    def test_newdict(self):
        bm1 = BaseModel()
        newdict = bm1.to_dict()
        self.assertIsInstance(newdict, dict)
        self.assertIsInstance(newdict["updated_at"], str)
        self.assertIsInstance(newdict["created_at"], str)

    def test_str_met(self):
        bm1 = BaseModel()
        self.assertIn(bm1.id, str(bm1))


class TestBaseModel2(unittest.TestCase):
    "TASK 2 UNIT TESTS"
    def test_init_with_kwargs(self):
        created_at = '2023-04-20T00:00:00.000000'
        updated_at = '2023-04-20T00:00:00.000000'
        newdict1 = {
            'id': 'kratos',
            'created_at': created_at,
            'updated_at': updated_at,
            'name': 'chicken'
        }
        bm1 = BaseModel(**newdict1)
        self.assertEqual(bm1.id, 'kratos')
        self.assertEqual(bm1.created_at,
                         datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm1.updated_at,
                         datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm1.name, 'chicken')


if __name__ == "__main__":
    unittest.main()
