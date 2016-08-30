(function () {
  'use strict';

  var controlGroupInfoToggle = $('.control-group-info-toggle');

  $('#human_research').on('click', function () {

    if($('#human_research').is(':checked')){
      $('#human_research').val(1);
      $('#human_research').attr('checked', 'checked');
    }
    else{
      $('#human_research').val(0);
      $('#human_research').removeAttr('checked');
    }

  });

  $('#assign-creator').on('click', function () {

    var current_user_email = $('#current_user_email').val();
    var current_user_name = $('#current_user_name').val();
    $('#field-author').val(current_user_name);
    $('#field-author-email').val(current_user_email);

  });

  $('#assign-publisher').on('click', function () {

    var current_user_email = $('#current_user_email').val();
    var current_user_name = $('#current_user_name').val();
    $('#field-maintainer').val(current_user_name);
    $('#field-maintainer-email').val(current_user_email);

  });

  $(document).ready(function () {
    $('#tc_start').datepicker({
      dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true,
        showButtonPanel: true,
        onClose: function(dateText, inst) {
            $(this).datepicker('setDate', new Date(inst.selectedYear, inst.selectedMonth, 1));
        }
    });
    $('#tc_end').datepicker({
      dateFormat: 'yy-mm-dd',
        changeMonth: true,
        changeYear: true,
        showButtonPanel: true,
        onClose: function(dateText, inst) {
            $(this).datepicker('setDate', new Date(inst.selectedYear, inst.selectedMonth, 1));
        }
    });

    // Required for the info button for the fields
    controlGroupInfoToggle.click(function (e) {
      e.preventDefault();
      if (!$(this).parent().hasClass('toggled')) {
        $('.control-group-info').removeClass('toggled');
        $(this).parent().addClass('toggled');
      } else {
        $(this).parent().removeClass('toggled');
      }
    });

    // Hide control group info when it loses focus
    controlGroupInfoToggle.blur(function () {
      $(this).parent().removeClass('toggled');
    });
  });

})($);
