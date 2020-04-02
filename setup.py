import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='flowvis',
    packages=['flowvis'],
    version='0.1',
    license='MIT',
    author='Tom Runia',
    author_email='firstname.lastname@gmail.com',
    description='Easy optical flow visualisation in Python.',
    long_description=long_description,
    url='https://github.com/tomrunia/OpticalFlow_Visualization',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords=['optical flow', 'visualization', 'motion'],
    install_requires=['numpy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)