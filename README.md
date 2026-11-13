# AI Website Summarizer 🌐

A simple Python project that extracts text from a website and uses a locally running AI model to generate a short and meaningful summary.

The project uses **BeautifulSoup** to extract website content and **Ollama** to process that content using the Llama 3.2 (1B) model.

## 🚀 Features

- Takes a website URL as user input.
- Fetches website content using Python's `requests` library.
- Extracts the page title and main text using BeautifulSoup.
- Removes unnecessary elements such as scripts, styles, images, and input fields.
- Uses a locally running AI model to summarize the extracted content.
- Displays the summary in Markdown format.

## 🛠️ Technologies Used

- **Python** – Main programming language.
- **Requests** – Fetches website content.
- **BeautifulSoup4** – Parses HTML and extracts text.
- **Ollama** – Runs the AI model locally.
- **Llama 3.2 (1B)** – Generates website summaries.

## 📂 Project Structure

```text
AI-Website-Summarizer/
│
├── main.py
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd AI-Website-Summarizer
```

### 3. Install the required libraries

```bash
pip install requests beautifulsoup4 ollama
```

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com/

### 5. Download the AI model

Open your terminal and run:

```bash
ollama pull llama3.2:1b
```

Make sure Ollama is running before executing the Python program.

## ▶️ How to Run

Run the following command:

```bash
python main.py
```

Enter the URL of the website you want to summarize.

Example:

```text
Enter the website URL you want to summarise:
https://www.python.org/
```

The program will fetch the website content, process it using the AI model, and display a short summary.

## 📚 What I Learned

While building this project, I got practical experience with:

- Working with external Python libraries.
- Sending HTTP requests using `requests`.
- Extracting and parsing HTML using BeautifulSoup.
- Understanding Python classes and objects.
- Working with local AI models through Ollama.
- Creating prompts for AI models.
- Combining web scraping with AI-powered text summarization.

## 🔮 Future Improvements

- Add support for summarizing multiple websites.
- Improve error handling for invalid URLs.
- Extract only the main article content.
- Add a graphical user interface (GUI).
- Save generated summaries into text files.

## 👨‍💻 Author

Built as part of my Python learning journey.

More Python projects and experiments coming soon!