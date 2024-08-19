
# Contributing to Infinity File Transfer Architecture

🎉 Thank you for considering contributing to the Infinity File Transfer Architecture! Your contributions help make this project better. Below are some guidelines to help you get started.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Improving Documentation](#improving-documentation)
  - [Contributing Code](#contributing-code)
- [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [License](#license)

## Code of Conduct

By participating in this project, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md). Please read it to understand the standards of behavior we expect from all contributors.

## How Can I Contribute?

### Reporting Bugs

If you find a bug in the project, please help us by reporting it. Here's how:

1. **Search for existing issues**: Before reporting a new bug, please check if it has already been reported.
2. **Create a new issue**: If you can't find an existing issue, create a new one using the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md).
3. **Provide detailed information**: Include a clear title, description, and steps to reproduce the bug. If possible, add screenshots or logs to help us understand the issue.

### Suggesting Features

If you have an idea for a new feature or improvement, we'd love to hear about it! Here's how you can suggest a feature:

1. **Search for existing suggestions**: Check if someone else has already proposed your idea.
2. **Create a new issue**: If your idea is unique, create a new issue using the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md).
3. **Describe your idea**: Clearly explain the feature, why it would be useful, and any implementation suggestions you might have.

### Improving Documentation

Good documentation is essential for any project. If you find any part of the documentation unclear, outdated, or missing, you can help improve it:

1. **Edit directly**: For small fixes (e.g., typos), you can directly edit the markdown files and submit a pull request.
2. **Create an issue**: If you're unsure how to improve the documentation, create an issue to discuss it first.

### Contributing Code

If you'd like to contribute code to the project, follow these steps:

1. **Fork the repository**: Click the "Fork" button at the top of this page to create a copy of the repository under your GitHub account.
2. **Create a new branch**: Branch from `main` for new features or `fix` for bug fixes. Use descriptive names, such as `feature/add-encryption-algorithm` or `fix/file-transfer-bug`.
3. **Make your changes**: Develop your feature or fix in your branch.
4. **Write tests**: If applicable, write tests to ensure your code works as expected.
5. **Commit your changes**: Use clear and concise commit messages. See the [Style Guidelines](#style-guidelines) for more information.
6. **Push to your branch**: Push your branch to your forked repository on GitHub.
7. **Submit a pull request**: Create a pull request (PR) to the `main` branch of the original repository. Include a clear description of your changes.

## Setting Up the Development Environment

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/infinity-file-transfer.git
    cd infinity-file-transfer
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run tests**:

    Make sure everything is working before you start making changes:

    ```bash
    pytest
    ```

## Pull Request Process

1. **Ensure your code follows the project’s style guidelines**.
2. **Update the documentation** if your change requires it.
3. **Add tests** for any new functionality or changes.
4. **Submit a pull request**: Once your code is ready, open a PR. Ensure your PR description includes the following:
   - What issue does it fix or what feature does it implement?
   - How was it tested?
   - Any additional context or screenshots.

## Style Guidelines

- **Coding Style**: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- **Commit Messages**: Use clear, concise, and descriptive commit messages. Example:

    ```plaintext
    Add feature to encrypt files using AES
    ```

- **Branch Names**: Use hyphen-separated, lowercase names that describe the purpose of the branch.

## License

By contributing, you agree that your contributions will be licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
