//  function to run search
function runSearch( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();

    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#input_form').serialize();

    $.ajax({
         /* ajax is incorrect */
        url: './main.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("runSearch failed! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}


//  function to process JSON
function processJSON( data ) {

    /*
    jQuery script to generate results section
    */

    $('#results').show();   // now show the result section that was previously hidden
}


//  document ready function
$(document).ready( function() {
    // search form submit definition
    $('#submit').click( function() {
        runSearch();
        return false;   // prevents 'normal' form submission
    });
});

// Katharina Gees
