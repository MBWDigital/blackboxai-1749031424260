frappe.ui.form.on('Project', {
    refresh: function(frm) {
        // Add button only on form view and if not already added
        if (!frm.doc.__islocal && !frm.custom_button_added) {
            frm.add_custom_button(__('Show Gantt'), function() {
                showGanttDialog(frm.doc);
            });
            frm.custom_button_added = true;
        }
    }
});

function showGanttDialog(project) {
    // Create a modern dialog with a custom header image and title
    let d = new frappe.ui.Dialog({
        title: `Gantt Chart for ${project.name}`,
        fields: [
            { 
                fieldname: 'gantt_area', 
                fieldtype: 'HTML', 
                options: `
                    <div id="gantt-container" class="gantt-chart-container">
                        <div class="loading-state">Loading Gantt Chart...</div>
                    </div>
                    <div class="gantt-controls">
                        <button id="refresh-gantt" class="btn btn-secondary btn-sm">
                            <i class="fa fa-refresh"></i> Refresh Chart
                        </button>
                    </div>
                `
            }
        ],
        primary_action_label: __('Close'),
        primary_action: function() {
            d.hide();
        }
    });

    d.show();

    // Fetch Gantt Data via the server method
    function fetchGanttData() {
        frappe.call({
            method: "project_gantt.project_gantt.api.get_gantt_data",
            args: { project_name: project.name },
            callback: function(r) {
                if (r.message && r.message.length > 0) {
                    renderGanttChart(r.message);
                } else {
                    showEmptyState();
                }
            },
            error: function(err) {
                showErrorState();
                console.error(err);
            }
        });
    }

    function renderGanttChart(tasks) {
        const container = document.getElementById('gantt-container');
        container.innerHTML = '';

        // Initialize Frappe Gantt
        const gantt = new frappe.views.GanttView({
            parent: '#gantt-container',
            tasks: tasks,
            width: '100%',
            height: '400px',
            view_mode: 'Day',
            date_format: 'YYYY-MM-DD',
            on_click: function(task) {
                frappe.set_route('Form', 'Task', task.id);
            },
            on_date_change: function(task, start, end) {
                updateTaskDates(task, start, end);
            },
            custom_popup_html: function(task) {
                return `
                    <div class="gantt-task-info">
                        <h4>${frappe.utils.escape_html(task.name)}</h4>
                        <p>Start: ${frappe.datetime.str_to_user(task.start)}</p>
                        <p>End: ${frappe.datetime.str_to_user(task.end)}</p>
                        <p>Progress: ${task.progress}%</p>
                    </div>
                `;
            }
        });
    }

    function showEmptyState() {
        const container = document.getElementById('gantt-container');
        container.innerHTML = `
            <div class="no-tasks-message">
                <p>No tasks found for this project.</p>
            </div>
        `;
    }

    function showErrorState() {
        const container = document.getElementById('gantt-container');
        container.innerHTML = `
            <div class="error-message">
                <p>Error loading Gantt chart data. Please try again.</p>
            </div>
        `;
    }

    function updateTaskDates(task, start, end) {
        frappe.call({
            method: "project_gantt.project_gantt.api.update_task_dates",
            args: {
                task_id: task.id,
                start_date: start,
                end_date: end
            },
            callback: function(r) {
                if (r.message) {
                    frappe.show_alert({
                        message: __('Task dates updated successfully'),
                        indicator: 'green'
                    });
                }
            }
        });
    }

    // Bind refresh button click event
    d.$wrapper.find('#refresh-gantt').click(function() {
        fetchGanttData();
    });

    // Initial data fetch
    fetchGanttData();
}
