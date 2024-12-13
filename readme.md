# Movie Weather API

## **Overview**
This project is a Flask-based API that integrates movie and weather data. The service allows users to query information about a movie and retrieve details such as the title, genres, and the weather conditions (maximum and minimum temperatures) for the city of Medellin, Colombia on the movie's release date.

### **Features**
- Fetches movie details by query using external movie APIs.
- Retrieves historical weather data for the movie's release date.
- Middleware sends the response data to a webhook after successful processing.
- Handles missing movie or weather data gracefully.

---

## **Endpoints**

### **GET `/movie-info`**
Retrieves movie details and weather information for the movie's release date.

#### Query Parameters:
- `query` (required): The name of the movie to search for.

#### Example Request:
```http
GET /movie-info?query=avatar
```

#### Example Successful Response:
```json
{
  "title": "Avatar",
  "genres": ["Action", "Adventure", "Fantasy", "Science Fiction"],
  "maxTemp": 25.5,
  "minTemp": 15.1
}
```

#### Error Responses:
- **400**: Missing query string.
  ```json
  { "error": "Query string is required" }
  ```
- **404**: No movies or weather data found.
  ```json
  { "error": "No movies found" }
  ```

---

## **How to Run the Project**

### **1. Install Python**
Ensure you have Python installed. You can download it from the [official Python website](https://www.python.org/).

### **2. Clone the Repository**
```bash
git clone https://github.com/dcalled/weather-movies
cd weather-movies
```

### **3. Set Up the Virtual Environment**
Create and activate a virtual environment:

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### **4. Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

### **5. Set Up Environment Variables**
Copy the provided `.env.example` file to create your `.env` file:
```bash
cp .env.example .env
```
Edit the `.env` file and replace placeholders with your actual values.

### **6. Run the Application**
Start the Flask development server:
```bash
flask run
```

The API will be available at `http://127.0.0.1:5000`.

### **7. (Optional) Run the Webhook Receiver**
If you want to test the webhook functionality, you can set up a webhook receiver on another port.

#### Example Webhook Receiver:
```bash
python webhook.py
```

---

## **Environment Variables**
- **The `.env` file is mandatory. Use the `.env.example` file as a template.**
  ```plaintext
  MOVIEDB_ACCESS_TOKEN=your_token_here
  ```

---

## **Files Overview**

- `app/`
  - `__init__.py`: Initializes the Flask app.
  - `routes.py`: Defines the API routes.
  - `movies.py`: Handles movie API logic.
  - `weather.py`: Handles weather API logic.
- `run.py`: Entry point to run the Flask app.
- `requirements.txt`: Lists project dependencies.
- `.env.example`: Example file for environment variables.
- `.env`: Environment variables for configuration.

---

## **Future Improvements**
- Add authentication for secured API access.
- Implement asynchronous webhook calls.
- Expand endpoints for additional movie or weather data.
- Add more robust error handling and logging.

---

## **License**
This project is licensed under the MIT License. See `LICENSE` for details.

