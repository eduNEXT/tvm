# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## v2.2.1 - 2024-04-11

### [2.2.1](https://github.com/eduNEXT/tvm/compare/v2.2.0...v2.2.1) (2024-04-11)

### Bug Fixes

- add build.os to RTD & install proper youtube sphinx dep ([#72](https://github.com/eduNEXT/tvm/issues/72)) ([134ed7f](https://github.com/eduNEXT/tvm/commit/134ed7f808e55fba69e6f4be4b00961ab15942eb))

### Continuous Integration

- adds mantainer group ([#62](https://github.com/eduNEXT/tvm/issues/62)) ([41b0145](https://github.com/eduNEXT/tvm/commit/41b0145ae561be6f765a5ed2899a4536f7582650))
- adds pr mantainer group ([#65](https://github.com/eduNEXT/tvm/issues/65)) ([2b5e5b1](https://github.com/eduNEXT/tvm/commit/2b5e5b1e39e262b54f28aa4d939ff75900e4676f))

## v2.2.0 - 2022-12-22

### [2.2.0](https://github.com/eduNEXT/tvm/compare/v2.1.1...v2.2.0) (2022-12-22)

#### Features

- **DS-322:** add command for remove TVM project ([#60](https://github.com/eduNEXT/tvm/issues/60)) ([12439ff](https://github.com/eduNEXT/tvm/commit/12439ff774c299cbb8793f8e64a5da80b3020dd3))

#### Continuous Integration

- update the changelog updater step in bumpversion ([#61](https://github.com/eduNEXT/tvm/issues/61)) ([c6fb805](https://github.com/eduNEXT/tvm/commit/c6fb805578adc1e322307ac937f4c3850eb1a435))

#### Documentation

- update tvm doc release version to 2.1.1 and fix typo and grammar ([#59](https://github.com/eduNEXT/tvm/issues/59)) ([025f000](https://github.com/eduNEXT/tvm/commit/025f00026a955d6e93dcb3a360b7efe547f0a662))

## v2.1.1 - 2022-10-25

### [2.1.1](https://github.com/eduNEXT/tvm/compare/v2.1.0...v2.1.1) (2022-10-25)

### Bug Fixes

- **DS-291:** create a project with a version that is not install ([#58](https://github.com/eduNEXT/tvm/issues/58)) ([8adc08a](https://github.com/eduNEXT/tvm/commit/8adc08a209d9af6dcb3143d4d3f9d0f2808c4b68))

### Documentation

- **bumpversion:** v2.0.1 → 2.1.0 ([0d6494b](https://github.com/eduNEXT/tvm/commit/0d6494b278bdb7c9fb9965fe7bc6b61c114fefa7))
- add the base doc configuration ([631048c](https://github.com/eduNEXT/tvm/commit/631048c48bb2abfe71ce4a430f2e13c1564a9f61))
- add tvm documentation ([09cadc4](https://github.com/eduNEXT/tvm/commit/09cadc4fe01e50ddc4a98c8aba753cab18fbb082))
- update README with the new template and add links to docs ([#57](https://github.com/eduNEXT/tvm/issues/57)) ([7d880c5](https://github.com/eduNEXT/tvm/commit/7d880c5b91db87df2d3bf6e1d61ef12a9e4033d5))

## v2.1.0 - 2022-09-22

### [2.1.0](https://github.com/eduNEXT/tvm/compare/v2.0.1...v2.1.0) (2022-09-22)

#### Features

- init command creates new project with global tvm or latest tvm if machine lacks of one ([0136699](https://github.com/eduNEXT/tvm/commit/01366993b88434ed36565bb02464b23e45e8c265))

#### Styles

- solve styling issues ([5f14fe6](https://github.com/eduNEXT/tvm/commit/5f14fe61e5183bfc77ea5e266bcb5aadd5a734e6))

#### Code Refactoring

- fixed logic style ([8d204d1](https://github.com/eduNEXT/tvm/commit/8d204d175c572cd5183362022017dbec9882eccd))

#### Documentation

- correct quickstart command tvm project init ([c2b9545](https://github.com/eduNEXT/tvm/commit/c2b9545ac144b3c65d62a4c8eed06717b93cab38))
- making the default install the main branch ([7c2ef2a](https://github.com/eduNEXT/tvm/commit/7c2ef2a734a1f6bea4e9a1048115feb4b031265b))

## [2.0.1] - 2022-08-25

### Changed

- Add virtualenv to requirements

## [2.0.0] - 2022-08-10

### Changed

- **BREAKING CHANGE:** Migrate environment manager project init command to clean architecture.
- **BREAKING CHANGE:** Migrate version manager commands to clean architecture.
