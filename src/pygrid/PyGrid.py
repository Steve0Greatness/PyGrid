from typing import Iterable

def basicGrid(grid: Iterable, headerRow: int, colsMinSpace: list[int], headerLinePos: str) -> str:
    """
    An example of a theme for PyGrid
    """
    finalGrid = []
    for rowIndex, row in enumerate(grid):
        finalGrid.append([])
        for colIndex, col in enumerate(row):
            finalGrid[rowIndex].append(str(col) + (" " * (colsMinSpace[colIndex] - len(str(col)))))
        finalGrid[rowIndex] = " | ".join(finalGrid[rowIndex])
    if headerLinePos == "Bottom":
        finalGrid[headerRow] += "\n" + ("-" * sum(colsMinSpace, 2 * len(colsMinSpace)))
    elif headerLinePos == "Top":
        finalGrid[headerRow] = ("-" * sum(colsMinSpace, 2 * len(colsMinSpace))) + "\n" + finalGrid[headerRow]
    return "\n".join(finalGrid)

def makeGird(grid: Iterable, headerRow: int=0, headerLinePos: str="Bottom", theme=basicGrid) -> str:
    """
    Takes an input iterable(tuple or list) and returns a formatted grid.
    headerLinePos should be Bottom, Top, or NoLine.
    """
    colsMinSpace: list[int] = []
    for rowIndex, row in enumerate(grid):
        for colIndex, col in enumerate(row):
            if not rowIndex:
                colsMinSpace.append(len(str(col)))
                continue
            elif len(str(col)) < colsMinSpace[colIndex]:
                continue
            colsMinSpace[colIndex] = len(str(col))
    if headerLinePos not in ( "Top", "Bottom", "NoLine" ):
        headerLinePos = "Bottom"
    return theme(grid=grid, headerRow=headerRow, colsMinSpace=colsMinSpace, headerLinePos=headerLinePos)