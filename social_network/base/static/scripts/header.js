$(document).ready(function(){
    // activate Materialize sidenav
    $('.sidenav').sidenav();
    // customized nav button reactions when on hover state
    $('.my-nav-button').hover(function(){
        $(this).removeClass('transparent');
    }).mouseleave(function(){
        $(this).addClass('transparent');
    });
});