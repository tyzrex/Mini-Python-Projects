# QR Code Generator

This is a simple QR code generator web application built using Flask, a micro web framework for Python. The application allows users to generate QR codes by inputting a piece of data (e.g. a website link) and displays the generated QR code on the webpage.

## Getting Started

### Prerequisites

* Python 3.9 or above
* Flask
* qrcode

First, install the required libraries by running the following command:

```bash
    pip install -r requirements.txt
```

To run the application, clone this repository and navigate to the root directory. Then, run the following command:

```bash
    python main.py
```

If you're on linux then enter the following command

```bash
    python3 main.py
```

The application will be running on http://localhost:5000/.

## Screenshots

![screenshot1](docs/screenshot.png)

![screenshot2](docs/sc2.png)

## Usage

Open the application in your browser by navigating to http://localhost:5000/

1. Input the data you want to encode in the QR code (e.g. a website link)
2. Click the "Generate" button
3. The generated QR code will be displayed on the webpage
4. If no data is inputted, the application will display an error message
   ![screenshot3](docs/sc3.png)

You can also test this by opening the web page and scan the QR code using your mobile phone.

## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - A micro web framework for Python
* [qrcode](https://pypi.org/project/qrcode/) - A Python library for generating QR codes
* [Pillow](https://pypi.org/project/Pillow/) - A Python library for handling images
* [Tailwind CSS](https://tailwindcss.com/) - A utility-first CSS framework for rapidly building custom user interfaces

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgments

* [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/) - A great resource for learning Flask
* [Tailwind CSS Documentation](https://tailwindcss.com/docs) - A great resource for learning Tailwind CSS
* [qrcode Documentation](https://pypi.org/project/qrcode/) - A great resource for learning how to use the qrcode library
