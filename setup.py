from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'gz_ptz_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jeff',
    maintainer_email='jeffersonkim97@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pan_vel_cmd_publisher = gz_ptz_control.ptz_pan_cmd:main',
            'pan_pos_cmd_publisher = gz_ptz_control.ptz_pan_cmd_pos:main',
        ],
    },
)
