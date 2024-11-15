# AIRepublic_Day4

**RouteGuru** is designed specifically for parcel delivery drivers, offering AI-powered solutions to optimize delivery routes, save time, and enhance customer satisfaction. With its intelligent route-planning capabilities, RouteGuru ensures that every delivery is as efficient as possible, helping drivers navigate their day with ease. This project is part of the **Day4 Activity** in the **AI First Engineering Bootcamp**.

---

## Features

✨ **AI-Powered Route Optimization**  
RouteGuru uses advanced algorithms to analyze delivery data and generate the fastest and most efficient routes, saving valuable time and fuel. Whether you're delivering parcels across town of Metro Manila, RouteGuru ensures you're always on the best path.

💡 **Smart Delivery Prioritization**  
RouteGuru helps you prioritize deliveries based on customer needs, parcel urgency, and time constraints. Get suggestions for the best routes to follow, ensuring you meet delivery windows and optimize your schedule.

🤖 **AI-Assisted Chatbot**
RouteGuru includes an interactive chatbot that drivers can use to ask questions about their routes. Whether you're wondering about the optimal path to your next stop, estimated delivery times, or possible delivery delays based on historical data, the chatbot provides helpful answers and guidance. With this AI-powered assistant, you can get insights into your route and make informed decisions throughout the day.

---

## Technology

**RouteGuru** is built on advanced AI technologies, combining machine learning to optimize delivery processes. Powered by the OpenAI API for natural language processing and Streamlit for user interaction, RouteGuru makes route optimization both powerful and user-friendly.

### Getting Started

To run **RouteGuru** locally, clone this repository and install the necessary dependencies:

```bash
git clone https://github.com/noelabu/AIRepublic_Day4.git
cd AIRepublic_Day4
pip install -r requirements.txt
```

### API Key Configuration

#### 1. **OpenAI API Key**  
To use the OpenAI API for advanced route recommendations, you'll need an API key. Sign up at [OpenAI](https://openai.com) and create an API key. Store your key in an environment variable named `OPENAI_API_KEY`.

```bash
export OPENAI_API_KEY='your-openai-api-key'
```

#### 2. **Google Maps API Key**  
RouteGuru leverages the **Google Maps API** for routing, geolocation, and traffic updates. To use Google Maps for accurate route optimization, you'll need to sign up for a Google Cloud account and enable the **Google Maps Directions API** and **Google Maps Geocoding API**.

- **Sign up for Google Cloud**: [Google Cloud Console](https://console.cloud.google.com/)
- **Create a Project**: In your Google Cloud Console, create a new project.
- **Enable the APIs**: In your Google Cloud Console, navigate to "APIs & Services" and enable both the **Google Maps Directions API** and **Google Maps Geocoding API**.
- **Get your API Key**: In the "Credentials" section of the Google Cloud Console, create an API key and copy it.

Once you have your Google Maps API key, store it in an environment variable named `GOOGLE_MAPS_API_KEY`.

```bash
export GOOGLE_MAPS_API_KEY='your-google-maps-api-key'
```

### Running the Streamlit App
Once you've set up the API key, you can run the Streamlit app to interact with **RouteGuru**.

```bash
streamlit run app.py
```

Open your browser and go to `http://localhost:8501` to access the application. You can also access the live version [here](https://noelabu-routeguru.streamlit.app/).

---

## Contributing

Contributions to **RouteGuru** are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request.

---

## Acknowledgments

- OpenAI for providing the API that powers **RouteGuru's** intelligent features.
- All the delivery drivers for the inspiration and real-world use cases that drive the development of **RouteGuru**.

---


