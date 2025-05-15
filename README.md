# Weather Teller App

**Weather Teller App** is a Python desktop application that provides real-time weather information for any city entered by the user. It features a graphical user interface (GUI) built with Tkinter and displays weather data fetched from an online API.

## 🌦️ Features

- **City-Based Weather Search**: Enter any city to retrieve current weather information.
- **Graphical Display**: Visual representation of weather conditions.
- **User-Friendly Interface**: Simple and intuitive GUI for seamless user experience.

## 🛠️ Prerequisites

- **Python 3.x**
- **Required Libraries**:
  - `tkinter`
  - `requests`
  - `configparser`

*Note*: `tkinter` is usually included with standard Python installations. If not, it can be installed separately.

## 📦 Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/Vinayakrai/weather-teller-app.git
cd weather-teller-app
```

2. **Install Required Packages**:

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Then install the dependencies:

```bash
pip install requests
```

## 🚀 Usage

1. **Configure API Key**:

- Obtain an API key from a weather service provider (e.g., OpenWeatherMap).
- Open the `config.ini` file and replace `'your_api_key_here'` with your actual API key:

```ini
[weather]
api_key = your_api_key_here
```

2. **Run the Application**:

```bash
python weatherpredictor.py
```

- A GUI window will appear.
- Enter the desired city name and click the "Get Weather" button.
- The application will display the current weather information for the entered city.

## 📁 Project Structure

```
weather-teller-app/
├── weatherpredictor.py   # Main application script
├── config.ini            # Configuration file containing API key
└── README.md             # Project documentation
```

