// redirect users to categories (helper function) -- large screen based funcionality
function redirect(category,variable) {
    variable.addEventListener('click',()=>{
        window.location = '/' + category + '/topics';
    });
}
var programming_category = document.getElementById('programming_ctg');
var webdev_category = document.getElementById('webdev_ctg');
var videogames_category = document.getElementById('videogames_ctg');
var yourcategory_category = document.getElementById('yourcategory_ctg');

redirect('programming',programming_category);
redirect('web-development',webdev_category);
redirect('video-games',videogames_category);
redirect('yourcategory',yourcategory_category);