  $(document).ready(function(){

    $("a").click(function(){
        $("#h2title").text( $("img", this).attr("alt"));
    });
  });

