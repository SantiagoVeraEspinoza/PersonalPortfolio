import unittest
import os
os.environ['TESTING'] = 'true'

from peewee import *
from playhouse.shortcuts import model_to_dict

from app import app
from app import TimelinePost

class AppTestCase(unittest.TestCase):
    print("Hola")
