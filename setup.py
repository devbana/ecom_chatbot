from setuptools import find_packages, setup

setup(name='chat_bot_ecomm',
      version='0.0.1',
      author='Akash Devbanshi',
      author_email='akash.devbanshi@outlook.com',
      packages=find_packages(),
      install_requires=['langchain-astradb', 'langchain', 'langchain-openai', 'datasets', 'pypdf', 'python-dotenv', 'flask']
      )