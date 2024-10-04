# Redis Operations and Caching with Python

## Learning Objectives

- Understand how to use Redis for basic operations.
- Learn how to use Redis as a simple cache.

## Requirements

- Files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.9**.
- All files should end with a new line.
- A `README.md` file at the root of the project is mandatory.
- The first line of all Python files should be exactly:
  ```python
  #!/usr/bin/env python3
  ```

## Code Style and Documentation Requirements

- Your code should follow **pycodestyle** (version 2.5).
- All modules, classes, functions, and methods should have comprehensive documentation.

### Example for Module Documentation:

```bash
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```

- Documentation must explain the purpose of the module, class, or method in clear, complete sentences.
- All functions and coroutines must be type-annotated.

## Installation of Redis on Ubuntu 18.04

To install and set up Redis on **Ubuntu 18.04**, follow these steps:

### Install Redis Server:

```bash
sudo apt-get -y install redis-server
pip3 install redis
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
sudo service redis-server start
```

### License

This project is licensed under the MIT License. -
This section provides clear steps for installing Redis on Ubuntu and using it in a container. Let me know if you'd like any modifications!
