$(document).ready(function() {
    $('.form-container').hide().fadeIn(1000);

    $('button').on('mouseenter', function() {
        $(this).addClass('shadow-lg').css('cursor', 'pointer');
    });

    $('button').on('mouseleave', function() {
        $(this).removeClass('shadow-lg');
    });

    // Example animation for form submission
    $('form').on('submit', function(e) {
        e.preventDefault();
        $(this).fadeOut(500, function() {
            alert('Form submitted successfully!');
            $(this).fadeIn(500);
        });
    });

    // Navigation link hover effect
    $('.nav-link').hover(
        function() {
            $(this).css('color', '#fc5c7d');
        },
        function() {
            $(this).css('color', 'white');
        }
    );
});
