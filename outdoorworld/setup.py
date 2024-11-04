from setuptools import find_packages, setup

package_name = 'outdoorworld'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/f23_robotics_1_launch.py']))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/outdoorworld.wbt', 
]))
data_files.append(('share/' + package_name, ['package.xml']))
setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='crolson1',
    maintainer_email='cooper@olsonville.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
