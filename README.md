# AI Text CAPTCHA Solver

Some shitty code that uses Google’s Gemini API to automatically solve text-based CAPTCHA images and measure the time taken for each solution.

## Features

* Sends CAPTCHA images to Google Gemini API for OCR-based text extraction
* Measures and prints the time taken to solve each CAPTCHA

## Prerequisites

* Python 3.7 or later
* A Google Cloud project with the Gemini API enabled
* A valid Gemini API key

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/ai-captcha-solver.git
   cd ai-captcha-solver
   ```
2. Install required Python packages:

   ```bash
   pip install google-genai pillow
   ```

## Configuration

Edit the script to include your API key by replacing the placeholder:

```python
client = genai.Client(api_key="key")
```

## Usage

1. Place your CAPTCHA image in the directory (e.g., `captcha.png`).
2. Run the script:

   ```bash
   python solve.py
   ```
3. The script will output the extracted text and the time taken:

   ```text
   ABC123 - (time of solving)
   ```

## Example

```bash
$ python solve.py
XYZ789 - (time of solving)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.MD) file for details.
