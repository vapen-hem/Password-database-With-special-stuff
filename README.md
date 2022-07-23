# Password-database-With-special-stuff
This program can:
- Generate passwords and pincodes
- Generate Encryption keys
- Encrypt files
- Decrypt files(If you have the original encryption key, no bruteforce option exists)

## Showcase
https://www.youtube.com/watch?v=il-FryGU4Ik

## Installation

1. Clone the repository
    ```bash
        git clone https://vapen-hem/Password-database-With-special-stuff
    ```

2. Install with poetry
    ```bash
        poetry install
    ```

3. Run using the following command.
    ```bash
        poetry run python src
    ```

## Usage

1. It is recommend to put these files in a folder only cointaing the program files, and to have an encryption key on a USB-Stick.

2. If you want "super security", I recommend using the program on a offline pc, or mini computer like a raspberry pi.

3. Before using this program, to enable database and encryption features run this command

    ```bash
    mkdir storage & mkdir encryption
    ```


## General Information

```python
        "database - opens the database interface."
        "password - opens the password interface."
        "help - displays this help message."
        "encryption - opens the encryption interface."
        "exit - exits the program."
        "settings - opens the settings interface"
```


## Contact

YouTube: https://www.youtube.com/channel/UCTHHIPTtETe6hawsfnZTM8A

Reddit: vapen_hem

Discord: vapen_hem#1161, nesta#4550
