from setuptools import find_packages, setup

package_name = 'assignment1'

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
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node_1 = assignment1.my_node_1:main'
            'student_receive_node = assignment1.student_receive_node:main'
            'teacher_hello_node = assignment1.teacher_hello_node:main'
        ],
    },
)
