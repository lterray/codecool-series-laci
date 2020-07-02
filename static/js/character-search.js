function init() {
    let searchButton = document.querySelector('#character-search-button');
    searchButton.addEventListener('click', function () {
        let phrase = document.querySelector('#phrase').value;

        fetch(searchButton.dataset.url + '?phrase=' + phrase)
          .then(response => response.json())
          .then(data => showCharacters(data));
    });
}

function showCharacters(characters) {
    let list = document.querySelector('#search-result');
    let charactersHtml = '';

    for (let character of characters) {
        charactersHtml += `
            <li>
                ${character.character_name},
                ${character.name},
                ${character.title}
            </li>
        `;
    }

    list.innerHTML = charactersHtml;
}

init();