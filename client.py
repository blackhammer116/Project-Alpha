#!/usr/bin/python3
"""
Necessary models for the clients base class
"""
import uuid


class BaseClient:
    """ Base class for all clients """
    def __init__(self, *args, **kwargs):
        """ initialization of the base model """
        self.id = str(uuid.uuid4())
        self.name = args[0]
        #payment credentials also needed
        self.email = args[1]
