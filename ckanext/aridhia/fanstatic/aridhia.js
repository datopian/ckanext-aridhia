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
	
 })($);