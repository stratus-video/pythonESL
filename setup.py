from setuptools import Extension, find_packages, setup
from setuptools.command.install import install
from distutils.command.build import build


class CustomBuild(build):
    sub_commands = [
        ('build_ext', build.has_ext_modules),
        ('build_py', build.has_pure_modules),
        ('build_clib', build.has_c_libraries),
        ('build_scripts', build.has_scripts),
    ]


esl = Extension(
    name='ESL._ESL',
    sources=['ESL/esl.c',
             'ESL/esl_buffer.c',
             'ESL/esl_config.c',
             'ESL/esl_event.c',
             'ESL/esl_json.c',
             'ESL/esl_threadmutex.c',
             'ESL/cJSON.c',
             'ESL/esl_oop.cpp',
             'ESL/ESL.i'],
    swig_opts=['-c++', '-py3', '-threads', '-I./ESL'],
    include_dirs=['./ESL'],
    extra_compile_args=['-I./ESL']
)

setup(
    name='python-ESL',
    version='1.10.11',
    author='FreeSWITCH Developers',
    description='FreeSWITCH Event Socket Library for Python',
    url='https://github.com/stratus-video/pythonESL',
    download_url='https://github.com/stratus-video/pythonESL/tarball/1.10.11',
    cmdclass={'build': CustomBuild},
    ext_modules=[esl],
    packages=['ESL'],
)
