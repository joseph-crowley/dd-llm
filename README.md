# Fat Tailed DD Chat: Blueprint AI Protocol Assistant

## Overview

**Fat Tailed DD Chat** is an intelligent assistant designed to answer user queries based on the high-quality information and protocols from the **Blueprint Protocol**. This Flask-based application uses OpenAI's GPT models to deliver structured, concise, and actionable responses. The assistant can cite relevant sources directly, making it ideal for users who seek accurate and reliable information.

---

## Features

- **Interactive Chat Interface**: Users can ask questions and get precise, source-backed responses.
- **Source Citation**: Provides relevant excerpts and links from Blueprint Protocol documents.
- **Markdown to HTML Converter**: Renders source files in a clean and readable format.
- **Dynamic Chat Window**: Designed with Bootstrap for responsive design and user-friendly interaction.
- **Blueprint Protocol Integration**: Uses preloaded Markdown files as source context.

---

## Requirements

- Python 3.8+
- Flask
- OpenAI Python SDK
- Bootstrap (via CDN)
- jQuery (via CDN)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/joseph-crowley/dd-llm.git
   cd dd-llm
   ```

2. **Set up Python environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Set environment variables**:
   Ensure you have an OpenAI API key. Set it as an environment variable:
   ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the app**:
   Open your browser and navigate to `http://127.0.0.1:5000`.

---

## Usage

### Chatting with the Assistant
1. Open the application in your browser.
2. Type your query in the input field and click **Send**.
3. The assistant will respond with concise and protocol-based answers, citing relevant sources if applicable.

### Viewing Sources
- Each response citing a source includes a "Source" button. Click it to view the relevant information.

---

## Project Structure

```plaintext
dd-llm/
├── app.py                # Flask application entry point
├── main.py               # Chat logic and OpenAI integration
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # Chat interface (HTML + JS)
├── static/               # Static assets (e.g., Bootstrap, CSS)
├── sources/              # Markdown files with protocol information
└── README.md             # Project documentation
```

---

## Development Notes

### Markdown-to-HTML Conversion
- The application includes a utility function to render Markdown files (`sources/*.md`) as HTML, ensuring consistent formatting.

### Chat Logic
- The `main.py` file defines the core logic for interacting with the OpenAI API using structured prompts.
- The assistant ensures responses adhere strictly to the Blueprint Protocol.

### Frontend Design
- A dynamic and modern chat interface is built using **Bootstrap** and **jQuery**.

---

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message"
   ```
4. Push your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Create a pull request.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contact

For questions or suggestions, contact [Joseph Crowley](mailto:joseph@example.com) or visit [FatTailed.ai](https://fattailed.ai).
