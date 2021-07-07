from distutils.core import setup

setup(
    name='pyramid-xml-renderer',
    version='0.1.6',
    author='Alexander Vasilyev',
    author_email='alexvassel@gmail.com',
    packages=['pyramid_xml_renderer'],
    url='http://pypi.python.org/pypi/pyramid_xml_renderer/',
    description='Pyramid renderer to get xml output of the view and serializer to the xml format',
    long_description=open('README.txt').read(),
)
