from setuptools import setup, find_packages

setup(
    name='MessagePush',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'httpx',
        'pyyaml',
    ],
    author='XiaoqiangClub',
    author_email='your_email@example.com',
    description='A Python package for sending messages via various platforms asynchronously.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/MessagePush',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
