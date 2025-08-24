# AI Text CAPTCHA Solver

Some shitty code that uses Google’s Gemini API to automatically solve text-based CAPTCHA.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DevFaded/AI-Text-Captcha-Solver.git
   cd AI-Text-Captcha-Solver
   ```
2. Install Python packages:

   ```bash
   pip install google-genai pillow
   ```

## Configuration

Edit the code to include your API key by replacing the placeholder:

```python
genai.configure(api_key="api")
```

## Usage

1. Place your CAPTCHA image in the directory (e.g., `captcha.png`).
2. Run the script:

   ```bash
   python solve.py
   ```
3. The script will print the text and the time taken:

   ```text
   ABC123 - (time of solving)
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.MD) file for details.
