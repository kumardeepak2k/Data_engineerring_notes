
# SQL Notes

## Chapter 3: Basic SQL Queries

### Introduction
This chapter covers the basic SQL statements used to retrieve data from a relational database using the `SELECT` statement.

---

### 1. SELECT Statement
Used to retrieve data from one or more columns in a table.

```sql
SELECT column1, column2 FROM table_name;
```

To select all columns:
```sql
SELECT * FROM table_name;
```

---

### 2. DISTINCT
Used to return only unique values (eliminates duplicates).

```sql
SELECT DISTINCT column_name FROM table_name;
```

---

### 3. WHERE Clause
Used to filter records based on specific conditions.

```sql
SELECT * FROM table_name
WHERE condition;
```

**Operators used with WHERE:**
- `=` (equal)
- `!=` or `<>` (not equal)
- `>` , `<`, `>=`, `<=`
- `BETWEEN`, `LIKE`, `IN`, `IS NULL`, `IS NOT NULL`

Example:
```sql
SELECT name, salary FROM employees
WHERE salary > 50000;
```

---

### 4. ORDER BY
Used to sort the result set in ascending (ASC) or descending (DESC) order.

```sql
SELECT * FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC];
```

Example:
```sql
SELECT name, salary FROM employees
ORDER BY salary DESC;
```

---

### 5. LIMIT (or TOP / FETCH)
Used to limit the number of rows returned.

- MySQL / PostgreSQL:
```sql
SELECT * FROM table_name
LIMIT 5;
```

- SQL Server:
```sql
SELECT TOP 5 * FROM table_name;
```

- Oracle (12c+):
```sql
SELECT * FROM table_name
FETCH FIRST 5 ROWS ONLY;
```

---

### 6. ALIAS (AS)
Used to rename a column or table for better readability in queries.

```sql
SELECT column_name AS alias_name FROM table_name;
```

Example:
```sql
SELECT salary AS monthly_salary FROM employees;
```

---

### 7. Basic Arithmetic in SQL
You can perform arithmetic operations in SQL queries.

```sql
SELECT name, salary * 12 AS annual_salary FROM employees;
```

---

### 8. Comments in SQL
Single-line comment:
```sql
-- This is a comment
```

Multi-line comment:
```sql
/* This is 
a multi-line comment */
```

---

### Summary

| Keyword       | Description                                   |
|---------------|-----------------------------------------------|
| `SELECT`      | Retrieve data                                 |
| `DISTINCT`    | Remove duplicate results                      |
| `WHERE`       | Filter rows based on a condition              |
| `ORDER BY`    | Sort results in ascending or descending order |
| `LIMIT`/`TOP` | Restrict the number of returned rows          |
| `AS`          | Rename a column or table                      |

---

This concludes Chapter 3: Basic SQL Queries.

Next Steps:
- Practice using `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, and aliases.
- Combine these clauses to form complex queries.

---
