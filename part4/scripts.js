document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const placesList = document.getElementById('places-list');
    const priceFilter = document.getElementById('price-filter');

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            const response = await fetch('https://your-api-url/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });

            if (response.ok) {
                const data = await response.json();
                document.cookie = `token=${data.access_token}; path=/`;
                window.location.href = 'index.html';
            } else {
                alert('Login failed!');
            }
        });
    }

    async function fetchPlaces() {
        if (!placesList) return;
        const token = getCookie('token');
        
        const loginLink = document.getElementById('login-link');
        if (token && loginLink) loginLink.style.display = 'none';

        const response = await fetch('https://your-api-url/places');
        const places = await response.json();
        displayPlaces(places);
    }

    function displayPlaces(places) {
        placesList.innerHTML = '';
        places.forEach(place => {
            const card = document.createElement('div');
            card.className = 'place-card';
            card.setAttribute('data-price', place.price_per_night);
            card.innerHTML = `
                <h3>${place.name}</h3>
                <p>Price: $${place.price_per_night}</p>
                <a href="place.html?id=${place.id}" class="details-button">View Details</a>
            `;
            placesList.appendChild(card);
        });
    }

    if (priceFilter) {
        priceFilter.addEventListener('change', (e) => {
            const maxPrice = e.target.value;
            const cards = document.querySelectorAll('.place-card');
            cards.forEach(card => {
                const price = parseInt(card.getAttribute('data-price'));
                if (maxPrice === 'All' || price <= parseInt(maxPrice)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    }

    fetchPlaces();
});
async function fetchPlaceDetails(placeId) {
    const token = getCookie('token');
    const response = await fetch(`https://your-api-url/places/${placeId}`);
    const place = await response.json();

    const infoSection = document.getElementById('place-info');
    infoSection.innerHTML = `
        <h1>${place.name}</h1>
        <p><strong>Host:</strong> ${place.host_name}</p>
        <p><strong>Price:</strong> $${place.price_per_night}</p>
        <p><strong>Description:</strong> ${place.description}</p>
        <p><strong>Amenities:</strong> ${place.amenities.join(', ')}</p>
    `;

    const reviewsContainer = document.getElementById('reviews-container');
    place.reviews.forEach(review => {
        const reviewCard = document.createElement('div');
        reviewCard.className = 'review-card';
        reviewCard.innerHTML = `
            <p>"${review.comment}"</p>
            <p><strong>- ${review.user_name}</strong> (Rating: ${review.rating}/5)</p>
        `;
        reviewsContainer.appendChild(reviewCard);
    });

    if (token) {
        document.getElementById('add-review').style.display = 'block';
        document.getElementById('add-review-button').href = `add_review.html?id=${placeId}`;
    }
}

const reviewForm = document.getElementById('review-form');
if (reviewForm) {
    reviewForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const token = getCookie('token');
        const params = new URLSearchParams(window.location.search);
        const placeId = params.get('id');

        if (!token) {
            window.location.href = 'index.html';
            return;
        }

        const comment = document.getElementById('review-text').value;
        const rating = document.getElementById('review-rating').value;

        const response = await fetch('https://your-api-url/reviews', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ place_id: placeId, comment, rating })
        });

        if (response.ok) {
            alert('Review added!');
            window.location.href = `place.html?id=${placeId}`;
        } else {
            alert('Error adding review');
        }
    });
}