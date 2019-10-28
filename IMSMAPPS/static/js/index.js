$("#connexion").on('click', function () {
    // alert("dddd");

    $("#modalLRForm").modal();
    $("#modal-title").html("Welcome to user connexion panel");
    $.get("login/", function (data) {
        alert(data);
        $("#diagshow").html(data);

    });


});

   $('.btnmenu').on('click', function () {
       var opt=$(this).attr("id");
    //    alert(opt)
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
 //alert(opt+"   ddd  "+csrftoken)
        $.ajax({
            url: ''+opt+'/',
            type: "POST",
           headers: {'X-CSRFToken': csrftoken},
            data: {'obj':opt},
            dataType: "text",
            success: function (data) {
                $(".refresh").prop("id",opt);
                // do something
  $("#mainshow").html(data);
   //             alert(data);

            }
        });
    });

    $('.refresh').on('click', function () {
       var opt=$(this).attr("id");
        alert(opt)
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
 //alert(opt+"   ddd  "+csrftoken)
        $.ajax({
            url: opt+'/',
            type: "POST",
           headers: {'X-CSRFToken': csrftoken},
            data: {'obj':opt},
            dataType: "text",
            success: function (data) {
                // do something
  $("#mainshow").html(data);
   //             alert(data);

            }
        });
    });
$(".btnmenuk").on('click', function () {
var opt=$(this).attr('id');
   // alert(opt);
   var target="";
  /* switch (opt) {
       case "newproject":
           target="projects";
           break;
       case "newapplication":
           target="application";
           break;
       case :"newcomponent":
           target="components";
           break;
       case "newdevice":
           target="devices";
           break;
       case "newmicroservice":
           target="microservice";
           break;
       case "newdata":
           target="data";
           break;
       default:
           alert("command not reconized");
   }*/
   //  $("#modalLRForm").modal();
   // $("#modal-title").html("show  project ");
     $.post("/"+opt+"/", {'obj':opt},function (data) {
      //  alert(data);
        $("#mainshow").html(data);

    });

});


           /////////////////////////////////////////////////////////////
     $('#build').on('click', function () {
      //   var x=  confirm('get started to develop this application');
     //    if (!x==false){}else{
       var opt=$(this).attr("id");
     //   alert(opt)
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();


  $.ajax({
            url: "applications/building/",
            type: "POST",
           headers: {'X-CSRFToken': csrftoken},
            data: {'id':opt},

            success: function (data) {

   $("#mainshow").html(data);

            }
        });

//    }
});
     /////////////////////////////////////////////
   $(document).on('change','#languageMenu', function () {
       var x=$(this).val();
     $("#lang").val(x)
       // alert(x+   + $("#lang").val())
     //  alert($("#msgis").html())
  var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();


  $.ajax({
            url: "applications/building/",
            type: "POST",
           headers: {'X-CSRFToken': csrftoken},
            data: {'id':''},

            success: function (data) {
//alert("dddddd")
   $("#mainshow").html(data);

            }
        });});