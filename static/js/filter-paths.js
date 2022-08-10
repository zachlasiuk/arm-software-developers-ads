

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
            
            const all_path_cards = document.querySelectorAll('div.path-div');


            // iterate over all cards, get titles
            for (let card of all_path_cards) {
                let card_title = card.querySelector('.card-title').innerHTML.toLowerCase();

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



// ==========================================================
//                  Filter Behavior
// ==========================================================

function filterPaths(element) {
    // get status of checkbox (true for checked, false for unchecked)
    element.value().then((value) => {
        if (value === true) {
            const tags = element.classList.values();
            for (let tag of tags) {
                if (tag.includes('tag')) {
                    addTag(tag);
                    break;
                }
            }
        }
        else {
            const tags = element.classList.values();
            for (let tag of tags) {
                if (tag.includes('tag')) {
                    removeTag(tag);
                    break;
                }
            }
        }
    });
}


function addTag(tag) {
    // Check if facet exists for this already. If yes, ignore this erroneous press
    if (document.getElementById('filter-'+tag)) {
        return
    }
    console.log("adding tag: "+tag);

    // Display tag in 'current-tag-bar'
    display_tag = tag.replace('tag-','')
    document.querySelector('#current-tag-bar').insertAdjacentHTML(
        'afterbegin',
        `
        <ads-tag href="#" class="filter-facet" id="filter-${tag}">
            <span class="u-flex u-flex-row u-align-items-center u-gap-1/2">
                ${display_tag}
                <a onclick="removeTag('${tag}')">
                    <span class="fal fa-times-circle"></span>
                </a>
            </span>
        </ads-tag>
        `
    );


    // Filter paths by tag (hide if don't have tag and currently active) 
    let all_path_cards = document.querySelectorAll('div.path-div');
    for (let card of all_path_cards) {
        if (!card.classList.contains(tag)) { // if a card doesn't contain this tag, hide
            card.setAttribute('hidden',true);
        }
    }
}





function removeTag(tag) {
    // Check if facet does not exist. If it doesn't, ignore this erroneous press
    if (!document.getElementById('filter-'+tag)) {
        return
    }

    // Check if checkbox is now unchecked. If not, uncheck it.
    // get status of checkbox (true for checked, false for unchecked)
    const checkbox_element = document.querySelectorAll('ads-checkbox.'+tag)[0]
    checkbox_element.value().then((value) => { 
        if (value === true) {
            // uncheck it. NOT WORKING EXACTLY, but close enough.
            checkbox_element.setAttribute('checked',false);

            //console.log('influencing child dom '+checkbox_element.shadowRoot.querySelector('.c-checkbox__box'));
            //let box_ele = checkbox_element.shadowRoot.querySelector('.c-checkbox__box');
            //box_ele.classList.remove("is-checked")
            //box_ele.setAttribute('aria-checked',false)
        }
    });



    console.log("removing tag: "+tag);
    
    // Hide tag in 'current-tag-bar'
    document.getElementById('filter-'+tag).remove();

    // Re-show paths with tag if currently hidden 
    let all_path_cards = document.querySelectorAll('div.path-div');
    for (let card of all_path_cards) {
        if (!card.classList.contains(tag)) { // if a card doesn't contain this tag, hide
            //////////////////////////////////////
            //////// TAKE INTO ACCOUNT SEARCH
            card.removeAttribute('hidden');
        }
    }
    
}




function updateCardsToShow() {
    
}