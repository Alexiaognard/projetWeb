  $(document).ready(function(){
    $('select').formSelect();
  });

$('.dropdown-trigger').dropdown();

$(document).ready(function() {
    M.updateTextFields();
  });

$(document).ready(function(){
$('.sidenav').sidenav();
  });

  $(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "Apple": null,
        "Microsoft": null,
        "Google": 'https://placehold.it/250x250'
      },
    });
  });

$( document ).ready(function(){
    $('.dropdown-trigger').dropdown();
    });