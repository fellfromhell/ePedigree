//THIS FILE MUST BE IMPORTED BEFORE THE "main" FILE.
 
/**
   Executes a like click. Triggered by clicks on the various yes/no links.
 */
var processLike = function()  {
 
   //In this scope, "this" is the button just clicked on.
   //The "this" in processServerResponse is *not* the button just clicked
   //on.
   var $button_just_clicked_on = $(this);
 
   //The value of the "data-color_id" attribute.
   var color_id = $button_just_clicked_on.data('color_id');
 
   var processServerResponse = function(sersverResponse_data, textStatus_ignored,
                            jqXHR_ignored)  {
      //alert("sf sersverResponse_data='" + sersverResponse_data + "', textStatus_ignored='" + textStatus_ignored + "', jqXHR_ignored='" + jqXHR_ignored + "', color_id='" + color_id + "'");
      $('#toggle_client_like_cell_' + color_id).html(sersverResponse_data);
   }
 
   var config = {
      url: LIKE_URL_PRE_ID + color_id + '/',
      dataType: 'html',
      success: processServerResponse
      //Should also have a "fail" call as well.
   };
   $.ajax(config);
};
