function closeAllElements() {
    document.querySelectorAll('.modal').forEach(modal => {
        modal.classList.remove('show');
    });
    
    const dropdown = document.getElementById('dropdown');
    dropdown.classList.remove('show');
}

document.querySelectorAll('.nav-button').forEach((button, index) => {
    button.addEventListener('click', (e) => {
        e.stopPropagation();
        const modalId = index === 0 ? 'aboutModal' : 'contactsModal';
        closeAllElements();
        document.getElementById(modalId).classList.add('show');
    });
});

function toggleDropdown() {
    closeAllElements();
    document.getElementById('dropdown').classList.toggle('show');
}

window.addEventListener('click', function(event) {
    if (!event.target.closest('.nav-button') && 
        !event.target.closest('.dropdown') && 
        !event.target.closest('.menu-icon')) {
        closeAllElements();
    }
});

// Поисковая строка и обработка запросов
const searchInput = document.getElementById('searchInput');
const responseBox = document.getElementById('responseBox');
const submitBtn = document.getElementById('submitBtn');

function autoResize(textarea) {
    textarea.style.height = 'auto';
    const maxHeight = 150;
    const newHeight = Math.min(textarea.scrollHeight, maxHeight);
    textarea.style.height = newHeight + 'px';
    textarea.style.overflowY = textarea.scrollHeight > maxHeight ? 'auto' : 'hidden';
}

searchInput.addEventListener('input', (e) => {
    autoResize(e.target);
});

function handleSubmit() {
    const query = searchInput.value.trim();
    if (!query) return;
    const simulatedResponse = "This is a simulated response for: " + query;
    
    typeResponse(simulatedResponse);
    searchInput.value = '';
    autoResize(searchInput);
}

// Отправка по клику
submitBtn.addEventListener('click', handleSubmit);

// Отправка по Enter
searchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleSubmit();
    }
});

// Анимация печати ответа
function typeResponse(text) {
    responseBox.innerHTML = '';
    let i = 0;
    function type() {
        if (i < text.length) {
            responseBox.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, 20);
        }
    }
    type();
}

function debounce(func, timeout = 300) {
    let timer;
    return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => { func.apply(this, args); }, timeout);
    };
}