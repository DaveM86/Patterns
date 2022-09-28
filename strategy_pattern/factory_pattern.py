'''
The factory pattern is a pattern used to seperate object creation from use
'''

from abc import ABC, abstractstaticmethod, ABCMeta

# generate the abstract base class, the I represents that this is an interface

class IPerson(metaclass=ABCMeta):

	@abstractstaticmethod
	def person_method():
		''' Interface Method '''


# generate the concrete subclasses that that will effectivly overwrite the
# person_method from the abstract class

class Teacher(IPerson):

	def __init__(self):
		self.name = 'Mrs Teacher'

	def person_method(self):
		print('I am a teacher')

class Student(IPerson):

	def __init__(self):
		self.name = 'Student'

	def person_method(self):
		print('I am a Student')

# create the factory that will generate the object, it's important that they return something of type 'IPerson' (the product) subclass in this

class PersonFactory:

	@staticmethod
	def build_person(person_type):
		if person_type == 'Student':
			return Student()
		if person_type == 'Teacher':
			return Teacher()
		print('Invalid Type')


'''
when we create an object we pass our request to the factor to handle the instantation of the object,
we no longer need to know how to instanciate the object the factory does this for us,
you can also have a number of concrete factorys that contain some sort of logic before creating the object that
are subclasses of the main factory.
'''

person = PersonFactory.build_person('Student')
person.person_method()
print(type(person))
print(person)
print(repr(person))