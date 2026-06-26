from setuptools import find_packages, setup

package_name = 'autonomous_navigation'

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
    maintainer='Muqaddsa',
    maintainer_email='forlearning.354@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            # Task 2 — hardcoded 5-waypoint mission
            'waypoint_navigator = autonomous_navigation.waypoint_navigator:main',
            # Task 3 — dynamic CLI-driven mission
            'dynamic_waypoint_navigator = autonomous_navigation.dynamic_waypoint_navigator:main',
        ],
    },
)
