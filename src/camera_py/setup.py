from setuptools import find_packages, setup

package_name = 'camera_py'

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
    maintainer='mitko',
    maintainer_email='kinov.mitko@gmail.com',
    description='Camera feeds as ROS2 topics',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "usbcam_node = camera_py.usb_cam:main"
        ],
    },
)
