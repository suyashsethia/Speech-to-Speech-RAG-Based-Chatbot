## Speech-to-Speech Real-Time Seller Simulation

### Overview

The Speech-to-Speech Real-Time Seller Simulation is an AI-powered voice agent designed to mimic an experienced seller in real-time. It engages in natural, fluid conversations with customers, answering product-related queries with low latency, and providing expert recommendations based on user preferences. This project was developed for a hackathon by Flipkart.

The system leverages technologies such as retrieval-augmented generation (RAG), text-to-speech (TTS), speech-to-text (STT), and large language models (LLMs) to synthesize product information, market trends, and personalized customer interactions.

### Features

- **Real-Time Conversations**: Provides fast, responsive dialogue with low latency (<500ms) for a smooth user experience.
- **Contextual Understanding**: Maintains context throughout the conversation and answers queries about product features, pricing, availability, and comparisons.
- **Voice-Based Interface**: Users can speak directly to the agent, which responds in a natural and engaging manner, simulating a live seller.
- **Personalized Recommendations**: Offers tailored product recommendations based on customer preferences, browsing history, and interests.
- **Multiple Seller Personas**: Adapts to various seller personalities, such as an enthusiastic tech seller or a professional fashion consultant.
- **Data-Driven Responses**: Accesses product databases and synthesizes information from multiple sources, such as Flipkart, to answer queries accurately.
- **Negotiation Capabilities**: Engages in negotiation scenarios and offers deals or bundles based on customer interactions.

### Architecture

This project is built using multiple components and technologies, including:

1. **Speech-to-Text (STT)**: Captures live audio from customers and converts it to text using Google's Speech-to-Text API.
2. **Retrieval-Augmented Generation (RAG)**: Combines a retrieval mechanism with generative models to fetch relevant product data and generate responses in real-time.
3. **Text-to-Speech (TTS)**: Converts AI-generated responses back into natural-sounding speech using Google's Text-to-Speech API.
4. **Product Data Integration**: The agent draws product information from external sources, such as Flipkart's database, privacy policies, return policies, and other market-related documents.

### Technology Stack

- **LangChain**: Used for managing text splitting, document storage, and retrieval processes.
- **Google Cloud Speech-to-Text API**: For converting live speech input into text.
- **Google Cloud Text-to-Speech API**: For generating natural-sounding speech responses.
- **Hugging Face Generative Models**: Powering AI-generated text responses.
- **Vector Databases**: For storing and retrieving product documents in chunks for relevant context-based responses.
- **BeautifulSoup**: For web scraping product and policy data from HTML files.

### How It Works

1. **Data Processing**: Product-related data is collected, cleaned, and stored in a vector database. The documents are chunked to enable efficient retrieval based on customer queries.
2. **Speech Interaction**: The customer speaks a query (e.g., “Can you tell me about the latest phone deals on Flipkart?”), which is captured and transcribed using Google Speech-to-Text.
3. **Query Resolution**: The system retrieves relevant data from the vector database using a RAG approach, feeding it into a generative model to craft a coherent, human-like response.
4. **Speech Output**: The generated response is converted to speech using Google Text-to-Speech, completing the conversation in real time.

### Key Components

- **`document_search.ipynb`**: Contains the logic for processing product data, chunking text, and saving it to a vector database for future retrieval.
- **`first.py`**: Manages speech input from the user and handles the conversion between speech and text.
- **`reader.py`**: Handles the retrieval of product information and generates AI-driven responses.
- **`Frontend/main.py`**: The user interface for interacting with the system, facilitating real-time voice-based interactions.

### Judging Criteria

1. **Naturalness and Fluency**: Voice interactions should be smooth, avoiding robotic or unnatural speech patterns.
2. **Product Knowledge**: Responses must be accurate and showcase depth in product understanding.
3. **Low Latency**: System should respond quickly to maintain a seamless user experience.
4. **Contextual Consistency**: Maintains conversation context and seller persona across multiple interactions.
5. **Addressing Customer Concerns**: Effectively handles objections or queries raised by the customer.
6. **Personalization**: Offers relevant and personalized product recommendations.
7. **Seller Simulation Realism**: The system should convincingly simulate a human seller's behavior and knowledge.

### Installation

1. Clone the repository:
    
    ```bash
    bash
    Copy code
    git clone https://github.com/rathee-19/Speech-to-Speech-RAG-Based-Chatbot.git
    
    ```
    

### Usage

1. **Run the voice simulation**: The system will listen for speech input and respond with synthesized speech output.
    
    ```bash
    bash
    Copy code
    python first.py
    
    ```
    
2. **Data Retrieval and Processing**: You can process new product data or policies by running the `document_search.ipynb` notebook.
