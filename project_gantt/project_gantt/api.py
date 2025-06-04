import frappe
from frappe import _
from datetime import datetime

@frappe.whitelist()
def get_gantt_data(project_name):
    """
    Fetch tasks associated with the given project and format them for Gantt chart.
    """
    try:
        # Fetch tasks for the project
        tasks = frappe.get_all(
            "Task",
            filters={
                "project": project_name,
                "docstatus": ["<", 2]  # Include both draft (0) and submitted (1) tasks
            },
            fields=[
                "name", "subject", "exp_start_date", "exp_end_date", 
                "progress", "depends_on_tasks", "status"
            ],
            order_by="exp_start_date asc"
        )

        gantt_tasks = []
        for task in tasks:
            # Skip tasks without start or end date
            if not task.exp_start_date or not task.exp_end_date:
                continue

            # Format task for Gantt chart
            gantt_task = {
                "id": task.name,
                "name": task.subject,
                "start": task.exp_start_date.strftime("%Y-%m-%d"),
                "end": task.exp_end_date.strftime("%Y-%m-%d"),
                "progress": task.progress or 0,
                "dependencies": task.depends_on_tasks or "",
                "custom_class": get_task_class(task.status)
            }
            gantt_tasks.append(gantt_task)

        return gantt_tasks

    except Exception as e:
        frappe.log_error(
            title="Error in Gantt Data Fetch",
            message=str(e)
        )
        frappe.throw(_("Error fetching Gantt chart data. Please check error logs."))

@frappe.whitelist()
def update_task_dates(task_id, start_date, end_date):
    """
    Update task start and end dates when modified in Gantt chart.
    """
    try:
        if not frappe.has_permission("Task", "write"):
            frappe.throw(_("No permission to update tasks"))

        # Convert string dates to datetime objects
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        # Update the task
        task = frappe.get_doc("Task", task_id)
        task.exp_start_date = start
        task.exp_end_date = end
        task.save()

        return True

    except Exception as e:
        frappe.log_error(
            title="Error in Task Date Update",
            message=str(e)
        )
        frappe.throw(_("Error updating task dates. Please check error logs."))

def get_task_class(status):
    """
    Return CSS class based on task status.
    """
    status_classes = {
        "Open": "task-open",
        "Working": "task-working",
        "Pending Review": "task-pending",
        "Overdue": "task-overdue",
        "Completed": "task-completed",
        "Cancelled": "task-cancelled"
    }
    return status_classes.get(status, "task-default")
