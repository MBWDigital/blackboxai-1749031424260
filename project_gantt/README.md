# Project Gantt

A Frappe/ERPNext app that adds an interactive Gantt chart view to Project details.

## Features

- Interactive Gantt chart visualization for project tasks
- Real-time task date updates
- Progress indication
- Task dependencies support
- Status-based task coloring
- Responsive design
- Error handling and user feedback

## Installation

1. Get the app from GitHub:
```bash
bench get-app project_gantt https://github.com/yourusername/project_gantt
```

2. Install the app:
```bash
bench install-app project_gantt
```

3. Run migrations:
```bash
bench migrate
```

4. Clear browser cache and reload the page

## Usage

1. Open any Project in ERPNext
2. Look for the "Show Gantt" button in the Project form
3. Click the button to open the Gantt chart dialog
4. View and interact with the Gantt chart:
   - Drag tasks to update dates
   - Click tasks to view details
   - Use the refresh button to update the view
   - View task dependencies and progress

## Dependencies

- Frappe Framework
- ERPNext
- Project Module enabled

## License

MIT
