// task.routes.js
const express = require("express");
const router = express.Router();
const taskController = require("./task.controller");

// Define routes
router.post("/", taskController.createTask);        // Create a task
router.get("/", taskController.getAllTasks);       // Get all tasks
router.get("/:id", taskController.getTaskById);    // Get a task by ID
router.put("/:id", taskController.updateTask);     // Update a task by ID
router.delete("/:id", taskController.deleteTask);  // Delete a task by ID

module.exports = router;


// app.js
const express = require("express");
const taskRoutes = require("./task.routes");

const app = express();
const PORT = 5000;

// Middleware
app.use(express.json()); // To parse JSON request bodies

// Task routes
app.use("/tasks", taskRoutes);

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

// department.controller.js
const pool = require("./db");

// Create a department
exports.createDepartment = async (req, res) => {
  const { name } = req.body;

  try {
    const result = await pool.query(
      "INSERT INTO Departments (name) VALUES ($1) RETURNING *",
      [name]
    );
    res.status(201).json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Get all departments
exports.getAllDepartments = async (req, res) => {
  try {
    const result = await pool.query("SELECT * FROM Departments");
    res.status(200).json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Get a department by ID with associated employees
exports.getDepartmentById = async (req, res) => {
  const { id } = req.params;

  try {
    const department = await pool.query(
      "SELECT * FROM Departments WHERE id = $1",
      [id]
    );

    if (department.rows.length === 0) {
      return res.status(404).json({ message: "Department not found" });
    }

    const employees = await pool.query(
      "SELECT * FROM Employees WHERE department_id = $1",
      [id]
    );

    res.status(200).json({
      department: department.rows[0],
      employees: employees.rows,
    });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Update a department
exports.updateDepartment = async (req, res) => {
  const { id } = req.params;
  const { name } = req.body;

  try {
    const result = await pool.query(
      "UPDATE Departments SET name = $1 WHERE id = $2 RETURNING *",
      [name, id]
    );

    if (result.rows.length === 0) {
      return res.status(404).json({ message: "Department not found" });
    }

    res.status(200).json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};

// Delete a department
exports.deleteDepartment = async (req, res) => {
  const { id } = req.params;

  try {
    await pool.query("DELETE FROM Departments WHERE id = $1", [id]);
    res.status(200).json({ message: "Department deleted successfully" });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
};
