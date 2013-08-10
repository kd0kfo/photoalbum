$(document).ready(function(){
    var title_node = $("#h2title");
    var default_title = title_node.text();
    $("a").click(function(){
        var attribute = $("img", this).attr("alt");
        if(attribute){
            title_node.text(attribute);
        }
        else
        {
            title_node.text(default_title);
        }
    });
  });
