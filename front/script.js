document.addEventListener('DOMContentLoaded', function() {
    const loginButton = document.querySelector('.login-button');
    const registerButton = document.querySelector('.register-button');
    const forgotPasswordButton = document.querySelector('.forgot-password-button');

    const loginForm = document.getElementById('login');
    const registerForm = document.getElementById('register');
    const confirmForm = document.getElementById('confirm');
    const forgotPasswordForm = document.getElementById('forgot-password');

    const registerFormSubmit = document.getElementById('registerForm');
    const codeInputs = document.querySelectorAll('.code-input');
    const timerElement = document.getElementById('timer');
    const sendAgainText = document.getElementById('sendAgain');

    let timer;
    let timeLeft = 59;
    let generatedCode = generateCode();

    loginButton.addEventListener('click', () => {
        loginForm.classList.remove('hidden');
        registerForm.classList.add('hidden');
        confirmForm.classList.add('hidden');
        forgotPasswordForm.classList.add('hidden');
        loginButton.classList.add('active');
        registerButton.classList.remove('active');
        forgotPasswordButton.classList.remove('active');
    });

    registerButton.addEventListener('click', () => {
        loginForm.classList.add('hidden');
        registerForm.classList.remove('hidden');
        confirmForm.classList.add('hidden');
        forgotPasswordForm.classList.add('hidden');
        loginButton.classList.remove('active');
        registerButton.classList.add('active');
        forgotPasswordButton.classList.remove('active');
    });

    forgotPasswordButton.addEventListener('click', () => {
        loginForm.classList.add('hidden');
        registerForm.classList.add('hidden');
        confirmForm.classList.add('hidden');
        forgotPasswordForm.classList.remove('hidden');
        loginButton.classList.remove('active');
        registerButton.classList.remove('active');
        forgotPasswordButton.classList.add('active');
    });

    // Переключение видимости пароля
    document.querySelectorAll('.toggle-password').forEach(icon => {
        icon.addEventListener('click', function() {
            const target = this.getAttribute('data-target');
            const passwordInput = document.getElementById(target);
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                this.classList.remove('fa-eye-slash');
                this.classList.add('fa-eye');
            } else {
                passwordInput.type = 'password';
                this.classList.remove('fa-eye');
                this.classList.add('fa-eye-slash');
            }
        });
    });
    forgotPasswordForm.addEventListener('submit', function(event) {
        event.preventDefault();
        forgotPasswordForm.classList.add('hidden');
        confirmForm.classList.remove('hidden');
        startTimer();
    });

    // Обработчик для формы логина
    document.querySelector('#login form').addEventListener('submit', function(e) {
        e.preventDefault();
        const overlay = document.createElement('div');
        overlay.className = 'page-transition';
        document.body.appendChild(overlay);
        setTimeout(() => {
            window.location.href = 'search.html';
        }, 500);
    });

    // Отправка формы регистрации
    registerFormSubmit.addEventListener('submit', function(event) {
        event.preventDefault();
        registerForm.classList.add('hidden');
        confirmForm.classList.remove('hidden');
        startTimer();
    });

    // Логика ввода кода
    codeInputs.forEach((input, index) => {
        input.addEventListener('input', () => {
            if (input.value.length === 1 && index < codeInputs.length - 1) {
                codeInputs[index + 1].focus();
            }
            if (Array.from(codeInputs).every(input => input.value.length === 1)) {
                checkCode();
            }
        });

        input.addEventListener('keydown', (e) => {
            if (e.key === 'Backspace') {
                if (input.value.length === 0 && index > 0) {
                    codeInputs[index - 1].value = '';
                    codeInputs[index - 1].focus();
                } else if (input.value.length === 1) {
                    input.value = '';
                    if (index > 0) codeInputs[index - 1].focus();
                }
            }
        });
    });

    // Таймер
    function startTimer() {
        clearInterval(timer);
        timeLeft = 59;
        timerElement.textContent = `00:59`;
        timerElement.style.display = 'block';
        sendAgainText.style.display = 'none';

        timer = setInterval(() => {
            timeLeft--;
            if (timeLeft <= 0) {
                clearInterval(timer);
                timerElement.style.display = 'none';
                sendAgainText.style.display = 'block';
            } else {
                const minutes = Math.floor(timeLeft / 60);
                const seconds = timeLeft % 60;
                timerElement.textContent = 
                    `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
            }
        }, 1000);
    }

    // Повторная отправка кода
    sendAgainText.addEventListener('click', () => {
        generatedCode = generateCode();
        startTimer();
    });

    // Проверка кода
    function checkCode() {
        const enteredCode = Array.from(codeInputs).map(input => input.value).join('');
        if (enteredCode === "123456") {
            const overlay = document.createElement('div');
            overlay.className = 'page-transition';
            document.body.appendChild(overlay);
            setTimeout(() => window.location.href = 'search.html', 500);
        } else {
            alert('Invalid code. Please try again.');
            codeInputs.forEach(input => input.value = '');
            codeInputs[0].focus();
        }
    }

    // Генерация кода
    function generateCode() {
        return Math.floor(100000 + Math.random() * 900000).toString();
    }
});

function validateNumber(input) {
    input.value = input.value.replace(/[^0-9]/g, '');
}