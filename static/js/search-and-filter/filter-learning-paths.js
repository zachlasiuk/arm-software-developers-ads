function filter_LearningPath_card(card) {
    let to_hide = true;             // set as true by default; change to false if ALL filters apply

    // iterate over all active filters in the dom area; if this card matches ALL of the tags, keep shown
    const active_tags = document.getElementsByClassName('filter-facet');
    if (active_tags.length==0) { return false }        // Return already if no tags...no filtering neccecary 

    for (tag of active_tags) {
        let active_tag_name = tag.id.replace('filter-',''); // tag.id = filter-tag-databases   strip off 'tag-'
        if (card.classList.contains(active_tag_name)) {
            // DO NOT hide this card as it matches an active tag!
            to_hide = false;
        }        
        else {
            // If here, at least one tag doesn't match. Return true, meaning hide it
            return true
        }
    }

    return to_hide
}




function removeFacet(tag) {
    const all_path_cards = document.querySelectorAll('div.search-div');
     //////// Remove Facet
     document.getElementById('filter-'+tag).remove();

    ////////// Uncheck checkbox if applicable
        // get status of checkbox (true for checked, false for unchecked)
        const checkbox_element = document.querySelectorAll('ads-checkbox.'+tag)[0]
        checkbox_element.value().then((value) => { 
            if (value === true) {
                // uncheck it. NOT WORKING EXACTLY, but close enough.
                checkbox_element.removeAttribute('checked');
            }
        });

    // Apply search and filters to current parameters
        // deal with ads promise
        document.getElementById('search-box').value().then((value) => { 
             results_to_hide = applySearchAndFiltersTo_LearningPaths(all_path_cards, value); // apply active search & filter terms to the specified divs
             hideElements(all_path_cards,results_to_hide);
            },
        );

}

function addFacet(element) {
    const all_path_cards = document.querySelectorAll('div.search-div');

     //////// Add Facet
     // Get 'tag' and 'display_tag'
     let tag = null;
     const tags = element.classList.values();
     for (let t of tags) {
         if (t.includes('tag')) {
             tag = t;
             break;
         }
     };
     display_tag = element.id;
     document.querySelector('#current-tag-bar').insertAdjacentHTML(
         'beforeend',
         `
         <ads-tag href="#" class="filter-facet u-margin-left-1/2" id="filter-${tag}">
             <span class="u-flex u-flex-row u-align-items-center u-gap-1/2">
                 ${display_tag}
                 <a onclick="removeFacet('${tag}')">
                     <span class="fal fa-times-circle"></span>
                 </a>
             </span>
         </ads-tag>
         `
     );

     // Apply search and filters to current parameters
        // deal with ads promise
        document.getElementById('search-box').value().then((value) => { 
             results_to_hide = applySearchAndFiltersTo_LearningPaths(all_path_cards, value); // apply active search & filter terms to the specified divs
             hideElements(all_path_cards,results_to_hide);
            },
        );
}









function filterHandler_LearningPaths(element) {
    /*      Called from ads-checkbox components themselves, triggered from a user press on checkbox        
                Update facets to appear
                Apply only updated filter to search results (show what isn't that matches & vice versa)
    */
        const all_path_cards = document.querySelectorAll('div.search-div');
    
        // get status of checkbox (true for checked, false for unchecked)
        element.value().then((value) => {
            if (value === true) {
                // add 'checked' value to html
               addFacet(element,all_path_cards);
            }
            else {
                //?????????????????????????????????????????????????????????????????????????
                // This is being called when there is no facet. Strange behaivor with checkbox value being set strangely
                // ADS team to fix this problem.
                let tag = null;
                const tags = element.classList.values();
                for (let t of tags) {
                    if (t.includes('tag')) {
                        tag = t;
                        break;
                    }
                };
               removeFacet(tag);
            }
        });
    }