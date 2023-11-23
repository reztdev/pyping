from setuptools import setup, find_packages

setup(
    name='pyping',
    version='1.0.0',
    py_modules=['pyping'],
    install_requires=['scapy'],
    author='Muhammad Rizki (reztdev)',
    author_email='reztdev_ryz@gmail.com',
    description='Simple ping TCP and ICMP implementation in Python',
    packages=find_packages(),
    keywords='ping tcping scapy networking',
    url='https://github.com/reztdev/pyping',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        ],
    )

