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
    )
    // Filter paths by tag (hide if don't have tag and currently active) 
}


function removeTag(tag) {
    // Check if facet does not exist. If it doesn't, ignore this erroneous press
    if (!document.getElementById('filter-'+tag)) {
        return
    }
    console.log("removing tag: "+tag);
    
    // Hide tag in 'current-tag-bar'
    document.getElementById('filter-'+tag).remove();

    // Re-show paths with tag if currently hidden 
}

function removeRow(tag) {
    tag.parentNode.remove(); // best option! Only works with 'this' though, not the tag itself.
    document.getElementById('current-tag-bar').removeChild(input.parentNode);
}