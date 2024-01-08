$(document).ready(function() {
    $('#worked-before').change(function() {
        if ($(this).is(':checked')) {
            $('#work-where').show();
        } else {
            $('#work-where').hide();
        }
    });
});

