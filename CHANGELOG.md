# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
