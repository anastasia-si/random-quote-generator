function getRandomDarkColor() {
   /**
   * Generate dark hex color
   * @return {String} HEX color string
   */

    MAX_DEGREE = 8 // don't use all 16 digits in generating hex color to exclude too light colors
    var chars = '0123456789ABCDEF'.substring(0, MAX_DEGREE+1).split('');
    var color = '#';
    n = chars.length;
    for (var i = 0; i < 6; i++) {
        color += chars[Math.floor(Math.random() * n)];  
    }
    return color;    
}

document.body.style.backgroundColor = getRandomDarkColor();

$(document).ready(function() {
    $('select').select2({
        placeholder: 'Select an option'
    });
    
});