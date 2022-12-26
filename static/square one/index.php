<!-- <?php
session_start();
if(!isset($_SESSION['loggedin']) || $_SESSION['loggedin']!=true){
    header("location: login.php");
    exit;
}

?> -->


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Home</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cabin&family=Ms+Madi&display=swap" rel="stylesheet"> 
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@600&family=Poppins:wght@700&display=swap" rel="stylesheet"> 
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Poppins:wght@300&display=swap" rel="stylesheet">
  

</head>
<body>

<?php
     include 'partials/navbar-bottom.php';
     ?>

  <div class="whole-content">
    <?php
     include 'partials/navbar.php';
      ?>

      
<div class="upper-centered-objects1" >
         
  
         <div class="search-box ">
           <input type="text" name="search" placeholder="Search for places, loaction, services" class="search-bar">
 
           <input type="submit" name="submit" class="search-icon " >
          
           
           
         </div>
 
       </div>

    <div class="coupon-container">
      <div class="coupon-page-content"><h1>THE SQUARE ONE</h1>
      <div class="list-coupon"><li>Opened Hours - 9:00AM to 7:30PM</li><li>Phone Number - 9371568293</li><li>Services Option - Dine in</li></div>
      <div class="location-coupon" >
      <input type="hidden" name="saddr" id="id1" value="Delhi">
      <button class="find-state" onclick="myFunction()" style="margin-left: 60px; "><img src="placeholder.png" style="height:20px;width:20px; "alt="">Get Direction</button>
      <button class="menu-show" id="myBtn" onclick="myFunction()" style="margin-left: 60px; "><img src="menu-icon1.png" style="height:20px;width:20px; margin-right: 5px;"alt="">Get Menu</button>
      <!-- The Modal -->
<div id="myModal" class="modal">

<!-- Modal content -->
<div class="modal-content">
  <span class="close">&times;</span>
  <img src="menu123.jpg" class="modal-image" alt="">
</div>

</div>
      </div>
      
    </div>
      <div class="image-in-coupon">
        <!-- <img src="sq1-cafe.png" style="height: 100%; width: 100%;"alt=""> -->
        <div class="content33 cropped-section" style="max-width:500px">
              <img class="mySlides" src="sq1-cafe.png" style="width:100%">
              <img class="mySlides" src="sq2-cafe.png" style="width:100%">
              <img class="mySlides" src="sq3-cafe.png" style="width:100%">
</div>
      </div>
      <div class="coupon-review"></div>
      <div class="coupon-id-container">

      <div class="coupon-id-1"><div class="discount-coupon-page">10</div><div class="discount-off">% <br>OFF</div><div class="heading-coupon-page">THE SQUARE ONE</div><input type="text" class="coupon-code-container" value="JT660A4I8K" readonly></div>
      <!-- <div class="coupon-code-container"><div class="use-code-button">USE <br>CODE</div></div> -->
      
      </div>

    </div>
       
      
      
         
      
    
    
      
  

    
      
    
    
       <div class="footer"></div>
    </div>
      
    </div> 

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

    
    
<script>
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
  setTimeout(carousel, 4000); // Change image every 4 seconds
}
// Get the modal
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
}</script>
<script src="index.js"></script>
</body>




</html>
