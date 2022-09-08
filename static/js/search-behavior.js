// ==========================================================
//                  Search Behavior
// ==========================================================
// SEARCHING
function implementSearch(search_string) {
    console.log('hi');
    console.log(search_string);

    // HANDLE if coming from search box (event) or URL (string)
    if (! (typeof search_string === 'string')) {
        search_string = search_string.value;
    }

    const search_word_array = search_string.toLowerCase().split(" ");
    const all_path_cards = document.querySelectorAll('div.search-div');

    // iterate over all cards, get titles
    for (let card of all_path_cards) {
        let card_title = card.querySelector('.search-title').innerHTML.toLowerCase();

        // Returns true if card_title includes all search terms in any order
        var serach_match = search_word_array.every(item => card_title.includes(item));
        if (!serach_match) {
            // hide card
            card.setAttribute('hidden',true);
        }
        else {
            // show card
            card.removeAttribute('hidden');
        }
    }
}

    // Assign this handler on page load
    (() => {

        const search_box = document.getElementById('search-box');
        search_box.inputChangeHandler = implementSearch;

        // Call implementSearch function if URL has parameters
        let url_str = window.location.search;

        if (url_str.includes('search=')) {
            // Split by & and get element that has 'search='
            let url_params = url_str.split('&');
            let search_str = url_params[url_params.findIndex(e => e.includes("search="))];
            
            // Remove '?', 'search=', and replace '+' with spaces leaving just the string.
            search_str = search_str.replaceAll('?','').replace('search=','').replaceAll('+',' ');
            // Again, for safety, strip all non numbers and letters
            search_str = search_str.replaceAll(/[^a-z A-Z 0-9]+/g, "");

            // Apply search
            search_box.setAttribute('search-value',search_str);
            implementSearch(search_str);
        }
    })();