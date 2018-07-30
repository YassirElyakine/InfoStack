$(document).ready(function(){
    // hover effects on buttons
    $('.btn').hover(function(){
        $(this).addClass('darken-1').removeClass('darken-4');
    }).mouseleave(function(){
        $(this).addClass('darken-4').removeClass('darken-1');
    });
    // disable buttons on click
    $('#programming').click(function(){
        $(this).addClass('disabled');
        $('#selected_category').val('programming');
        $('#webdev').removeClass('disabled');
        $('#videogames').removeClass('disabled');
        $('#else').removeClass('disabled');
    });
    $('#webdev').click(function(){
        $(this).addClass('disabled');
        $('#selected_category').val('web-development');
        $('#programming').removeClass('disabled');
        $('#videogames').removeClass('disabled');
        $('#else').removeClass('disabled');
    });
    $('#videogames').click(function(){
        $(this).addClass('disabled');
        $('#selected_category').val('video-games');
        $('#webdev').removeClass('disabled');
        $('#programming').removeClass('disabled');
        $('#else').removeClass('disabled');
    });
    $('#else').click(function(){
        $(this).addClass('disabled');
        $('#selected_category').val('yourcategory');
        $('#webdev').removeClass('disabled');
        $('#videogames').removeClass('disabled');
        $('#programming').removeClass('disabled');
    });
    $('.post-button').click(function(){
        $('#selected_category').removeAttr('readonly');
        setInterval(()=>{
            $('#selected_category').attr('readonly','readonly');
        }, 50);
    });
});