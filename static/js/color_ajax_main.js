/**
 * Created by Viv on 8/15/15.
 */
//THIS MUST BE IMPORTED AS THE VERY LAST THING BEFORE THE CLOSE </body>
//tag.

/**
  The number of milliseconds to ignore key-presses in the search box,
  after a key *that was not ignored* was pressed. Used by
  `$(document).ready()`.

  Equal to <code>100</code>.
 */
var MILLS_TO_IGNORE_SEARCH = 100;
/**
  The number of milliseconds to ignore clicks on the *same* like
  button, after a button *that was not ignored* was clicked. Used by
  `$(document).ready()`.

  Equal to <code>500</code>.
 */
var MILLS_TO_IGNORE_LIKES = 500;
/**
   The Ajax "main" function. Attaches the listeners to the elements on
   page load, each of which only take effect every
   <link to MILLS_TO_IGNORE_SEARCH> or <link to MILLS_TO_IGNORE_LIKES>
   seconds.

   This protection is only against a single user pressing buttons as fast
   as they can. This is in no way a protection against a real DDOS attack,
   of which almost 100% bypass the client (browser) (they instead
   directly attack the server). Hence client-side protection is pointless.

   - http://stackoverflow.com/questions/28309850/how-much-prevention-of-rapid-fire-form-submissions-should-be-on-the-client-side

   The protection is implemented via Underscore.js' debounce function:
  - http://underscorejs.org/#debounce

   Using this only requires importing underscore-min.js. underscore-min.map
   is not needed.
 */
$(document).ready(function()  {
  /*
    Warning: Placing the true parameter outside of the debounce call:

    $('#color_search_text').keyup(_.debounce(processSearch,
        MILLS_TO_IGNORE_SEARCH), true);

    results in "TypeError: e.handler.apply is not a function"
   */
  $('#color_search_text').keyup(_.debounce(processSearch,
      MILLS_TO_IGNORE_SEARCH, true));
  /*
    There are many buttons having the class

      td__toggle_color_like_button

    This attaches a listener to *every one*. Calling this again
    would attach a *second* listener to every button, meaning each
    click would be processed twice.
   */
  $('.td__toggle_client_like_button').click(_.debounce(processLike,
      MILLS_TO_IGNORE_LIKES, true));
});