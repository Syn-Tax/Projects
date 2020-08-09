console.log("testing");

const $body = $("body");
const $header = $(".page-header");
const scrollClass = "scroll";

console.log(window.location.href);

$(window).on("scroll", () => {
  if (this.matchMedia("(min-width: 992px)").matches && window.location.href.includes("index")) {
    const scrollY = $(this).scrollTop();
    scrollY > 0
      ? $body.addClass(scrollClass)
      : $body.removeClass(scrollClass);
  } else if (window.location.href.includes("index")) {
    $body.removeClass(scrollClass);
  } else if (!window.location.href.includes("index")) {
    $body.addClass(scrollClass);
  }
});

$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top - 71
      }, 800, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        //window.location.hash = hash;
      });
    } // End if
  });
});
