frappe.pages['credit-notes'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Credit Notes',
		single_column: true
	});
}