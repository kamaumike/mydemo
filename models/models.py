from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Student(Base):
	"""Creates student table"""

	__tablename__ = 'student'
	id = Column(Integer,primary_key=True)
	name = Column(String(50))
	is_student_in_class = Column(Boolean, default=False)    

class Class(Base):
	"""Creates class table"""

	__tablename__ = 'class'
	id = Column(Integer,primary_key=True)
	name = Column(String(50))
	class_in_session = Column(Boolean, default=False)
	class_start_time = Column(DateTime)
	class_end_time = Column(DateTime)

class TrackStudent(Base):
	"""Creates a TrackStudent table for 
	tracking students' in a class.
	"""

	__tablename__ = 'TrackStudent'
	id = Column(Integer,primary_key=True)
	check_in_time = Column(DateTime, default=func.now())
	check_out_time = Column(DateTime)
	reason = Column(String)
	student_id = Column(Integer,ForeignKey('student.id'))
	class_id = Column(Integer,ForeignKey('class.id'))
	students = relationship(Student)
	classes = relationship(Class)
