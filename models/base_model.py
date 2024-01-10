#!/usr/bin/python3
"""Module for the BaseModel"""
import uuid
from datetime import datetime


class BaseModel():
	"""
	Parent class contain all attribues and methods used by other classes

	...

	Attributes
	----------
	id : str 
		to have unique id
	created_at : datetime 
		date and time for instance creation
	updated_at : datetime
		date and time for any update happen to an instance

	Methods
	-------
	save()
		updates the public instance attribute updated_at with the current datetime
	to_dict()
		returns a dictionary containing all keys/values of __dict__ of the instance
	"""

	def __init__(self):
		self.id = str(uuid.uuid4())
		self.created_at = datetime.today()
		self.updated_at = datetime.today()

	def save(self):
		"""Update date and time for instance"""
		self.updated_at = datetime.today()

	def to_dict(self):
		"""Update dictionary of the instance"""
		enhanced_dict = self.__dict__.copy()
		enhanced_dict["__class__"] = self.__class__.__name__
		enhanced_dict["created_at"] = self.created_at.isoformat()
		enhanced_dict["updated_at"] = self.updated_at.isoformat()
		return enhanced_dict

	def __str__(self):
		"""Print representation for instance"""
		clsname = self.__class__.__name__
		return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
