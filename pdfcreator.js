$(document).ready(function(){
    $('#btn_print').click(function() {
        $('#content').printThis("Kap.pdf");
    });
});