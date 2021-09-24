---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
permalink: /
---
<link rel="stylesheet" href="MyWeb/assets/css/styles.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<!-- Navigation bar -->
<nav>
		<uln id="mainMenu">
        <lin><a class="active" href="{{site.baseurl}}/Home/">Home</a></lin>
        <lin><a href="/Events/">Events</a></lin>
        <lin><a>Activities</a>
            <uln>
                <lin><a href="/Activities/Courses/" style= "width: 130px;">Courses</a></lin>
                <lin><a href="/Activities/Workshops/" style= "width: 130px;">Workshops</a></lin>
                <lin><a href="/Activities/Internships/" style= "width: 130px;">Internships</a></lin>
            </uln>
        </lin>
        <lin><a href="/Competitions/">Competitions</a></lin>
        <lin><a href="https://www.ieee.org/membership/join/index.html?WT.mc_id=hc_join" target="_blank">Join IEEE</a></lin>
        <lin><a href="/MembersBenefits/">Members Benefits</a></lin>
        <lin><a href="/Gallery/">Gallery</a></lin>
        <lin><a>About Us</a>
            <uln>
                <lin><a href="/about/Vision_Goal/" style= "width: 130px;">Vision & Goal</a></lin>
                <lin><a href="/about/Board/" style= "width: 130px;">Our Board</a></lin>
                <lin><a href="/about/Members/" style= "width: 130px;">Members</a></lin>
                <lin><a href="/about/Sponsors/" style= "width: 130px;">Sponsors</a></lin>
                <lin><a href="/about/Partners/" style= "width: 130px;">Partners</a></lin>
            </uln>
        </lin>        <!-- <a href="javascript:void(0);" class="icon" onclick="myFunction()"> -->
    <!-- <i class="fa fa-bars"></i> -->
    </uln>
</nav>
<br><br><br><br><br><br>
<!-- Slideshow container -->
<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <div class="numbertext">1 / 3</div>
    <img src="{{site.baseurl}}/assets/Images/Dragons i4.0 camp.png" style="width:100%; height:100%;" >
    <br>
    <div class="text">AEMC 2021</div>
  </div>
  <div class="mySlides fade">
    <div class="numbertext">2 / 3</div>
    <img src="{{site.baseurl}}/assets/Images/AEMC-web.png" style="width:100%; height:100%;">
    <br>
    <div class="text">Egyptian Engineering Day</div>
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 3</div>
    <img src="{{site.baseurl}}/assets/Images/EED Website.png" style="width:100%; height:100%;">
    <br>
    <div class="text">Caption Three</div>
  </div>
  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
<br>
<!-- The dots/circles -->
<div style="text-align:center">
  <span class="dot" onclick="currentSlide(1)"></span>
  <span class="dot" onclick="currentSlide(2)"></span>
  <span class="dot" onclick="currentSlide(3)"></span>
</div>

<!-- Content -->
# Latest Articles
<hr class="new1">
Coming soon
<br><br><br><br>

# Latest Events Highlights

<hr class="new1">

<div class="slideshow-container2">
  <!-- Full-width images with number and caption text -->
  <div class="mySlides2 fade">
    <div class="numbertext">1 / 3</div>
    <img src="{{site.baseurl}}/assets/Images/Cybersecurity-web.png" style="width:100%; height:100%;" >
    <div class="text">Caption Text</div>
  </div>
  <div class="mySlides2 fade">
    <div class="numbertext">2 / 3</div>
    <img src="{{site.baseurl}}/assets/Images/Infosession-web.png" style="width:100%; height:100%;">
    <div class="text">Caption Two</div>
  </div>
  <div class="mySlides2 fade">
    <div class="numbertext">3 / 3</div>
    <img src="{{site.baseurl}}/assets/Images/Deeplearningforselfdrivingcars.png" style="width:100%; height:100%;">
    <div class="text">Caption Three</div>
  </div>
  <!-- Next and previous buttons -->
  <a class="prev2" onclick="plusSlides2(-1)">&#10094;</a>
  <a class="next2" onclick="plusSlides2(1)">&#10095;</a>
</div>
<br>
<!-- The dots/circles -->
<div style="text-align:center">
  <span class="dot2" onclick="currentSlide2(1)"></span>
  <span class="dot2" onclick="currentSlide2(2)"></span>
  <span class="dot2" onclick="currentSlide2(3)"></span>
</div>

# The Buzz

<hr class="new1">

<img src="{{site.baseurl}}/assets/Images/Magazine Cover Website.png" alt="The Buzz Magazine" style= "border-right: 6px solid #0074D9; float: left; padding-right: 10px; margin-right: 20px;"/>

* <a href="" target="_blank" style="font-size:25px">The Buzz #E1</a>
* <a href="" target="_blank" style="font-size:25px">Submit an article</a>
* <a href="" target="_blank" style="font-size:25px">Article guidlines</a>

<aside id="sidebar">
  <a style= "font-size: 20px;">Branch Calendar</a>
  <hr class="new1">
  <div class="events-container">
        <span class="events__title">Upcoming events</span>
        <ul class="events__list">
          <li class="events__item">
            <div class="events__item--left">
              <span class="events__name">Dragons i4.0 Camp & Summit</span>
              <span class="events__date">Sep 30</span>
            </div>
            <span class="events__tag">9:00</span>
          </li>
          <li class="events__item">
            <div class="events__item--left">
              <span class="events__name">AEMC 2021</span>
              <span class="events__date">Oct 6</span>
            </div>
            <span class="events__tag">10:00</span>
          </li>
          <li class="events__item">
            <div class="events__item--left">
              <span class="events__name">Egyptian Engineering Day</span>
              <span class="events__date">Oct 15</span>
            </div>
            <span class="events__tag">16:00</span>
          </li>
        </ul>
  </div>
</aside>

<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<!-- Footer -->
<footer class="footer-distributed">
  <div class="footer-left">
    <h3>IEEE<span>E-JUST SB</span></h3>
    <p class="footer-links">
      <a href="/index/">Home</a>
      <a href="/Activities/">Activities</a>
      <a href="/JoinIEEE/">Join IEEE</a>
      <a href="/Gallery/">Gallery</a>
      <a href="/about/">About Us</a>
    </p>
    <p class="footer-company-name">IEEE E-JUST SB &copy; 2019</p>
  </div>
  
  <div class="footer-center">
    <div>
      <i class="fa fa-map-marker"></i>
      <p><span>Hod Sakrah WA Abu Hamad, Borg Al Arab Al Gadida City</span> Alexandria, Egypt</p>
    </div>
    <div>
      <i class="fa fa-phone"></i>
      <p>+201201984321</p>
    </div>
    <div>
      <i class="fa fa-envelope"></i>
      <p><a href="mailto:ieee@ejust.edu.eg">ieee@ejust.edu.eg</a></p>
    </div>
    
  </div>
  
  <div class="footer-right">
    <p class="footer-company-about">
      <span>About US</span>
      IEEE E-JUST SB is a branch that aims to develop engineers academically, tecnically and personally to better our world.
    </p>
    <div class="footer-icons">
      <a href="https://www.facebook.com/IEEE.EJUST/" target="_blank"><i class="fa fa-facebook"></i></a>
      <a href="https://www.linkedin.com/company/ieee-e-just-sb/" target="_blank"><i class="fa fa-linkedin"></i></a>
      <a href="https://www.instagram.com/ieee_ejust/" target="_blank"><i class="fa fa-instagram"></i></a>
    </div>
  </div>
</footer>



<script>
       /* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
    function myFunction() {
        var x = document.getElementById("myTopnav");
        if (x.className == "topnav") {
            x.className += "responsive";
        } else {
            x.className = "topnav";
        }
    }

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000);
//   slideIndex++;
}
showSlides(slideIndex);


var slideIndex2 = 1;
showSlides2(slideIndex2);

// Next/previous controls
function plusSlides2(n) {
  showSlides2(slideIndex2 += n);
}

// Thumbnail image controls
function currentSlide2(n) {
  showSlides2(slideIndex2 = n);
}

function showSlides2(n) {
  var i;
  var slides2 = document.getElementsByClassName("mySlides2");
  var dots2 = document.getElementsByClassName("dot2");
  if (n > slides2.length) {slideIndex2 = 1}
  if (n < 1) {slideIndex2 = slides2.length}
  for (i = 0; i < slides2.length; i++) {
      slides2[i].style.display = "none";
  }
  for (i = 0; i < dots2.length; i++) {
      dots2[i].className = dots2[i].className.replace(" active", "");
  }
  slides2[slideIndex2-1].style.display = "block";
  dots2[slideIndex2-1].className += " active";
  setTimeout(showSlides2, 2000);
//   slideIndex++;
}
showSlides2(slideIndex2);
</script>



