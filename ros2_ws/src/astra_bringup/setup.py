import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'astra_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='Launch files that bring up the ASTRA Phase 1 demo',
    license='MIT',
    tests_require=['pytest'],
    entry_points={'console_scripts': []},
)
