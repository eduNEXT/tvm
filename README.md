# TVM

![Maintainance Badge](https://img.shields.io/badge/Status-Maintained-brightgreen)
![Test Badge](https://img.shields.io/github/actions/workflow/status/edunext/tvm/.github%2Fworkflows%2Ftests.yml?label=Test)
![GitHub Tag](https://img.shields.io/github/v/tag/edunext/tvm?label=Tag)


TVM is a tool that allows you to manage several Tutor development environments so that they work in isolation, and you can work on different projects with independent Tutor versions and configurations.

TVM is also the acronym for:

- **Tutor Version Manager:** Handle the Tutor versions.
- **Tutor enVironment Manager:** Create project-based environments with Tutor.

# Installing TVM

Open a terminal and run:

```bash
pip install git+https://github.com/eduNEXT/tvm.git
```

Verify the installation:

```bash
tvm --version
```

# Getting Started

Create and activate a new project with the following steps:

1. Install the version of Tutor you want to use with TVM.

   ```bash
   tvm install <tutor-version>

   # For example:
   # tvm install v14.0.0
   ```

2. Create a new project with TVM.

   ```bash
   tvm project init <project-name> <tutor-version>

   # For example:
   # tvm project init tvm-test v14.0.0
   ```

3. Open the project folder.

   ```bash
   cd <project-name>
   ```

4. Activate the project environment.

   ```bash
   source .tvm/bin/activate
   ```

5. Run your project.

   ```bash
   tutor local launch
   ```

> [!NOTE]
> For Tutor versions <15, init a project with `tutor local quickstart`

You can start configuring and using your Tutor instance.

## Next steps

If you want to see what else you can do, access **the complete TVM documentation**: https://tvm.docs.edunext.co

# Getting Help

- To report a bug or ask for a feature, go to the TVM GitHub issues: https://github.com/eduNEXT/tvm/issues

- To get support, go to the TVM Github discussion forum: https://github.com/eduNEXT/tvm/discussions

# How to Contribute

Contributions are welcome! See our [CONTRIBUTING](https://github.com/edunext/tvm/blob/master/CONTRIBUTING.md) file for more information – it also contains guidelines for how to maintain high code quality, which will make your contribution more likely to be accepted.

# License

The code in this repository is licensed under version 3 of the AGPL unless
otherwise noted. Please see the [LICENSE](https://github.com/edunext/tvm/blob/main/LICENSE) file for details.
