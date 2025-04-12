
# SQL Notes

## Chapter 2: SQL Data Types

### Introduction to SQL Data Types
SQL data types are used to define the type of data that a column can hold in a table. Understanding data types is essential for defining proper table structures and ensuring data integrity.

### Major SQL Data Types
SQL provides a wide range of data types. Here are the most commonly used ones:

#### 1. Numeric Data Types
- **INT** (Integer): Used for whole numbers. Example: `1`, `100`, `-42`.
- **DECIMAL** or **NUMERIC**: Used for fixed-point numbers with exact precision. Example: `123.45`.
- **FLOAT**: Used for floating-point numbers (approximate precision). Example: `3.14159`.
- **BIGINT**: Used for large integers (larger than INT). Example: `123456789`.

#### 2. String Data Types
- **CHAR**: Fixed-length string. The length is defined at the time of table creation. Example: `CHAR(10)` stores strings of exactly 10 characters.
- **VARCHAR**: Variable-length string. The length is defined at the time of table creation but can store strings of any length up to the specified maximum. Example: `VARCHAR(255)` can store up to 255 characters.
- **TEXT**: Stores long text strings. No length limit (depends on the database system).

#### 3. Date and Time Data Types
- **DATE**: Stores date values in the format `YYYY-MM-DD`. Example: `2025-04-10`.
- **TIME**: Stores time values in the format `HH:MM:SS`. Example: `14:30:00`.
- **DATETIME** or **TIMESTAMP**: Stores both date and time values. Example: `2025-04-10 14:30:00`.

#### 4. Boolean Data Type
- **BOOLEAN**: Used for storing true/false values. Typically stored as `TRUE` or `FALSE`, or `1` for true and `0` for false, depending on the database system.

#### 5. Binary Data Types
- **BLOB**: Stands for Binary Large Object, used to store binary data such as images, files, etc.
- **VARBINARY**: Similar to BLOB but with a variable length.

### Choosing the Right Data Type
When designing a table, choosing the right data type for each column is crucial:
- **Efficiency**: Different data types require different amounts of storage space. For example, using `INT` when you need a small range of numbers is more efficient than using `BIGINT`.
- **Precision**: Choose `DECIMAL` or `NUMERIC` when dealing with exact precision, such as storing financial data.
- **Storage**: Use `VARCHAR` instead of `CHAR` unless you are sure all values will be the same length.

---

### Example of Creating a Table with Data Types

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10, 2),
    hire_date DATE,
    active BOOLEAN
);
```

In this example:
- `id` is an integer.
- `name` is a variable-length string.
- `salary` is a decimal number with 2 digits after the decimal point.
- `hire_date` is a date.
- `active` is a boolean value indicating whether the employee is active.

---

### Summary of Key Concepts
- **Data types** define the kind of data that a column can hold.
- Choose the appropriate data type based on the nature of the data.
- **Common data types** include numeric, string, date/time, boolean, and binary data types.
- **Best practices**: Use `INT` for whole numbers, `VARCHAR` for variable-length strings, and `DECIMAL` for precise values.

---

This concludes Chapter 2: SQL Data Types.

Next Steps:
- **Practice** creating tables with different data types.
- **Explore** how different data types behave with SQL queries.
- **Learn** the database-specific variations in data types (e.g., how `DATE` and `DATETIME` differ between databases).

---
