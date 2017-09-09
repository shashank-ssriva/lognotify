from setuptools import setup

setup(name='lognotify',
      version='0.1',
      py_modules = ['lognotify'],
      description='A real-time log monitoring & notification utility which pops up a notification (while running your application) whenever it sees an error in log-file.',
      url='http://github.com/shashank-ssriva',
      author='Shashank Srivastava',
      license='MIT',
      entry_points={
        'console_scripts':[
            'lognotify = lognotify.app:main'
            ]
        },
      zip_safe=False)
