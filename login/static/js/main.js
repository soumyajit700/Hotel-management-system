jQuery( document ).ready(function( $ ) {
	var form = $('#booking-form'),
	loading = $('#form-loading')
	content = $('#form-content'),
	message = $('#form-message');



	$('#date-from, #date-to', form).dateTimePicker({
		paging: ['<i class="fa fa-angle-left"></i>', '<i class="fa fa-angle-right"></i>'],
		picker: ['date'],
		format: 'm/d/Y',
		filter: function(date){
			// Select date in the future
			var d = new Date();
			if (date.getTime() < d.getTime()){
				return false;
			}else{
				return true;
			}
		},
		filter_show: function(date){
			var d = new Date();
			return date.getYear() > d.getYear() || (date.getYear() == d.getYear() && date.getMonth() >= d.getMonth());
		}
	}).dateTimePickerRange();
	
	$('select', form).styleSelect({
		class_wrap: 'ul-dropdown-wrap',
	});

	var groups = $('.group', form).filter(function(){
		return !$(this).hasClass('submit');
	}).click(function(){
		$(groups).removeClass('active');
		$(this).addClass('active');
	});
	$('#name').trigger('click').trigger('focus');
});
