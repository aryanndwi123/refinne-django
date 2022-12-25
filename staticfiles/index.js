var findMyState =() =>{
    

    var success=(position)=>{
        console.log(position)
        var latitude =position.coords.latitude;
        var longitude = position.coords.longitude;
        console.log(latitude +''+longitude)
        document.getElementById('id1').value = latitude+' '+longitude;
        location.replace('https://www.google.com/maps?saddr='+latitude+','+longitude+'&daddr=The+square+one+cafe')
        
        
    }
    

    navigator.geolocation.getCurrentPosition(success);
    
    
}



document.querySelector('.find-state').addEventListener('click',findMyState);


var myIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}    
  x[myIndex-1].style.display = "block";  
  setTimeout(carousel, 4000); // Change image every 2 seconds
}


function infiniteSlider(){
  var count;
  var b = document.getElementsByClassName("bg_slider");
  for(count=0; count < 100;count++){
    
  }
}

function dropdownBtn(){
  dropdowncontent.style.display = "block";

}


var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}