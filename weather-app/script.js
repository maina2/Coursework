// OpenWeatherMap API Key (Replace with your API key)
const apiKey = "YOUR_API_KEY";

document.getElementById("weather-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const city = document.getElementById("city").value;
  const weatherResult = document.getElementById("weather-result");

  // Clear previous results
  weatherResult.classList.add("hidden");
  weatherResult.innerHTML = "";

  try {
    // Fetch weather data
    const response = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`
    );

    if (!response.ok) {
      throw new Error("City not found");
    }

    const data = await response.json();

    // Populate weather details
    document.getElementById("city-name").textContent = `${data.name}, ${data.sys.country}`;
    document.getElementById("temperature").textContent = `Temperature: ${data.main.temp}°C`;
    document.getElementById("description").textContent = `Description: ${data.weather[0].description}`;
    document.getElementById("humidity").textContent = `Humidity: ${data.main.humidity}%`;

    weatherResult.classList.remove("hidden");
  } catch (error) {
    alert(error.message);
  }
});
