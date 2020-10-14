frappe.pages['technician-time-brea'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Technician Time Breakdown',
		single_column: true
	});
}