# What's TVM

TVM is the acronym for:

- **Tutor Version Manager:** manages the version of the tutor.
- **Tutor enVironment Manager:** for creating project-based environments with tutor.

# Installing TVM

Open a terminal and run:

```bash
pip install git+https://github.com/eduNEXT/tvm.git@<TAG>
```

You can verify the installation with:

```bash
tvm --version
```

## Upgrading TVM (ToDo)

Currently, there isn't a command to do it, if you want to upgrade it, please install it again.

# Usage

## Quickstart with TVM as enVironment Manager

Create and activate a new project with:

1. Install a tutor version with tutor version manager

```bash
tvm install v<tutor-version>
```

2. Create a new project with tutor environment manager

```bash
tvm project <project-name> v<tutor-version>
```

3. Open the project folder

```bash
cd <project-name>
```

4. Activate the project environment

```bash
source .tvm/bin/activate
```

Now you can start configuring and using your tutor instance, reference [tutor official documentation](https://docs.tutor.overhang.io/index.html).

## User Guide

If you want to see what else you can do, access the complete guide of:

- [**Tutor Version Manager**](/docs/TutorVersionManager.rst)

- [**Tutor enVironment Manager**](/docs/TutorEnvironmentManager.rst)

# How to Contribute

Contributions are welcome!. See our [CONTRIBUTING](https://github.com/edunext/tvm/blob/master/CONTRIBUTING.md)
file for more information – it also contains guidelines for how to maintain high code quality, which will make your
contribution more likely to be accepted.

# License

The code in this repository is licensed under version 3 of the AGPL unless
otherwise noted. Please see the [LICENSE](https://github.com/edunext/tvm/blob/main/LICENSE) file for details.
