#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple file-backed caching engine."""

import os
import pickle


class PickleCache(object):
    """A simple file-backed caching engine."""

    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor for PickleCache class.

        Args:
            file_path (str, optional): The name of the output pickle file.
                                       Default: 'datastore.pkl'
            autosync (bool, optional): Autosync setting. Default: False.

        Attributes:
            __file_path (pseudo-private): The name of the output pickle file.
            __data (pseudo-private): An empty dictionary object.
            autosync (bool): Autosync setting. Default: False
        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """Sets the keys and values in PickleCache.

        Args:
            key (str): the key to be stored in self.__data
            value (str): the value to be stored in self.__data
        """
        cache_dict = {key: value}
        self.__data.update(cache_dict)
        if self.autosync:
            self.flush()

    def __len__(self):
        """Returns the length of self.__data"""
        return len(self.__data)

    def __getitem__(self, key):
        """Get the value from self.__data.

        Args:
            key (str): Use this key to get requested value from self.__data

        Returns:
            str: the value of the key.
        """
        return self.__data[key]

    def __delitem__(self, key):
        """Deletes unwanted objects from the PickleCache object.

        Args:
           key (str): The key of the object that will be removed.
        """
        del self.__data[key]
        if self.autosync:
            self.flush()

    def load(self):
        """To load the file if it exists and is greater than zero bite."""
        file_a = self.__file_path
        if os.path.exists(file_a) and os.path.getsize(file_a) > 0:
            fhandler = open(file_a, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """To save the stored data to a file."""
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
