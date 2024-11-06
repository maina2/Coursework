use Workers

	CREATE TABLE Employees (
		EmployeeID INT PRIMARY KEY,
		FirstName NVARCHAR(50),
		LastName NVARCHAR(50),
		Position NVARCHAR(50),
		Salary DECIMAL(10, 2),
		DepartmentID INT
	);
	INSERT INTO Employees (EmployeeID, FirstName, LastName, Position, Salary, DepartmentID)
	VALUES (1, 'John', 'Doe', 'Manager', 75000.00, 1),
		   (2, 'Jane', 'Smith', 'Analyst', 55000.00, 2),
		   (3, 'Sam', 'Brown', 'Developer', 65000.00, 2),
		   (4, 'Alice', 'Johnson', 'Sales Rep', 50000.00, 4),
		   (5, 'Mike', 'Davis', 'Accountant', 58000.00, 5);
	CREATE TABLE Departments (
		DepartmentID INT PRIMARY KEY,
		DepartmentName NVARCHAR(50)
	);
	INSERT INTO Departments (DepartmentID, DepartmentName)
	VALUES (1, 'Human Resources'),
		   (2, 'Engineering'),
		   (3, 'Marketing'),
		   (4, 'Sales'),
		   (5, 'Finance');
	CREATE TABLE Projects (
		ProjectID INT PRIMARY KEY,
		ProjectName NVARCHAR(100),
		Budget DECIMAL(15, 2),
		DepartmentID INT
	);
	INSERT INTO Projects (ProjectID, ProjectName, Budget, DepartmentID)
	VALUES (1, 'Website Redesign', 20000.00, 2),
		   (2, 'Employee Onboarding', 15000.00, 1),
		   (3, 'Product Launch', 30000.00, 3),
		   (4, 'Customer Outreach', 12000.00, 4),
		   (5, 'Financial Audit', 25000.00, 5);

		  select * from Employees
		  select * from Departments
			select * from Projects

		SELECT Employees.FirstName, Employees.LastName, Departments.DepartmentName
	FROM Employees
	INNER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID;
	SELECT Projects.ProjectName, Departments.DepartmentName
FROM Projects
INNER JOIN Departments ON Projects.DepartmentID = Departments.DepartmentID;

