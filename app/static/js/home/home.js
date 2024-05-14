// Product 1
document.addEventListener('DOMContentLoaded', function() {
  // Define all advertisement messages for Product 1
  const notificationsProduct1 = [
      "Unwrap the joy of savings with our spectacular holiday discounts on electronics!",
      "Festive deals: Up to 50% off on home appliances!",
      "Celebrate the new year with exclusive tech bargains!",
      "Season's greetings with special pricing on the latest gadgets!"
  ];

  let currentNotificationProduct1 = 0;  // Initial index for Product 1
  function rotateNotificationsProduct1() {
      // Update the displayed message for Product 1
      document.getElementById('notificationMessages1').innerHTML = `<p>${notificationsProduct1[currentNotificationProduct1]}</p><a href="#" class="btn btn-primary">Shop Now</a>`;
      // Calculate the index for the next message
      currentNotificationProduct1 = (currentNotificationProduct1 + 1) % notificationsProduct1.length;
  }

  // Change advertisement every 2000 milliseconds (2 seconds)
  setInterval(rotateNotificationsProduct1, 2000);
});

// Product 2
document.addEventListener('DOMContentLoaded', function() {
  // Define all advertisement messages
  const notifications = [
      "Flash Sale: Books at up to 40% off!",
      "Deal Alert: Furniture sets starting from $99!",
      "Weekend Special: 20% off on sports gear!",
      "Limited Time: 30% discount on selected clothing!"
  ];

  let currentNotification = 0;  // Initial index
  function rotateNotifications() {
      // Update the displayed message
      document.getElementById('notificationMessages').innerHTML = `<p>${notifications[currentNotification]}</p><a href="#" class="btn btn-primary">Shop Now</a>`;
      // Calculate the index for the next message
      currentNotification = (currentNotification + 1) % notifications.length;
  }

  // Change advertisement every 2000 milliseconds (2 seconds)
  setInterval(rotateNotifications, 2000);
});

// Product 4

document.addEventListener('DOMContentLoaded', function() {
  // Countdown timer for end-of-season sale
  function updateCountdown() {
      const endTime = new Date("December 31, 2024 23:59:59").getTime();
      const now = new Date().getTime();
      const distance = endTime - now;

      const days = Math.floor(distance / (1000 * 60 * 60 * 24));
      const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      const seconds = Math.floor((distance % (1000 * 60)) / 1000);

      // Updating the inner HTML of the countdown timer
      const countdownTimer = document.getElementById("countdown-timer");
      if (distance > 0) {
          countdownTimer.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s `;
      } else {
          clearInterval(interval);
          countdownTimer.innerHTML = "EXPIRED";
      }
  }

  // Start the countdown timer and update every second
  let interval = setInterval(updateCountdown, 1000);
});

document.addEventListener('DOMContentLoaded', function() {
  // Display current time
  function updateTime() {
      document.getElementById("currentTime").innerHTML = "Current Time: " + new Date().toLocaleString("en-AU", { timeZone: "Australia/Perth" });
  }
  setInterval(updateTime, 1000);  // Update time every second

  // Weather button event with Fetch API
  const weatherButton = document.getElementById('weather-btn');
  if (weatherButton) {
      weatherButton.addEventListener('click', function() {
          fetch("http://api.weatherapi.com/v1/current.json?key=your_api_key&q=Perth&aqi=no")
          .then(response => response.json())
          .then(data => {
              document.getElementById("weather").innerHTML = data.location.name;
              document.getElementById("temp").innerHTML = data.current.temp_c + " degrees,";
              document.getElementById("sunny").innerHTML = data.current.condition.text;
          })
          .catch(error => console.error('Error fetching weather data:', error));
      });
  }
});

