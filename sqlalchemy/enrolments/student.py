from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///university.db', echo = False)
# Base class for your classes definitions
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

enrolment_table = Table('enrolments', Base.metadata,
              Column('student_id', Integer, ForeignKey('students.id')),
                    Column('module_id', Integer, ForeignKey('modules.id'))
                    )
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
 # Relationship to the Book class
    modules = relationship('Module', secondary=enrolment_table, back_populates='students')

# Define the Book class
class Module(Base):
    __tablename__ = 'modules'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    students = relationship('Student', secondary=enrolment_table, back_populates='modules')
# Create tables if they do not exist
Base.metadata.create_all(engine)

# Add students
student1 = Student(name = 'Alice Cooper')
student2 = Student(name = 'Robert Ludlum')
student3 = Student(name = 'Anita Kapur')
student4 = Student(name = 'James Colburn')
session.add_all([student1, student2, student3, student4])
session.commit()
# Add modules
module1 = Module(title = 'Mathematics')
module2 = Module(title = 'Robotics')
module3 = Module(title = 'Artifical Intelligence')
module4 = Module(title = 'Data Science')
session.add_all([module1, module2, module3, module4])
session.commit()

# Enrol students in modules
student1.modules.append(module1)
student1.modules.append(module4)
student2.modules.append(module1)
student2.modules.append(module2)
student3.modules.append(module3)
student3.modules.append(module2)
student4.modules.append(module4)
student4.modules.append(module3)
session.commit()
# Query the database.
for student in session.query(Student).all():
    print(f'{student.name} is enrolled in:')
    for module in student.modules:
        print(f'- {module.title}')


# Retrieve the student and module objects
student = session.query(Student).filter_by(name='Robert Ludlum').first()
module = session.query(Module).filter_by(title='Mathematics').first()
# Remove the module from the student's modules list.
if module in student.modules:
    student.modules.remove(module)
    session.commit()
    print(f'\nRemoved {module.title} from {student.name}\'s modules.')
else:
    print(f'{student.name} is not enrolled in {module.title}.')