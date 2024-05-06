document.addEventListener('DOMContentLoaded', function() {
    // 登录逻辑
    var loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            console.log('Login Attempt:', email, password);
            alert('Login attempted for ' + email);
        });
    }

    // 注册逻辑
    var registerForm = document.getElementById('registerForm');
    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            event.preventDefault();
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

    // 初始化 Bootstrap Dropdown
    var dropdownElementList = [].slice.call(document.querySelectorAll('.dropdown-toggle'));
    var dropdownList = dropdownElementList.map(function (dropdownToggleEl) {
        return new bootstrap.Dropdown(dropdownToggleEl);
    });

    // 筛选逻辑
    function filterResults() {
        console.log("Filtering by:",
            document.getElementById('locationSelect').value,
            document.getElementById('priceMin').value,
            document.getElementById('priceMax').value);
        alert('Filters applied. Check console for details.');
    }

    // 实时显示时间
    function updateTime() {
        document.getElementById("currentTime").innerHTML = "Current Time: " + new Date().toLocaleString("en-AU", { timeZone: "Australia/Perth" });
    }
    setInterval(updateTime, 1000);  // 每秒更新时间

    // 天气
    const weatherButton = document.getElementById('weather-btn');
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

    // 滚动消息
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

    // for the contact form here
    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        alert('Thank you for contacting us!');
        // Here you might want to handle the form data, e.g., sending it to a server
    });
});


    // 跳转至 browse_items 页面的逻辑
    //const buyButton = document.querySelector('.btn-primary');
    //if (buyButton) {
        //buyButton.addEventListener('click', function() {
            //window.location.href = 'browse_items.html';
        //});
    //}

