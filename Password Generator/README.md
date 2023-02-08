# Password Generator

This project implements a password generator that generates a password of specified length and type (alphanumeric, letters, or digits). The password is generated using Python's `secrets` module and the `string` module.

## Usage

To use the password generator, simply run the `password_generator.py` script. You will be prompted to either use default settings or customize the password length and type. If you choose to customize the password, you will be asked to enter the password length and choose the password type from the options (alphanumeric, letters, or digits).

## Requirements

This project requires the following packages:

* `pyfiglet`
* `simple-term-menu`

To install these packages, run the following command in your terminal:

```
pip install pyfiglet simple-term-menu
```

### Future Work

* Add more options for password complexity, such as adding uppercase letters, special characters, etc.
* Implement a GUI for the password generator for a more user-friendly experience.
