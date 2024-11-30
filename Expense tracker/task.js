// task.controller.js
const tasks = require("./task.model");

// Create a new task
exports.createTask = (req, res) => {
  const { name } = req.body;
  if (!name) {
    return res.status(400).json({ message: "Task name is required" });
  }

  const newTask = {
    id: Date.now(), // Unique ID
    name,
    completed: false,
  };

  tasks.push(newTask);
  res.status(201).json(newTask);
};

// Get all tasks
exports.getAllTasks = (req, res) => {
  res.status(200).json(tasks);
};

// Get a single task by ID
exports.getTaskById = (req, res) => {
  const { id } = req.params;
  const task = tasks.find((t) => t.id === parseInt(id));

  if (!task) {
    return res.status(404).json({ message: "Task not found" });
  }

  res.status(200).json(task);
};

// Update a task by ID
exports.updateTask = (req, res) => {
  const { id } = req.params;
  const { name, completed } = req.body;

  const task = tasks.find((t) => t.id === parseInt(id));
  if (!task) {
    return res.status(404).json({ message: "Task not found" });
  }

  if (name !== undefined) task.name = name;
  if (completed !== undefined) task.completed = completed;

  res.status(200).json(task);
};

// Delete a task by ID
exports.deleteTask = (req, res) => {
  const { id } = req.params;
  const index = tasks.findIndex((t) => t.id === parseInt(id));

  if (index === -1) {
    return res.status(404).json({ message: "Task not found" });
  }

  tasks.splice(index, 1);
  res.status(200).json({ message: "Task deleted successfully" });
};
