$(document).ready(function(){
    // darken the color of each category when hovering over it
    $('.large-based').hover(function(){
        $(this).removeClass('lighten-3').addClass('darken-3');
    }).mouseleave(function(){
        $(this).addClass('lighten-3').removeClass('darken-3');
    });
    // mobile based category access button, adding hover effects
    $('.btn').hover(function(){
        $(this).removeClass('darken-4').addClass('darken-1');
    }).mouseleave(function(){
        $(this).addClass('darken-4').removeClass('darken-1');
    });
});