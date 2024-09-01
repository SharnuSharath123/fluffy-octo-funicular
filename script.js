document.getElementById('funFactButton').addEventListener('click', function() {
    fetch('/fun-fact')
        .then(response => response.json())
        .then(data => {
            document.getElementById('message').textContent = data.fact;
        });
});
