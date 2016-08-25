(function () {
  'use strict';
  
	$('#assign-creator').on('click', function(){

		var current_user_email = $('#current_user_email').val();
		var current_user_name = $('#current_user_name').val();
		$('#field-author').val(current_user_name);
		$('#field-author-email').val(current_user_email);

	});

	$('#assign-publisher').on('click', function(){

		var current_user_email = $('#current_user_email').val();
		var current_user_name = $('#current_user_name').val();
		$('#field-maintainer').val(current_user_name);
		$('#field-maintainer-email').val(current_user_email);

	});

      $(document).ready(function () {
        $('#tc_start').datepicker({
          dateFormat: 'yy-mm-dd'
        });
        $('#tc_end').datepicker({
          dateFormat: 'yy-mm-dd'
        });

        // Required for the info button for the fields
        $('.control-group-info-toggle').click(function (e) {
          e.preventDefault();
          $(this).toggleClass('toggled');
          $(this).parent().children('.control-group-info-content').toggleClass('control-group-info-content-hidden');
        });
      });
	
 })($);