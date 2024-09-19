from setuptools import find_packages, setup

package_name = 'teacher_student_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    #tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'student_receive_node = teacher_student_pkg.student_receive_node:main',
            'teacher_hello_node = teacher_student_pkg.teacher_hello_node:main'
        ],
    },
)
