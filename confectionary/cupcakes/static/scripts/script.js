var URL = "/dishes/";

    $(document).ready(
       function() {
          $("#dishes").hide();
       }
    );

    function getDishes()
    {
       $.getJSON(URL,{},showDishes);
    }

    function getDish()
    {
       $.getJSON(URL + $("#code").val())
           .done(showDish)   // on success - 200
           .fail(function()    // on failure - 404
                 {
                      alert("Sorry! Dish Not Found!");
                 }
           );
    }

    function showDish(dish)
    {
        $("#name").val(dish.name)
        $("#rating").val(dish.rating)
        $("#kkal").val(dish.kkal)
        $("#price").val(dish.price)
    }

    function showDishes(dishes) {
       $("#dishrows").html("")
       $.each(dishes,
              function(idx,dish) {
                 $("#dishrows").append("<tr><td>" + dish.name + "</td><td>" +
                       dish.rating + "</td><td>" + dish.kkal + "</td><td>" +
                       dish.price + "</td></tr>");
              } // anonymous function
        ); // each()

        $("#dishes").show();
   } 

    function addDish()
    {
       $.ajax(
          { "url": URL,
             "data": {
                       "code" : $("#code").val(),
                       "name" : $("#name").val(),
                       "rating" : $("#rating").val(),
                       "kkal" : $("#kkal").val(),
                       "price" : $("#price").val()
                     },
             "type" : "post",
             "success" : add_success,
             "error" : add_error
          }
      ); // ajax()
    }

    function add_success()
    {
      alert("Added dish Successfully");
    }

    function add_error()
    {
      alert("Could not add dish!");
    }

    function deleteDish()
    {
       $.ajax(
          {  "url": URL + $("#code").val(),
             "type" : "delete",
             "success" : delete_success,
             "error" : delete_error
          }
      ); // ajax()
    }

    function delete_success()
    {
      alert("Deleted Dish Successfully");
    }

    function delete_error()
    {
      alert("Could not delete Dish!");
    }


    function updateDish()
    {
       $.ajax(
          {  "url"     : URL + $("#code").val() + "/",
             "data"    : { "code"     : $("#code").val(),
                           "name"    : $("#name").val(),
                           "rating" : $("#rating").val(),
                           "kkal"      : $("#kkal").val(),
                           "price"      : $("#price").val()
                          },
             "type"    : "put",
             "success" : update_success,
             "error"   : update_error
          }
      ); // ajax()
    }

    function update_success()
    {
      alert("Updated Dish Successfully");
    }

    function update_error()
    {
      alert("Could not update Dish!");
    }

var URL2 = "/calls/";

    $(document).ready(
       function() {
          $("#calls").hide();
       }
    );

    function getCalls()
    {
       $.getJSON(URL2,{},showCalls);
    }

    function getCall()
    {
       $.getJSON(URL2 + $("#id_call").val())
           .done(showCall)   // on success - 200
           .fail(function()    // on failure - 404
                 {
                      alert("Sorry! Call Not Found!");
                 }
           );
    }

    function showCall(call)
    {
        $("#name").val(call.name)
        $("#phone").val(call.phone)
    }

    function showCalls(calls) {
       $("#callrows").html("")
       $.each(calls,
              function(idx,call) {
                 $("#callrows").append("<tr><td>" + call.id + "</td><td>" +
                       call.name + "</td><td>" + call.phone + "</td></tr>");
              } // anonymous function
        ); // each()

        $("#calls").show();
   } 

    function addCall()
    {
       $.ajax(
          { "url": URL2,
             "data": {
                       "code_call" : $("#id_call").val(),
                       "name" : $("#name_call").val(),
                       "phone" : $("#phone_call").val()
                     },
             "type" : "post",
             "success" : add_success_call,
             "error" : add_error_call
          }
      ); // ajax()
    }

    function add_success_call()
    {
      alert("Call is confirmed");
    }

    function add_error_call()
    {
      alert("Could not confirm call!");
    }
    function deleteCall()
    {
       $.ajax(
          {  "url": URL2 + $("#id_call").val(),
             "type" : "delete",
             "success" : delete_success_call,
             "error" : delete_error_call
          }
      ); // ajax()
    }

    function delete_success_call()
    {
      alert("Deleted Call Successfully");
    }

    function delete_error_call()
    {
      alert("Could not delete Call!");
    }


    function updateCall()
    {
       $.ajax(
          {  "url"     : URL2 + $("#id_call").val() + "/",
             "data"    : { "id"     : $("#id_call").val(),
                           "name"    : $("#name_call").val(),
                           "phone" : $("#phone_call").val()
                          },
             "type"    : "put",
             "success" : update_success_call,
             "error"   : update_error_call
          }
      ); // ajax()
    }

    function update_success_call()
    {
      alert("Updated Call Successfully");
    }

    function update_error_call()
    {
      alert("Could not update Call!");
    }
