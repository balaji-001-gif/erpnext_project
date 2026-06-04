app_name = "projects"
app_title = "Projects"
app_publisher = "ERPNext Community"
app_description = "Standalone Projects app for ERPNext v15"
app_icon = "fa fa-puzzle-piece"
app_color = "grey"
app_email = "info@example.com"
app_license = "GNU General Public License (v3)"
app_url = "https://github.com/balaji-001-gif/projects"

required_apps = ["erpnext"]

after_install = "projects.install.after_install"

# Apps
# ------------------------------

# DocTypes
# ------------------------------

# Website
# ------------------------------
website_route_rules = [
	{"from_route": "/projects/<path:app>", "to_route": "projects"},
]
