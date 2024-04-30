document.addEventListener('DOMContentLoaded', function() {
    // 登录逻辑
    var loginForm = document.getElementById('loginForm');
    if(loginForm) {
        loginForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            console.log('Login Attempt:', email, password);

            // 这里可以添加实际的登录逻辑
            alert('Login attempted for ' + email);
        });
    }
    
    // 注册逻辑
    var registerForm = document.getElementById('registerForm');
    if(registerForm) {
        registerForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const fullName = document.getElementById('fullName').value;
            const email = document.getElementById('registerEmail').value; // 确保注册表单中的邮箱输入框的ID是唯一的
            const password = document.getElementById('registerPassword').value; // 确保注册表单中的密码输入框的ID是唯一的
            const confirmPassword = document.getElementById('confirmPassword').value; // 确保确认密码输入框的ID是唯一的

            // 检查密码是否匹配
            if (password !== confirmPassword) {
                alert('Passwords do not match. Please try again.');
                return; // 不提交表单
            }
            
            console.log('Registration Attempt:', fullName, email, password);

            // 这里可以添加实际的注册逻辑
            alert('Registration attempted for ' + fullName);
        });
    }
});
