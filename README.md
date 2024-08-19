# Infinity File Transfer Architecture

![Infinity File Transfer](https://your-image-link-here.com/banner.png)

## Overview

The **Infinity File Transfer Architecture** is a cross-platform file transfer system that ensures secure and reliable data transmission between Windows and Linux systems. The architecture uses custom encryption and decryption methods, leveraging platform-specific tools like Netcat for efficient file transfers.

## Features

- **Cross-Platform Compatibility**: Supports both Windows and Linux operating systems.
- **Secure File Transfer**: Uses a reversible mathematical encryption method to secure data.
- **Platform-Specific Optimization**: Utilizes platform-specific commands for seamless file transfer.
- **Simple & Lightweight**: Minimal dependencies and easy to set up.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Sending Files](#sending-files)
  - [Receiving Files](#receiving-files)
- [System Architecture](#system-architecture)
- [Security Considerations](#security-considerations)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/infinity-file-transfer.git
    cd infinity-file-transfer
    ```

2. **Install Dependencies** (if any):

    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure Netcat is installed:**

    - **Windows**: [Download and install Netcat](https://nmap.org/ncat/)
    - **Linux**: Install using package manager (e.g., `sudo apt-get install netcat`)

## Usage

### Sending Files

1. Run the **main** script:

    ```bash
    python mian.py
    ```

2. Follow the on-screen prompts to enter the file path, destination IP address, and port.

3. The file will be encrypted and securely transferred.

### Receiving Files

1. Run the **main** script:

    ```bash
    python main.py
    ```

2. Follow the on-screen prompts to specify the port to listen on and the name for the received file.

3. The file will be received, decrypted, and saved.

## System Architecture

The system is composed of four main components:

- **Encryptor**: Reverses the byte order of the file for basic encryption.
- **Decryptor**: Restores the original byte order to decrypt the file.
- **Sender**: Detects the operating system, encrypts the file, and uses Netcat to send it.
- **Receiver**: Listens on a specified port, receives the file using Netcat, and decrypts it.


## Security Considerations

While the current encryption method provides basic obfuscation, it is recommended to explore more advanced encryption algorithms for sensitive data. Network security measures like firewalls and secure network configurations should also be implemented.

## Testing

The system has been tested on both Windows and Linux environments for small to medium-sized files. Performance metrics like encryption time, transmission time, and decryption time were evaluated, and the results were satisfactory under typical network conditions.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
