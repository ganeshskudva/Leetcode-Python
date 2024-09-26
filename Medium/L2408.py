class SQL:
    
    def __init__(self, names: List[str], columns: List[int]):
        # Initialize the SQL tables
        self.tab = {}  # Dictionary to hold tables by name
        for name in names:
            # For each table name, create an entry with 'nextid' for the next row ID to be inserted
            self.tab[name] = {"nextid": 1}  # 'nextid' keeps track of the next available row ID

    def insertRow(self, name: str, row: List[str]) -> None:
        # Insert a new row into the specified table
        tab = self.tab[name]  # Access the table by name
        rowId = tab["nextid"]  # Get the current row ID for the new row
        tab[rowId] = row  # Insert the row into the table using rowId as the key
        tab["nextid"] += 1  # Increment the next available row ID for future inserts

    def deleteRow(self, name: str, rowId: int) -> None:
        # Delete the row with the given rowId from the specified table
        tab = self.tab[name]  # Access the table by name
        del tab[rowId]  # Delete the row with the given rowId

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        # Select a specific cell value from the specified table, row, and column
        return self.tab[name][rowId][columnId - 1]  # Return the value at (rowId, columnId), adjusting for 0-based index



# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)