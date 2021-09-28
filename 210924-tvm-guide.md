# TVM Tutor Version Manager


Es un comando para controlar la versión de tutor disponible en el sistema y en el virtualenv


```bash
tvm --help     # Show context information
tvm install    # Install the given VERSION of tutor in the .tvm directory.
tvm list       # Get all the versions from github.
tvm pip        # Use the package installer pip in current tutor version.
tvm plugins    # Use plugins commands.
tvm setup      # Make the switcher file to anyone in the system.
tvm uninstall  # Install the given VERSION of tutor in the .tvm directory.
tvm use        # Configure the path to use VERSION.


```
Muestra la ayuda.


```bash
stack tvm list
```
Muestra las ultimas versiones disponibles de tutor, las versiones instaladas
y la versión activa.


```bash
stack tvm install v12.0.0
```
Descarga e instala localmente la versión de tutor en .tvm


```bash
stack tvm setup
```
Configura el cambiador de versiones en el virtualenv local


```bash
stack tvm setup -g
```
Configura el cambiador de versiones en el virtualenv local y conecta este cambiador local al sistema unix completo.


```bash
stack tvm use v12.0.0
```
Cambia la versión activa

```
stack tvm pip <command> [options]
```
Usa pip en el entorno de la versión de tutor que está en uso.
Ejemplo:
```
stack tvm pip install git+https://bitbucket.org/edunext/plugin-distro-ednx.git
stack tvm pip freeze
```

```bash
stack tvm plugins list
```
Lista los plugins por cada versión instalada
