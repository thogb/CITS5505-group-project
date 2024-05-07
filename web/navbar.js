document.addEventListener('DOMContentLoaded', function() {
    // Login logic
    var loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            console.log('Login Attempt:', email, password);
            alert('Login attempted for ' + email);
        });
    }

    // Registration logic
    var registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission
            const fullName = document.getElementById('fullName').value;
            const email = document.getElementById('registerEmail').value;
            const password = document.getElementById('registerPassword').value;
            const confirmPassword = document.getElementById('confirmPassword').value;

            if (password !== confirmPassword) {
                alert('Passwords do not match. Please try again.');
                return;
            }

            console.log('Registration Attempt:', fullName, email, password);
            alert('Registration attempted for ' + fullName);
        });
    }

    // Help link scroll logic
    var helpLink = document.querySelector('a[href="#contact"]');
    if (helpLink) {
        helpLink.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior
            scrollToContact(); // Call scroll function
        });
    }

    // Function: Scroll to a specific part of the page
    function scrollToContact() {
        const contactSection = document.getElementById('contact');
        if (contactSection) {
            contactSection.scrollIntoView({ behavior: 'smooth' });
        } else {
            console.error('Contact section not found.');
        }
    }

    // Display current time
    function updateTime() {
        document.getElementById("currentTime").innerHTML = "Current Time: " + new Date().toLocaleString("en-AU", { timeZone: "Australia/Perth" });
    }
    setInterval(updateTime, 1000);  // Update time every second

    // Weather button event
    const weatherButton = document.getElementById('weather-btn');
    if (weatherButton) {
        weatherButton.addEventListener('click', function() {
            var weather = new XMLHttpRequest();
            weather.open("GET", "http://api.weatherapi.com/v1/current.json?key=422b3a5080c240e6a0825344231404&q=Perth&aqi=no", false);
            weather.send(null);

            var weatherdata = JSON.parse(weather.response);

            var curlocation = weatherdata.location.name;
            var temp = weatherdata.current.temp_c + " degrees,";
            var sunny = weatherdata.current.condition.text;

            document.getElementById("weather").innerHTML = curlocation;
            document.getElementById("temp").innerHTML = temp;
            document.getElementById("sunny").innerHTML = sunny;
        });
    }

    // Rotate notifications
    const notifications = [
        "Special Offer: Get 50% off on all electronics!",
        "Flash Sale: Books at up to 40% off!",
        "Deal Alert: Furniture sets starting from $99!",
        "Weekend Special: 20% off on sports gear!",
        "Limited Time: 30% discount on selected clothing!"
    ];

    let currentNotification = 0;
    function rotateNotifications() {
        document.getElementById('notificationMessages').innerHTML = `<p>${notifications[currentNotification]}</p>`;
        currentNotification = (currentNotification + 1) % notifications.length;
    }
    setInterval(rotateNotifications, 2000); // Change advertisement every 2 seconds

    // WebSocket connection
    const socket = new WebSocket('ws://localhost:3000');
    socket.addEventListener('open', function(event) {
        socket.send('Hello Server!');
    });
    socket.addEventListener('message', function(event) {
        console.log('Message from server:', event.data);
        document.getElementById('notificationArea').innerHTML += `<p>${event.data}</p>`;
    });

    // Countdown timer for end-of-season sale
    function updateCountdown() {
        const endTime = new Date("December 31, 2024 23:59:59").getTime();
        const now = new Date().getTime();
        const distance = endTime - now;

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById("countdown-timer").innerHTML = days + "d " + hours + "h "
        + minutes + "m " + seconds + "s ";

        if (distance < 0) {
            clearInterval(x);
            document.getElementById("countdown-timer").innerHTML = "EXPIRED";
        }
    }
    let x = setInterval(updateCountdown, 1000); // Update countdown every second
});
