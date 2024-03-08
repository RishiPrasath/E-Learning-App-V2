function updateField(fieldName) {
    const fieldValue = document.getElementById(`${fieldName}_field`).value;
    const updateMessageArea = document.getElementById(`${fieldName}-update-message`); 

    console.log('Updating field:', fieldName, 'with value:', fieldValue);

    fetch('/profile/update/', {  // URL of your update view
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token
        },
        body: JSON.stringify({
            username: '{{ user.username }}', // Pass the username 
            field_name: fieldName,
            new_value: fieldValue
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateMessageArea.textContent = data.message; 
            updateMessageArea.classList.add('success-message'); 
        } else {
            updateMessageArea.textContent = data.message; 
            updateMessageArea.classList.add('error-message'); 
        }
        // Optionally, clear the message after some seconds
    })
    .catch(error => {
        console.error('Error:', error);
        // Handle network errors
    });
}

function getCookie(name) { // Helper to get the CSRF token
    // ... (standard Django CSRF token retrieval logic) 
}