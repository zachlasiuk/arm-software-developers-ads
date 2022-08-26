// ==========================================================
//                  Search Behavior
// ==========================================================
    // Assign this handler on page load
    (() => {

        const search_box = document.getElementById('search-box');
        search_box.inputChangeHandler = (evt) => {
            console.log(evt.value);

            const search_string = evt.value;
            const search_word_array = search_string.toLowerCase().split(" ");
            
            const all_path_cards = document.querySelectorAll('div.search-div');


            // iterate over all cards, get titles
            for (let card of all_path_cards) {
                let card_title = card.querySelector('.search-title').innerHTML.toLowerCase();

                // Returns true if card_title includes all search terms in any order
                var serach_match = search_word_array.every(item => card_title.includes(item));
                if (!serach_match) {
                    // hide card
                    console.log('hiding: '+card_title)
                    card.setAttribute('hidden',true);
                }
                else {
                    // show card
                    card.removeAttribute('hidden');
                }
            }
        };

    })();