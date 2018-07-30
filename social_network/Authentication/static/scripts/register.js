$(document).ready(function(){
    $('.btn').hover(function(){
        $(this).removeClass('darken-4').addClass('darken-1');
    }).mouseleave(function(){
        $(this).addClass('darken-4').removeClass('darken-1');
    });
});