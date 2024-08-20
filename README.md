
# Samu Data Reader

The **Samu Data Reader** is a Python class designed to read, manipulate, and analyze custom `.smdt` files, which are delimited text files similar to CSV but with a custom format. This class provides functionalities similar to the `pandas` library for processing data, such as retrieving column names, calculating statistical measures, and displaying data.

## Features

- **Column and Row Information:** Easily retrieve the names of columns and the number of rows in the data.
- **Data Display:** View the first (`head`) or last (`tail`) rows of the data in a well-formatted table.
- **Data Analysis:** Compute the mean of a specified column.
- **Custom Data Format Handling:** Reads and processes `.smdt` files.

## Installation

To use the `ReadSamuData` class, ensure you have the necessary dependencies installed:

```bash
pip install numpy tabulate
```

## Usage

### Basic Usage

1. **Initialization:**

   To start using the `ReadSamuData` class, you need to create an instance of the class by passing the file path of your `.smdt` file:

   ```python
   from read_samu_data import ReadSamuData

   data = ReadSamuData('path/to/your/file.smdt')
   ```

2. **Display Data:**

   - **View Column Names:**

     ```python
     print(data.columns)
     ```

   - **View the First Few Rows:**

     ```python
     print(data.show(head=5))
     ```

   - **View the Last Few Rows:**

     ```python
     print(data.show(tail=5))
     ```

3. **Get Information About the Data:**

   ```python
   print(data.info())
   ```

4. **Calculate the Mean of a Column:**

   Specify the column name to calculate the mean:

   ```python
   average_salary = data.mean('Salary')
   print(f"The average salary is: {average_salary}")
   ```

### Custom Methods and Properties

- **`data.columns`**: Returns the list of column names.
- **`data.sizerows(withoutcolnames=True)`**: Returns the number of rows. If `withoutcolnames` is `True`, it excludes the header row from the count.
- **`data.indexrow`**: Returns the data rows (excluding the header).
- **`data.indexcol`**: Returns the columns of the data as tuples.
- **`data.mean(column)`**: Calculates the mean of the specified column.

### Example

```python
data = ReadSamuData('employees.smdt')

# Print column names
print("Columns:", data.columns)

# Show the first 5 rows
print(data.show(head=5))

# Calculate and print the mean of the 'Salary' column
print("Average Salary:", data.mean('Salary'))
```

## File Format

The `.smdt` file format is a delimited text file where data is separated by semicolons (`;`). The first row contains the column headers, and subsequent rows contain the data. Example:

```
Name;Age;Salary
John;34;5600
Marry;56;9392
```

## Error Handling

- The class raises a `ValueError` if the provided file does not have the `.smdt` extension.

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request with your changes.
# samudatareader
# samudatareader
# samudatareader
