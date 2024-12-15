# Jinx-Chatbot


A conversational AI chatbot built with Flask, utilizing the Gemini API for natural language processing and response generation. The chatbot is designed to interact with users in a conversational manner, providing useful and intelligent replies.

## Technologies Used

- **Flask**: A Python microframework used to build the backend of the chatbot.
- **Gemini API**: An API for natural language understanding and generation, used to power the chatbot’s conversational capabilities.
- **HTML**: Used for creating the structure of the chatbot interface.
- **CSS**: Used for styling the chatbot and its components.
- **JavaScript**: Provides dynamic interaction and communication between the frontend and backend of the chatbot.

## Features

- **Natural Language Processing**: The chatbot uses the Gemini API to process and respond to user inputs in a natural, conversational style.
- **Interactive UI**: A simple, user-friendly interface built with HTML, CSS, and JavaScript, allowing users to easily interact with the chatbot.
- **Real-time Communication**: Flask handles real-time communication with the Gemini API, sending and receiving messages dynamically.

## Setup Instructions

### Prerequisites

Before running this project, make sure you have the following installed on your local machine:

- Python 3.7+ 
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/maybemnv/jinx-chatbot.git
    cd jinx-chatbot
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Gemini API key:
   - Visit the Gemini API documentation and obtain your API key.
   - Create a `.env` file in the project root directory and add your API key:

    ```env
    GEMINI_API_KEY=your_api_key_here
    ```

5. Run the Flask application:

    ```bash
    flask run
    ```

    The application should now be live on [http://localhost:5000](http://localhost:5000).

### Frontend Usage

- The frontend is built with HTML, CSS, and JavaScript. It includes an input box for typing messages and displays chatbot responses in a chat interface.
- JavaScript handles the sending and receiving of messages via the Flask backend, which interacts with the Gemini API.


## Contributing

If you'd like to contribute to the project, feel free to fork the repository, make changes, and submit a pull request. Please make sure your code follows the project's coding standards and passes any tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify and expand this README according to your specific project needs. Let me know if you need further adjustments!


