$( "#theform" ).submit(function( event ) {

  event.preventDefault();

  var $form = $( this ), url = $form.attr( "action" );

  var posting = $.post( url, $form.serialize());

  posting.done(function( data ) {
    var content = data;
    console.log(data);
    $("#number").val('');
    $( "#result" ).append('<div class="taken-number">'+data.number+'</div>');
    $( "#submit-btn").html('Prenotane un altro!')
  });
});