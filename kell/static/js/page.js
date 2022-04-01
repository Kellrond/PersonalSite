var body = document.body; 
var element = document.getElementById("nav-bar"); 
//Update DOM on scroll 
document.addEventListener("scroll", function() {  
    var scrollAmt = window.pageYOffset || document.documentElement.scrollTop; 
	if(window.innerHeight/8 >= scrollAmt) 
	 	element.style.display = "none";  
  	else	 
		element.style.display = "block"; 
}); 