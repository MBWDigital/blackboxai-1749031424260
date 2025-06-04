app_name = "project_gantt"
app_title = "Project Gantt"
app_publisher = "Your Name"
app_description = "Show Gantt Chart in Project Detail"
app_icon = "octicon octicon-project"
app_color = "grey"
app_email = "your@email.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/project_gantt/css/project_detail.css"
app_include_js = "/assets/project_gantt/js/project_detail.js"

# include js, css files in header of web template
# web_include_css = "/assets/project_gantt/css/project_gantt.css"
# web_include_js = "/assets/project_gantt/js/project_gantt.js"

# Doctype JS
doctype_js = {
    "Project": "public/js/project.js"
}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "project_gantt.install.before_install"
# after_install = "project_gantt.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "project_gantt.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }
