# Creation of Python’s Virtual Environments / Creación de un Entorno Virtual Python #
### Windows 10: ###
#### Onboarding LaunchX module 2 documentation exercise. ####

### Create a Virtual Enviroment ###
Create a folder with the directory of your choice:
```
D:\User\LaunchX\NameOfVirtualEnviroment
```
After open cmd screen, you can install Virtualven with the command `python -m venv env`.
The next line is an approach of what your cmd screen shows:
```
D:\User\LaunchX\VirtualEnviroment>python -m venv env
```
After you've given an enter, nothing will happen on the CMD screen, however the environment is created in the chosen directory:

![Screenshot](https://res.cloudinary.com/gwenyver/image/upload/v1644208877/Github/Capture01_ruclfn.png)

### Activate the Virtual Enviroment ###

To activate the virtual environment, you must locate yourself in the folder with the name `bin` or `Scripts`

The next lines is what your cmd screen looks at:
```
D:\User\LaunchX\VirtualEnviroment>env\Scripts\activate
```

Now you will available to see an `(env)` before the directory, which means your enviroment is now **activate**.

```
(env) D:\User\LaunchX\VirtualEnviroment\env\Scripts>
```

### Install a Package ###
Now the package `python-dateutil` is installed, which according to the [Python](https://pypi.org/project/python-dateutil/) documentation:
> The dateutil module provides powerful extensions to the standard datetime module

You must write in the cmd as below is presented in the following line:

```
(env) D:\User\LaunchX\VirtualEnviroment>pip install python-dateutil --upgrade
```

Now, with the command `pip freeze`, you can see what packages you have installed.  
`pip freeze`, according to the [documentation](https://pip.pypa.io/en/stable/cli/pip_freeze/) is an:
>Output installed packages in requirements format.
>`packages` are listed in a case-insensitive sorted order.

After executing the command you will see the following on the CMD screen:
```
(env) D:\User\LaunchX\VirtualEnviroment>pip freeze
python-dateutil==2.8.2
six==1.16.0
```

### Deactivate the Virtual Enviroment ###

When you need to close your virtual environment, you just have to execute the following command in cmd:
```
(env) D:\User\LaunchX\VirtualEnviroment\env\Scripts>deactivate
```
After that, yor screen display your directory without `(env)`.
```
 D:\User\LaunchX\VirtualEnviroment\env\Scripts>
```

