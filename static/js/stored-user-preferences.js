(() => {
      // Always check local storage to keep these attributes constant:
        // Theme  (light, dark)
        // Width  (is-full-width)
        // Height (expanded-masthead and contextual data)
    	//Check Storage. Keep user preference on page reload

	if (localStorage.getItem('lightMode')) {
        document.querySelector('html').setAttribute('theme', 'light');
        document.getElementById('prism-code-theme').href='/css/prism-light.css';
	} 
  if (localStorage.getItem('fullWidth')) {
        document.getElementById("all-content-div").classList.add("is-full-width");
	} 
  if (localStorage.getItem('fullHeight')) {
    document.getElementById('global-nav-example-default').contextualData = []; // Hide seoncary nav on Global Nav         
    document.getElementById("expanded-masthead").setAttribute('hidden',true);  // Hide title
  } 


  })();




