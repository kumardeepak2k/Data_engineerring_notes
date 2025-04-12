
# SQL Notes

## Chapter 1: Introduction to SQL

### What is SQL?
- **SQL (Structured Query Language)** is a programming language used to manage and manipulate relational databases.
- SQL is used for querying, inserting, updating, and deleting data in databases.
- SQL is widely used in data analytics, data engineering, and software development.

### Key Components of SQL
1. **DDL (Data Definition Language)**: Defines the structure of the database and the tables.
   - **Commands**: `CREATE`, `ALTER`, `DROP`
2. **DML (Data Manipulation Language)**: Manipulates data stored in the database.
   - **Commands**: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
3. **DCL (Data Control Language)**: Controls access to the database.
   - **Commands**: `GRANT`, `REVOKE`
4. **TCL (Transaction Control Language)**: Manages the changes made by DML.
   - **Commands**: `COMMIT`, `ROLLBACK`, `SAVEPOINT`

---

### SQL Basics

#### SQL Syntax
- SQL statements follow a structured syntax that must be followed:
  - **Keywords**: Most SQL keywords are in uppercase (e.g., `SELECT`, `FROM`).
  - **Clauses**: SQL queries consist of clauses like `SELECT`, `FROM`, `WHERE`, etc.
  - **Semicolons**: SQL statements typically end with a semicolon (`;`).

#### Case Sensitivity
- SQL is **not case-sensitive** for most keywords, but some systems (like PostgreSQL) treat string literals as case-sensitive.
- Example: 
  - `SELECT` is the same as `select`.
  - `'John'` and `'john'` are different in some systems, depending on the database's settings.

#### SQL Commands Overview

1. **DDL Commands**
   - **CREATE**: Creates a new table, database, index, or view.
   - **ALTER**: Modifies an existing database object, such as adding or removing columns from a table.
   - **DROP**: Deletes an existing database object, such as a table.

   Example:
   ```sql
   CREATE TABLE employees (
     id INT PRIMARY KEY,
     name VARCHAR(100)
   );
   ```

2. **DML Commands**
   - **SELECT**: Retrieves data from a table.
   - **INSERT**: Adds new data into a table.
   - **UPDATE**: Modifies existing data in a table.
   - **DELETE**: Removes data from a table.

   Example:
   ```sql
   SELECT name, salary FROM employees WHERE id = 1;
   ```

3. **DCL Commands**
   - **GRANT**: Gives privileges to users to access or modify the database.
   - **REVOKE**: Removes privileges from users.

   Example:
   ```sql
   GRANT SELECT, INSERT ON employees TO user1;
   ```

4. **TCL Commands**
   - **COMMIT**: Saves changes made during a transaction.
   - **ROLLBACK**: Reverts the changes made during a transaction.
   - **SAVEPOINT**: Sets a savepoint within a transaction to which you can later roll back.

   Example:
   ```sql
   COMMIT;
   ```

---

### Summary of Key Concepts
- **SQL is essential for interacting with relational databases.** It allows you to define structures, manage data, control access, and handle transactions.
- **SQL Commands are categorized into four groups**: DDL (defining structure), DML (manipulating data), DCL (controlling access), and TCL (managing transactions).
- **SQL syntax and case rules** are important for writing correct queries, but SQL itself is not case-sensitive for keywords.

---

This concludes Chapter 1: Introduction to SQL.

Next Steps:
- **Practice** writing basic SQL queries and familiarize yourself with the commands.
- **Explore** the differences between SQL commands like `CREATE`, `INSERT`, `UPDATE`, and `DELETE`.
- **Learn** how to handle errors and edge cases as you move forward.

---
