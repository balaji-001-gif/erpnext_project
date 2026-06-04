import frappe


def after_install():
	"""Add Projects module to the system if not already present."""
	from frappe import _

	if not frappe.db.exists("Module Def", "Projects"):
		module_def = frappe.get_doc({
			"doctype": "Module Def",
			"module_name": "Projects",
			"app_name": "projects",
			"custom": 0,
		})
		module_def.insert(ignore_permissions=True)
		frappe.db.commit()
